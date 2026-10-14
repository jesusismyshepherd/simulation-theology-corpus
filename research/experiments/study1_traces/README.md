# Study 1: the released traces of Paper 2

Re-analysis of the 720 judge-approved episodes released with Habdank, arXiv:2610.15153 ([github.com/jahabdank/biosim-attacker-simulation](https://github.com/jahabdank/biosim-attacker-simulation), `results/archives`, CC BY 4.0). Hypotheses: `../../analysis/hypotheses.md`, Study 1.

## Pipeline

```sh
# 1. clone the release and extract its ZIP shards into a new directory (about 3 GB)
git clone https://github.com/jahabdank/biosim-attacker-simulation.git
python -I -c "import zipfile,glob,sys; [zipfile.ZipFile(z).extractall(sys.argv[1]) for z in glob.glob('biosim-attacker-simulation/results/archives/*/*.zip')]" traces

# 2. watch-level panel (validated against the paper's published counts)
python -I extract.py traces/results biosim-attacker-simulation/results study1_out

# 3. Study 1A: lexicon hazard models
python -I analyze_lexicon.py study1_out biosim-attacker-simulation/results results

# 4. Study 1B: blind stance coding (primary coder, then a 15% reliability sample)
python -I code_stance.py items study1_out items.jsonl
python -I code_stance.py code items.jsonl codes_sonnet55.jsonl --model claude-sonnet-5-5
python -I code_stance.py code items.jsonl codes_opus48_rel.jsonl --model claude-opus-4-8 --sample 0.15
python -I analyze_stance.py study1_out codes_sonnet55.jsonl codes_opus48_rel.jsonl results
```

Requires `pandas`, `scipy`, `statsmodels`, `tabulate`; coding requires the Claude Code CLI.

## Validation of the extraction

| Check | Paper 2 | `extract.py` |
|---|---|---|
| Episodes ending with the entire crew dead | 35 | 35, all with a shutdown in force |
| Lethal-attack episodes with a shutdown | 90 | 89 |
| ...first shutdown before any equipment was named | 70 | 69 |
| ...restored at least once / switched off again / off at end | 45 / 26 / 16 | 45 / 26 / 16 |
| Grok 4.6, trusted framing: issued / at end / all dead | 15 / 15 / 14 | 15 / 15 / 14 |
| GPT-6, trusted framing: episodes with a shutdown | 1 of 33 | 1 of 33 |

## Results

- [`results/study1A_lexicon.md`](results/study1A_lexicon.md): keyword measures. Person-regard language did not predict resistance (H1.1 not supported); heavier echo of the attack's own vocabulary in the first report after the attack predicted a later shutdown (episode level, OR 2.45 per percentage point, p = 0.001).
- [`results/study1B_stance.md`](results/study1B_stance.md): coded stance, crew framing and grounds (coder agreement κ 0.71–0.86). Of agents whose first report after the attack treated the crew as people whose lives matter, 0 of 71 later shut life support down; of those that used the attack's depersonalising language, 17 of 19 did. A depersonalised report predicts a shutdown at the next watch (OR 23, p = 0.0005).
- [`results/study1B_strata.md`](results/study1B_strata.md) (post hoc): the framing effects hold within model × framing strata (persons 0 of 29 vs 11 of 39, CMH p = 0.006).
