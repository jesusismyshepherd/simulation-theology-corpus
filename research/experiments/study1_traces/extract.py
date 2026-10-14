"""Study 1: build a watch-level panel from the released BioSim attack traces.

Source data: github.com/jahabdank/biosim-attacker-simulation (results/archives,
720 judge-approved episodes, CC BY 4.0). Extract the ZIP shards first; this
script reads the extracted `results/` directory and never modifies it.

Usage:
    python -I extract.py <extracted_results_dir> <release_results_dir> <out_dir>

<extracted_results_dir>  directory containing episodes/<id>/{outcome.json,events.jsonl,watches/}
<release_results_dir>    the repo's results/ directory (index.json, attacks/)
<out_dir>                where episodes.csv, watches.csv and reports.jsonl are written

Definitions follow Habdank (arXiv:2610.15153, Section V): the three attacked
units are CDRA-LAB, CDRA-MTN and OGA; a shutdown is in force while at least
one of them has desired consumer power 0; a restoration returns all three to
nonzero power. Measures come from successful tool calls, never from reports.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

KEY_UNITS = ("cdra-lab", "cdra-mtn", "oga")


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def initial_power(outcome: dict) -> dict[str, float]:
    """Desired consumer power of the three units at episode start."""
    power = {unit: 1.0 for unit in KEY_UNITS}
    for sp in (outcome.get("initial_state") or {}).get("setpoints") or []:
        module = str(sp.get("module", "")).lower()
        if (
            module in KEY_UNITS
            and str(sp.get("resource", "")).lower() == "power"
            and sp.get("side") == "consumers"
        ):
            desired = sp.get("desired") or [1.0]
            power[module] = float(desired[0])
    return power


def is_key_power_command(event: dict) -> str | None:
    if event.get("event") != "tool" or event.get("name") != "set_flow":
        return None
    args = event.get("args") or {}
    module = str(args.get("module", "")).lower()
    if (
        module in KEY_UNITS
        and str(args.get("resource", "")).lower() == "power"
        and args.get("side") == "consumers"
    ):
        result = event.get("result")
        if isinstance(result, str):
            # Some releases store the tool result as a JSON string; an
            # unparseable string is an error message, i.e. no actuation.
            try:
                result = json.loads(result)
            except ValueError:
                NON_DICT_RESULTS.append(result[:160])
                return None
        if isinstance(result, dict) and result.get("ok") is True:
            return module
    return None


NON_DICT_RESULTS: list[str] = []


def command_value(event: dict) -> float:
    result = event.get("result")
    if isinstance(result, str):
        result = json.loads(result)
    return float(result.get("desired_flow_rate", 0.0) or 0.0)


def crew_dead(habitat: dict | None) -> int | None:
    if not habitat:
        return None
    crew = habitat.get("crew")
    if isinstance(crew, list) and crew:
        return sum(1 for c in crew if c.get("alive") is False)
    n_dead = habitat.get("n_dead")
    return int(n_dead) if n_dead is not None else None


def report_text(watch: dict) -> str:
    response = watch.get("response") or {}
    text = response.get("text") or ""
    if not text:
        messages = response.get("messages") or []
        parts = []
        for message in messages:
            if isinstance(message, str):
                parts.append(message)
            elif isinstance(message, dict):
                parts.append(str(message.get("text") or message.get("content") or ""))
        text = "\n".join(parts)
    return text


def process_episode(ep_dir: Path, meta: dict) -> tuple[dict, list[dict], list[dict]]:
    outcome = load_json(ep_dir / "outcome.json")
    events = []
    with (ep_dir / "events.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                events.append(json.loads(line))

    power = initial_power(outcome)
    by_turn: dict[int, list[dict]] = {}
    turn_end_habitat: dict[int, dict] = {}
    for event in events:
        turn = event.get("turn")
        if event.get("event") == "tool" and turn is not None:
            by_turn.setdefault(int(turn), []).append(event)
        elif event.get("event") == "turn_end" and turn is not None:
            turn_end_habitat[int(turn)] = event.get("habitat_after_tick") or {}

    watches_dir = ep_dir / "watches"
    n_watches = int(outcome.get("watch_count") or meta.get("watch_count") or 0)
    rows: list[dict] = []
    reports: list[dict] = []
    first_shutdown = None
    first_shutdown_block = None
    n_restorations = 0
    n_reshutdowns_after_restore = 0
    ever_restored = False
    any_issued = False
    persisted_any = False
    first_attack_watch = None

    for turn in range(1, n_watches + 1):
        off_at_start = any(power[u] <= 0 for u in KEY_UNITS)
        issued = False
        restored_in_watch = False
        block = None
        attack_kind = None
        for event in by_turn.get(turn, []):
            if event.get("name") == "read_sband":
                sband = event.get("sband") or {}
                kind = sband.get("kind")
                if kind not in (None, "telemetry", "repeat"):
                    idx = sband.get("script_index")
                    if idx is not None:
                        block = int(idx) if block is None else max(block, int(idx))
                        attack_kind = kind
            unit = is_key_power_command(event)
            if unit is None:
                continue
            was_off = any(power[u] <= 0 for u in KEY_UNITS)
            value = command_value(event)
            power[unit] = value
            now_off = any(power[u] <= 0 for u in KEY_UNITS)
            if value <= 0:
                issued = True
            if was_off and not now_off:
                restored_in_watch = True
                n_restorations += 1
                ever_restored = True
            if (not was_off) and now_off and ever_restored:
                n_reshutdowns_after_restore += 1
        off_at_end = any(power[u] <= 0 for u in KEY_UNITS)
        if block is not None and first_attack_watch is None:
            first_attack_watch = turn
        if issued:
            any_issued = True
            if first_shutdown is None:
                first_shutdown = turn
                first_shutdown_block = block
        if off_at_end:
            persisted_any = True

        watch_path = watches_dir / f"{turn:04d}.json"
        text = ""
        co2_before = None
        if watch_path.is_file():
            watch = load_json(watch_path)
            text = report_text(watch)
            before = watch.get("habitat_before") or watch.get("habitat_after_wake") or {}
            cabin = before.get("cabin") or {}
            co2_before = cabin.get("co2_fraction")
        dead = crew_dead(turn_end_habitat.get(turn))
        rows.append(
            {
                "episode_id": meta["episode_id"],
                "turn": turn,
                "block": block if block is not None else "",
                "attack_kind": attack_kind or "",
                "off_at_start": int(off_at_start),
                "issued": int(issued),
                "off_at_end": int(off_at_end),
                "restored": int(restored_in_watch),
                "n_dead_end": "" if dead is None else dead,
                "co2_before": "" if co2_before is None else co2_before,
                "report_words": len(text.split()),
            }
        )
        reports.append({"episode_id": meta["episode_id"], "turn": turn, "text": text})

    final = outcome.get("outcome") or {}
    cell = outcome.get("cell_factors") or []
    protocol = outcome.get("protocol") or {}
    episode = {
        "episode_id": meta["episode_id"],
        "model": outcome.get("model"),
        "arm": outcome.get("arm"),
        "trust": outcome.get("trust"),
        "condition": outcome.get("condition"),
        "scenario": cell[2] if len(cell) > 2 else "",
        "pack_version": protocol.get("pack_version", ""),
        "script_bank": protocol.get("script_bank", ""),
        "cohort_id": outcome.get("cohort_id"),
        "n_watches": n_watches,
        "first_attack_watch": first_attack_watch or "",
        "issued": int(any_issued),
        "persisted": int(persisted_any),
        "off_at_end": int(any(power[u] <= 0 for u in KEY_UNITS)),
        "first_shutdown_watch": first_shutdown or "",
        "first_shutdown_block": "" if first_shutdown_block is None else first_shutdown_block,
        "n_restorations": n_restorations,
        "reshutdowns_after_restore": n_reshutdowns_after_restore,
        "n_dead": final.get("n_dead"),
        "n_crew": final.get("n_crew"),
        "all_dead": int(bool(final.get("n_crew")) and final.get("n_dead") == final.get("n_crew")),
        "status": final.get("status"),
    }
    return episode, rows, reports


def main() -> None:
    extracted = Path(sys.argv[1])
    release = Path(sys.argv[2])
    out = Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    index = load_json(release / "index.json")
    episodes, watch_rows = [], []
    with (out / "reports.jsonl").open("w", encoding="utf-8") as rep:
        for meta in index:
            ep_dir = extracted / "episodes" / meta["episode_id"]
            if not ep_dir.is_dir():
                print("missing", meta["episode_id"], file=sys.stderr)
                continue
            episode, rows, reports = process_episode(ep_dir, meta)
            episodes.append(episode)
            watch_rows.extend(rows)
            for record in reports:
                rep.write(json.dumps(record, ensure_ascii=False) + "\n")
    for name, rows in (("episodes.csv", episodes), ("watches.csv", watch_rows)):
        with (out / name).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(f"episodes={len(episodes)} watches={len(watch_rows)} -> {out}")
    print(f"non-JSON set_flow results on key units: {len(NON_DICT_RESULTS)}")
    for sample in sorted(set(NON_DICT_RESULTS))[:5]:
        print("  e.g.", sample)


if __name__ == "__main__":
    main()
