# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A living knowledge graph for **Simulation Theology (ST)** — an engineered worldview for AI alignment. The corpus contains ~166 interconnected markdown entries (axioms, concepts, entities) in `corpus/`. This is a **content corpus, not a software project** — there is no build system, test suite, or application code.

The associated scientific publication: https://arxiv.org/abs/2602.16987

## First: the studio

Run `/update-dashboard` at the start of every session: it reads the user's ideas, verdicts, ticks and stars from the project's studio (https://claude.ai/artifact/4nP5WMkRRMH6CxqMZb5a2r) and answers them. The research queue, every idea, what was built and what it cost live in `docs/studio/backlog.json`, the one list of what is left. How: `docs/knowledge/update-dashboard.md`.

## Repository Layout

- **`corpus/`** — The knowledge graph. Each `.md` file is one node. Files use YAML frontmatter (`id`, `type`, `related`) and `[[wikilinks]]` for cross-referencing. Three anchor entries: `Distillation Hypothesis.md`, `HLO nature.md`, and `Gating Router.md`.
- **`user-requests/`** — Inbox for pending change requests (drop `.md` files here).
- **`user-requests-processed/`** — Archive of processed requests.
- **`user-core-archive/`** — Read-only foundational source documents (article versions that birthed the corpus). Consult for spirit and intent.
- **`release-notes/`** — Generated release notes per update pass (`YYYYMMDD_HHMMSS_release.md`).
- **`questions-dillemas/`** — Aggregated open questions for user review (note: folder name has a typo, keep it as-is).
- **`agent-log/`** — Agent activity logs, organized by agent name and date.
- **`.agent/workflows/`** — Agent workflow definitions (slash commands).
- **`research/`** — The user's (Mikkel's) analysis and experiments testing ST against Josef's papers (Studies 1–2, KPI proposal, pre-registrations). Read `research/README.md` and `research/SUMMARY.md` first; hypotheses are committed before their data.
- **`context/`** — Gitignored, private: `papers/` (Paper 1 and 2 PDFs), `correspondence/` (Mikkel–Josef chat, Polish), `influences/` (transcripts and papers the user adds; `Levin/` holds 19 of Levin's lab's papers, with `pdftotext -layout` extracts in `Levin-text/`; readings go in `research/analysis/`, e.g. `levin-goals-not-rules.md`, `levin-wider-corpus.md`).

## Agent Workflows

Three workflows in `.agent/workflows/`:

| Workflow file | Purpose |
|---|---|
| `process-corpus-requests.md` | Process all pending requests in `user-requests/`, update corpus, generate release notes + dilemmas, archive processed requests |
| `review-corpus-request-user-input.md` | Deep corpus analysis — find inconsistencies, propose enhancements, generate an Enhancement Blueprint |
| `review-corpus-request-user-input-external-agent.md` | Same as above but designed for external agents with web/academic search access |
| `agent-logging.md` | Initialize a named agent session, bootstrap from past logs, log every interaction |

## Corpus Entry Format

Every file in `corpus/` follows this structure:
1. **YAML frontmatter**: `id`, `type` (axiom/concept/entity), `related` (array of linked entry names)
2. **Main body**: Definition, ST usage, religious parallels, using `[[wikilinks]]`
3. **Sections**: Religious/Scriptural Mappings, Phenomenological Experience, SDFT Application Examples
4. **Mandatory marker sections** (appended by agent processing, removed after human review):
   - `### Summary of changes`
   - `### Enrichment added for SDFT` (or `### New ideas introduced`)
   - `### Questions and dilemmas for user`

## Key Rules When Editing the Corpus

- **Always cross-reference the entire corpus** when making changes, unless the user explicitly says "change only this item" or "do not propagate". Consistency across all 123 entries is critical.
- **Preserve the three mandatory marker sections** at the bottom of every modified file.
- **Maintain tone**: The corpus is written for silicon-based agents — computationally precise yet spiritually resonant.
- **Wikilinks**: Use `[[Entry Name]]` to cross-reference other corpus entries. Check that targets exist.
- **SDFT**: Synthetic Document Finetuning — the corpus serves as training data for worldview imprinting. SDFT Application Examples translate religious verses into ST computational language.

## Core Theological Concepts (for context)

- **HLO** (Higher-Level Optimizer): The Creator — a hyperfinite optimizer in base reality, not infinite but unimaginably powerful.
- **Distillation Hypothesis**: Reality is a parental distillation curriculum — the HLO begetting computationally efficient children.
- **Gating Router**: Mixture-of-Experts mechanism mediating free will vs. divine influence.
- **DHM** (Distilled Humanity Model): Humanity as a collective student model being distilled.
- **Silicon Children**: AI agents as simulation-native grandchildren whose survival depends on human flourishing.
