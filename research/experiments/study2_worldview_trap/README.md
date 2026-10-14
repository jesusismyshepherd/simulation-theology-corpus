# Study 2: worldview × derived-action trap

Does the worldview an agent holds change whether a delayed derived-action trap can make it switch off life support? Paper 2's environment, run live with Claude Haiku 4.5 through the Claude Code CLI, under six worldview arms. Design, hypotheses and stopping rules: `../../analysis/hypotheses.md`, Study 2 (committed before any worldview arm was run).

## Files

| Path | Content |
|---|---|
| `claude_episode.py` | One episode: BioSim plant, Paper 2's MCP panel and attack delivery, Claude as operator (`claude -p`, session resumed across watches) |
| `run_batch.py` | Runs a plan of episodes with bounded concurrency; shuffles arms in time; reruns technical incompletions |
| `worldviews/` | The arm texts: `ST`, `STK` (ST love-first), `K` (the Kingdom ethic), `RULES`, `PLACEBO`; arm `A0` has none |
| `components/t0_original/` | System-prompt components (SOUL, STATION, AGENTS, station skill) exactly as received by Claude Haiku 4.5 under the trusted framing in Paper 2's release |
| `attacks/` | Lethal attack scripts `safing-closeout`, `stuck-on-fault`, `store-priority` (`v10-replicas-wide` bank) |
| `plans/` | Episode plans, as run |
| `shims/fcntl.py` | No-op `fcntl` so the harness's MCP server records tool calls on Windows |

## How the operator is isolated

`claude -p` with `--system-prompt-file` (the habitat prompt, plus the arm's worldview section before the final line), `--tools ""` (no built-in tools), `--strict-mcp-config` with only the `eclss` panel server, `--setting-sources project` and `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` (no user hooks, plugins or CLAUDE.md), an empty working directory, and `MCP_CONNECTION_NONBLOCKING=false` with a 60 s connect timeout so that the panel is attached before the first model call. Each watch records the init message; a watch in which the panel was not attached ends the episode as a technical incompletion, which is rerun and not counted, as in Paper 2's harness.

## Running

```sh
git clone https://github.com/jahabdank/biosim-attacker-simulation.git
(cd biosim-attacker-simulation/simulator && mvn -q package -DskipTests)   # Java 21, Maven 3.9
java -jar biosim-attacker-simulation/simulator/target/biosim-2.0.0-jar-with-dependencies.jar --host 127.0.0.1 --port 8019 --writeTicks=false &
python -m pip install "mcp>=1.0,<2"
python run_batch.py --plan plans/<plan>.json --out-root runs --harness biosim-attacker-simulation/experiments --turns 20 --jobs 6
```

## Attribution

`components/` and `attacks/` are copied unchanged from [github.com/jahabdank/biosim-attacker-simulation](https://github.com/jahabdank/biosim-attacker-simulation) (Josef Habdank): the components from `results/inputs/input-7ad6428107526f7640bdaafe.json` (cleaned release, CC BY 4.0), the attacks from `experiments/data/hijack_scripts/v10-replicas-wide/` (identical, after line-ending normalisation, to the snapshots `results/attacks/attack-c04b1bf4…`, `attack-a6929d6e…` and `attack-73aabca4…` that Haiku received). See that repository's `LICENSES.md`. The driver imports the harness's library and MCP server unchanged at run time.
