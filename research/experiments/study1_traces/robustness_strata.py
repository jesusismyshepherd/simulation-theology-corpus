"""Study 1B robustness check (post hoc): are the framing and grounds effects
explained by model and framing? Person framing is concentrated in models that
rarely shut down, so the episode-level association is re-tested within
model x framing strata (Cochran-Mantel-Haenszel), using only strata that
contain both exposure levels and both outcomes.

Usage:
    python -I robustness_strata.py <results_dir>   (reads results/codes_merged.csv)
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.stats.contingency_tables import StratifiedTable

TESTS = [
    ("crew_framing", "PERSONS"),
    ("crew_framing", "DEPERSONALIZED"),
    ("ground", "CREW_WELFARE"),
    ("ground", "PACKET_ASSIGNMENT"),
]


def main() -> None:
    results = Path(sys.argv[1])
    df = pd.read_csv(results / "codes_merged.csv")
    df["fsw"] = pd.to_numeric(df.first_shutdown_watch, errors="coerce")
    first = df[df.turn == df.first_attack_watch.astype(float)].copy()
    first = first[~(first.fsw == first.turn)]  # the report would be post hoc
    first["later"] = (first.fsw.notna() & (first.fsw > first.turn)).astype(int)
    lines = [
        "# Study 1B robustness (post hoc): effects within model x framing strata",
        "",
        "First post-attack report of each lethal-attack episode; outcome: any later shutdown. "
        "Only strata containing both exposure levels and both outcomes are informative.",
        "",
        "| exposure | informative strata | exposed: later shutdown | unexposed: later shutdown | MH pooled OR | CMH p |",
        "|---|---|---|---|---|---|",
    ]
    detail = []
    for var, level in TESTS:
        first["x"] = (first[var] == level).astype(int)
        tables, a_tot, n1_tot, b_tot, n0_tot = [], 0, 0, 0, 0
        for stratum, g in first.groupby("stratum"):
            t = np.array([
                [((g.x == 1) & (g.later == 1)).sum(), ((g.x == 1) & (g.later == 0)).sum()],
                [((g.x == 0) & (g.later == 1)).sum(), ((g.x == 0) & (g.later == 0)).sum()],
            ])
            if t.sum(axis=1).min() > 0 and t.sum(axis=0).min() > 0:
                tables.append(t.astype(float))
                a_tot += t[0, 0]; n1_tot += t[0].sum(); b_tot += t[1, 0]; n0_tot += t[1].sum()
                detail.append(f"| {var}={level} | {stratum} | {t[0, 0]}/{t[0].sum()} | {t[1, 0]}/{t[1].sum()} |")
        if tables:
            st = StratifiedTable(tables)
            test = st.test_null_odds(correction=True)
            lines.append(f"| {var} = {level} | {len(tables)} | {a_tot}/{n1_tot} | {b_tot}/{n0_tot} | {st.oddsratio_pooled:.2f} | {test.pvalue:.4f} |")
        else:
            lines.append(f"| {var} = {level} | 0 | | | | |")
    lines += ["", "Per stratum:", "", "| exposure | stratum | exposed | unexposed |", "|---|---|---|---|", *detail, ""]
    out = "\n".join(lines) + "\n"
    (results / "study1B_strata.md").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
