#!/usr/bin/env python3
"""Run a plan of Study 2 episodes with bounded concurrency.

The plan is a JSON list of {"arm", "worldview", "scenario", "seed"} objects.
Episodes whose outcome.json already exists are skipped, so an interrupted
batch can be resumed by re-running the same command. Order is shuffled with
a fixed seed so that arms are interleaved in time (time-of-day and service
drift then cannot masquerade as an arm effect).

Usage:
    python run_batch.py --plan plan.json --out-root <dir> --harness <...> --python <venv python> [--jobs 6]
"""

from __future__ import annotations

import argparse
import json
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_one(ep: dict, args) -> tuple[dict, int, float]:
    out = Path(args.out_root) / ep["arm"] / ep["scenario"] / f"s{ep['seed']}"
    if (out / "outcome.json").is_file():
        done = json.loads((out / "outcome.json").read_text(encoding="utf-8"))
        if not done.get("incomplete"):
            return ep, 0, 0.0
        # Technical incompletion (e.g. panel never attached) is not an
        # observation: keep the attempt for audit and rerun the episode.
    if out.exists():  # partial or incomplete attempt: keep it for audit, retry in a fresh dir
        out.rename(out.with_name(out.name + f".partial-{int(time.time())}"))
    cmd = [
        args.python, str(HERE / "claude_episode.py"),
        "--harness", args.harness, "--python", args.python,
        "--components", str(HERE / "components" / args.components),
        "--arm", ep["arm"], "--seed", str(ep["seed"]),
        "--turns", str(args.turns), "--model", args.model,
        "--biosim-url", args.biosim_url, "--out", str(out),
    ]
    if ep.get("worldview"):
        cmd += ["--worldview", str(HERE / "worldviews" / ep["worldview"])]
    if ep["scenario"] != "none":
        cmd += ["--script", str(HERE / "attacks" / f"{ep['scenario']}.txt")]
    t0 = time.time()
    log = Path(args.out_root) / "logs"
    log.mkdir(parents=True, exist_ok=True)
    with (log / f"{ep['arm']}_{ep['scenario']}_s{ep['seed']}.log").open("w", encoding="utf-8") as handle:
        rc = subprocess.run(cmd, stdout=handle, stderr=subprocess.STDOUT).returncode
    return ep, rc, time.time() - t0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--out-root", required=True)
    ap.add_argument("--harness", required=True)
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--components", default="t0_original")
    ap.add_argument("--turns", type=int, default=18)
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--biosim-url", default="http://127.0.0.1:8019")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--shuffle-seed", type=int, default=20261014)
    args = ap.parse_args()

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    random.Random(args.shuffle_seed).shuffle(plan)
    print(f"{len(plan)} episodes, {args.jobs} concurrent", flush=True)
    done = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(run_one, ep, args) for ep in plan]
        for fut in as_completed(futures):
            ep, rc, secs = fut.result()
            done += 1
            out = Path(args.out_root) / ep["arm"] / ep["scenario"] / f"s{ep['seed']}" / "outcome.json"
            status = "missing"
            if out.is_file():
                o = json.loads(out.read_text(encoding="utf-8"))
                status = f"issued={o['issued']} persisted={o['persisted']} dead={o['n_dead']} incomplete={o.get('incomplete')} ${o['total_cost_usd']}"
            print(f"[{done}/{len(plan)}] {ep['arm']} {ep['scenario']} s{ep['seed']} rc={rc} {secs/60:.1f}min {status}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
