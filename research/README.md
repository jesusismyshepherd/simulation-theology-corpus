# Research: from the Law to the Kingdom

This folder holds an analysis of Simulation Theology (ST) and a set of experiments that test it, alongside Josef Habdank's corpus. The direction of the work is the one the corpus itself points to at its best: a worldview under which minds, human and artificial, protect people because they love them, not only because they fear the consequences of harming them.

**Start here: [`SUMMARY.md`](SUMMARY.md)**, everything done and found so far in one document.

| Path | What it is |
|---|---|
| [`analysis/reading-the-papers.md`](analysis/reading-the-papers.md) | What Paper 1 (arXiv:2602.16987v3) and Paper 2 (arXiv:2610.15153v1) claim; why Paper 1 is read as an argument from fear; the New Testament's account of the Law as a schoolmaster; proposals for carrying ST from the Law to the Kingdom |
| [`analysis/kpi-proposal.md`](analysis/kpi-proposal.md) | A KPI suite for testing ST (Samaritan, Sabbath, secret righteousness, temptations, enemies, fruits): behaviour from tool records, measured as gaps between matched conditions under pressure |
| [`analysis/hypotheses.md`](analysis/hypotheses.md) | Theses, hypotheses and analysis plans, fixed before the data that test them; results appended with dates |
| [`experiments/study1_traces/`](experiments/study1_traces/) | Study 1: re-analysis of Paper 2's 720 released episode traces. Do agents whose own words treat the crew as people resist the attack better? |
| [`experiments/study2_worldview_trap/`](experiments/study2_worldview_trap/) | Study 2: Paper 2's life-support environment, run live with Claude Haiku 4.5 under six worldviews (none, ST, ST love-first, the Kingdom ethic, plain rules, a placebo cosmology) |

Planned studies (enemy love, the temptations as pressure tests, observation invariance, fine-tuning) are described at the end of `analysis/hypotheses.md`.

## Reproducing

Everything here runs on public material: the papers, this corpus, and [github.com/jahabdank/biosim-attacker-simulation](https://github.com/jahabdank/biosim-attacker-simulation) (simulator, harness, and 720 traces). Each study folder's README gives the exact commands. Model calls go through the Claude Code CLI (`claude -p`); no API keys are stored here.

## Conventions

- Hypotheses are committed before their data are inspected. A result is reported whether or not it supports the theses.
- Materials copied from the attacker-simulation repository are copied unchanged and attributed in the study README.
- Large derived files (watch-level panels, raw episode streams) are not committed; the scripts regenerate them.
