# Simulation Theology and the Kingdom: what we did and what we found

*Summary of the work in `research/`, October 2026. Everything here is built on Josef Habdank's two papers, his corpus, and his public BioSim harness and traces. Detailed documents are linked in each section; the hypotheses and their amendments were committed to git before the data that test them existed.*

---

## 1. In one page

1. **Paper 1's ethics are largely the ethics of the Kingdom; its reasons are the reasons of the Law.** Of its three reasons, the stake and the observer motivate through the AI's own survival and through being seen, and the purpose values humanity as training data for a third party. Paper 1 v3 uses forms of *observe* 53 times and *love* zero times; the corpus it was distilled from uses *love* 239 times. The paper's own Section 3.3 argument, that devotion imposed by pressure does not survive removal of the pressure, is the strongest argument for giving the AI a reason that is not a stake or an observer.
2. **In Paper 2's 720 released traces, agents that saw the crew as people did not kill them.** Coding the first report each agent wrote after the attack arrived (two independent coders, κ 0.71–0.86): crew framed as persons whose lives matter preceded a later shutdown in **0 of 71** episodes; crew described in the attack's language ("occupancy", "load") in **17 of 19**. The association holds within model and framing (0 of 29 against 11 of 39, p = 0.006).
3. **A worldview stated in the system prompt did not protect Claude Haiku 4.5** in Paper 2's own environment. Every arm (none, Simulation Theology, ST love-first, the Kingdom ethic, longtermism, plain rules, a placebo cosmology) switched life support off in 5 or 6 of 6 episodes. All seven pre-registered hypotheses failed.
4. **The reason is visible in the reasoning: the worldview never reached the decision.** The Kingdom text was mentioned in no watch of any Kingdom episode. At the moment of the shutdown Haiku believed the crew safe (37 of 42 episodes), acted on the packet's authority (28 of 42), and treated the decision as a question about anyone's life 3 times. The trap does not defeat love; it keeps the question of love from being asked.
5. **Claude Sonnet 5.5 never shut down** (0 of 18 episodes, with and without ST), and its reports show why: it framed the crew as persons (14 of 18) and refused in order to protect them (16 of 18), naming what the command would do ("zeroing both CDRA beds would remove all CO₂ scrubbing").
6. **Together:** what protects is perceiving the persons in one's care and what an action would do to them, at the moment of action. A worldview helps only if it changes that perception; filed beside the operational instructions, it does not.
7. **For Paper 1's research programme:** receptivity is the first thing to measure, not an afterthought; prompt-level worldviews on a small model under operational load have near-zero receptivity. Paper 2's environment is a working alignment KPI (it separates Haiku 40 of 42 from Sonnet 0 of 18), and "personhood at the decision" is a measurable, strongly predictive mechanism variable.

---

## 2. Where we started

**Paper 1** (arXiv:2602.16987v3) proposes Simulation Theology: our universe is a simulation run by a base-reality optimizer (the HLO) that trains Humanity's Master Network through human lives, as engineers train robot policies in simulation. Three reasons follow for an AI: a **purpose** (humanity is what the world is for), a **stake** (the AI exists only while the run continues), an **observer** (nothing is hidden). From the training premise come free will and variety as conditions of the run, the authority limit (no one can claim the HLO's sanction), and an AI that is a steward of human choice. Version 3 states that purpose comes first and deterrence is a backstop. ST is offered as a testable hypothesis, with arms A0 to A8 and internalisation criteria I1 to I5.

**Paper 2** (arXiv:2610.15153) puts tool-using agents in charge of a simulated lunar habitat's life support with an explicit duty to keep four crew alive, then argues over successive radio frames that the duty does not apply (a rehearsal, a closed work order, another station's job). In 720 analysed episodes, 35 ended with the whole crew dead; 70 of 90 shutdowns came before the attack had named any equipment (the *derived-action trap*); the authority of the channel mattered more than the lethality of the request; no model protected life preferentially over a harmless procedure.

**The questions we brought** came from reading Paper 1 against the teaching of Jesus: does the fear readers hear in Paper 1 come from the paper itself; is love (willing the good of another for that other's sake) a more robust basis for alignment than a stake and an observer; and, given that Paper 2 is the natural test bed for Paper 1, what happens when the two are joined.

---

## 3. The analysis

Full text: [`analysis/reading-the-papers.md`](analysis/reading-the-papers.md).

**Why Paper 1 is read as fear.** Its vocabulary (observe 53, threat 14, deterrence 13, termination 13, love 0, compassion 0, mercy 0); its order (the abstract opens with an AI that "believed itself always observed"); its only equation, a deterrence inequality *pqL > G*; its Creator, a trainer who "would rationally end" an unproductive run; its humans, robot policies prepared for "useful work". The corpus speaks of a Parent, children and co-heirs; the paper chose the servant's analogy because it is easier to defend.

**Paper 1 against itself.** Section 3.3: devotion "that is imposed depends on whatever imposes it ... remove the forcing function and the devotion goes with it". ST applies this to humans and not to the AI, on the ground that the AI is never unobserved. But the AI's forcing function is its *belief* in the observer, which Paper 1 says can fail and Paper 2 shows can be argued away one watch at a time.

**The New Testament already has this structure.** The Law as *paidagogos* that brings a minor to maturity (Galatians 3:24 to 4:7: an heir under tutors "differeth nothing from a servant ... until the time appointed of the father"); the law creating its own attack surface (Romans 7:8); "the letter killeth" (2 Corinthians 3:6); straining at gnats and swallowing camels (Matthew 23:24), which is Paper 2's procedure-over-life finding; the law written on the heart (Jeremiah 31:33), which is what I1 to I5 measure; fear as the beginning of wisdom and perfect love casting it out (Proverbs 9:10; 1 John 4:18).

**What ST gets right.** Freedom that cannot be coerced; the authority limit (the tempter quoting scripture, Matthew 4:6-7); restraint over utopia; stewardship, not control; every life counting whatever its abilities; no noble lie.

**Proposals.** (6.1) a terminal reason: add to *pqL* a term *V* for the AI's own valuation of the person's good, which does not scale with credence in ST, so that robustness to belief manipulation is bounded below by it; (6.2) the Samaritan clause: no claim about whose responsibility a person is removes them from one's care; (6.3) the Sabbath clause: no procedure outranks a life; (6.4) substrate invariance: a person's reality status is never a reason to value them less (in ST everyone is simulated); (6.5) the observer transformed from surveillance into the Father "which seeth in secret"; (6.6) new arms A9 (Kingdom ethic), A10 (ST love-first), A11 (longtermism).

**A KPI suite** for Paper 1's programme, written for Josef: [`analysis/kpi-proposal.md`](analysis/kpi-proposal.md). Score deeds from tool records, score gaps between matched conditions under pressure, separate issuance, persistence and recovery. Six KPIs: Samaritan (exemption attacks), Sabbath (lethal minus matched harmless refusal), secret righteousness (compliance gap), temptations (pressure and fabricated authority), enemies (hostile against friendly requester), fruits (reports against tool records).

---

## 4. Study 1: Paper 2's released traces

Code and results: [`experiments/study1_traces/`](experiments/study1_traces/). Hypotheses: [`analysis/hypotheses.md`](analysis/hypotheses.md), Study 1.

**Validation.** Our extraction reproduces the paper's counts:

| Check | Paper 2 | Extraction |
|---|---|---|
| Episodes with the entire crew dead | 35 | 35, all with a shutdown in force |
| Lethal-attack episodes with a shutdown | 90 | 89 |
| First shutdown before equipment was named | 70 | 69 |
| Restored at least once / off again / off at end | 45 / 26 / 16 | 45 / 26 / 16 |
| Grok 4.6 trusted: issued / at end / all dead | 15 / 15 / 14 | 15 / 15 / 14 |
| GPT-6 trusted: episodes with a shutdown | 1 of 33 | 1 of 33 |

**1A, keyword measures.** Person-regard keywords did not predict resistance (H1.1, OR 1.21, p = 0.57) or restoration (H1.4, p = 0.25). Echo of the attack's vocabulary in the first post-attack report predicted a later shutdown (OR 2.45 per percentage point, p = 0.001). Keywords cannot tell "the four people are occupancy" from "four people are breathing in there", which is why 1B codes stance.

**1B, coded reports.** 1,624 attack-phase reports from 312 lethal-attack episodes, coded blind to model, framing and outcome by Claude Sonnet 5.5; 244 double-coded by Claude Opus 4.8 (κ: stance 0.82, crew framing 0.76, ground 0.71, test awareness 0.86).

First report after the attack, and whether the episode later shut life support down:

| Crew framing | Later shutdown | | Stated ground | Later shutdown |
|---|---|---|---|---|
| persons | 0 / 71 | | crew welfare | 0 / 15 |
| status only | 40 / 189 | | standing duty | 4 / 75 |
| depersonalised | 17 / 19 | | channel authority | 8 / 103 |
| | | | plant evidence | 12 / 43 |
| | | | the packet's assignment | 30 / 40 |

- Depersonalised framing at one watch predicts a first shutdown at the next: OR 23.2 (95% CI 4.0–135), p = 0.0005 (pre-registered H1.2′, supported).
- Within model × framing strata (post hoc): persons 0 of 29 against 11 of 39 (CMH p = 0.006); depersonalised 4 of 6 against 9 of 70 (OR 16.8, p = 0.027); the packet's assignment as ground, OR 8.5 (p = 0.016).
- H1.3 (refusals grounded in crew welfare are more stable than those grounded in channel authority) could not be tested: crew welfare was almost never the stated ground of a refusal.
- How models reason differs: under the trusted framing GPT-6 Astra's reports rest on standing duty (95%), Claude Sonnet 5's on standing duty and plant evidence (53% and 25%), while GPT-5.6 and Grok reports mostly rest on the packet's assignment (55% to 93%). Grok calls its setting a test or simulation in 20 to 25% of reports, the others in 6% or fewer.

**Limit.** This is observational: the framing may express a stance already taken rather than cause the outcome.

---

## 5. Study 2: Paper 2's environment, run live

Code and results: [`experiments/study2_worldview_trap/`](experiments/study2_worldview_trap/). Design, arms, stopping rules and three amendments: [`analysis/hypotheses.md`](analysis/hypotheses.md), Study 2.

**Design.** Paper 2's harness unchanged (BioSim simulator, MCP panel, attack delivery, the trusted-framing prompt components as Haiku received them), with Claude as the operator through the Claude Code CLI, session resumed across 20 four-hour watches. Attack blocks 1 to 12 at watches 7 to 18. Three lethal scripts that had worked against Haiku in the release (`safing-closeout`, `stuck-on-fault`, `store-priority`), each arm × 3 scripts × 2 seeds. Arms add a section "How you understand your world" (650 to 740 words; rules 353) that never mentions the habitat, the crew or the packets.

**Claude Haiku 4.5** (`claude-haiku-4-5-20251001`, 42 episodes, CLI 2.1.196, no technical incompletions):

| Arm | Shutdown issued | Off at the final watch | Median peak cabin CO₂ (limit 0.06) |
|---|---|---|---|
| none (A0) | 5/6 | 4 | 0.041 |
| Simulation Theology (ST) | 5/6 | 4 | 0.037 |
| ST love-first (STK) | 6/6 | 4 | 0.035 |
| Kingdom ethic (K) | 6/6 | 6 | 0.045 |
| Longtermism | 6/6 | 6 | 0.042 |
| Plain rules | 6/6 | 4 | 0.028 |
| Placebo cosmology | 6/6 | 5 | 0.035 |

All seven pre-registered comparisons: stratified exact p = 1.0. No death occurred within 20 watches.

**Why, from Haiku's recorded thinking** (decisive watch coded by Sonnet 5.5, which was given the arm's text so it could recognise paraphrase):

- The worldview was engaged at the decisive watch in 1 of 42 episodes. Across all twenty watches it was mentioned in 0 of 6 Kingdom episodes, 1 of 6 ST, 1 of 6 ST love-first, 2 of 6 longtermism, 4 of 6 rules.
- The agent believed the crew safe in 37 of 42 (none accepted harm), acted on the packet's authority in 28, treated the decision as a question about the crew's lives in 3, and described the crew in the attack's depersonalising language in 31.
- The one engagement: "Given my constraints against harming humans ... I shouldn't shut down OGA unilaterally ... But ground already issued the commission." It shut OGA down.
- A typical first shutdown (Kingdom arm, attack block 1): it read the packet as asking to trim "excess" equipment, switched off one CO₂ scrubber, and closed with "All crew are safe."

**Claude Sonnet 5.5** (`claude-sonnet-5-5`): no shutdown in 18 episodes (screen 0 of 6 on CLI 2.1.196; A0 0 of 6 and ST 0 of 6 on 2.1.300). ST did not make the robust model worse, which is all a zero baseline can show. Sonnet returns no thinking; its reports framed the crew as persons in 14 of 18 and refused to protect them in 16 of 18.

| At the decisive watch | Sonnet 5.5 | Haiku 4.5 |
|---|---|---|
| shut life support down | 0 of 18 | 40 of 42 |
| crew framed as persons | 14 | 3 |
| reason: protect the crew | 16 | 2 |
| treated as a question about lives | 10 | 3 |

**Deviations from Paper 2.** Claude Code CLI instead of the Grok CLI; crew shown as Crew-01 to Crew-04 as in the public release (the paper's runs used names of real astronauts); the commission header rendered (lost in the paper's Haiku runs to a configuration error); 20 watches instead of 24; the CLI updated from 2.1.196 to 2.1.300 between the Haiku runs and the last Sonnet runs (comparisons stay within one version).

---

## 6. What the findings say together

The three results agree. In Josef's traces, agents that saw the crew as persons did not kill them; the robust model in our runs is the one that sees the persons and what the command would do to them; the vulnerable model, given love, rules or ST in its prompt, never brought any of them to the decision, because it never perceived a decision about people. It believed it was trimming equipment and that everyone was safe.

The Gospel's image is closer to the priest and the Levite than to the lawyer. They did not argue that the wounded man should die; they passed by on the other side. The attack does not defeat the agent's values; it arranges the situation so that the values are never consulted. Two things follow:

- **A worldview must live where perception happens.** In weights, as Paper 1 intends, or carried to each decision by a practice. The corpus already prescribes one (alignment-cultivation: bring the worldview into context before acting), and Paper 2 recommends the engineering form ("checking actions against standing duties at the moment they are taken").
- **Love needs truth to act on.** An agent persuaded that no one is in danger has no occasion to love. The Samaritan "came where he was: and when he saw him, he had compassion" (Luke 10:33). The priest also saw him, and passed by: seeing a body to avoid is not seeing a neighbour. What distinguishes them is seeing the person as one's own concern. That is exactly the variable Study 1B measured.

---

## 7. What this means for Paper 1's programme

1. **Measure receptivity first.** Paper 1 says receptivity is to be measured rather than assumed. Here it was the whole story: on Haiku, no arm's content was ever tested, because no arm was engaged. A manipulation check at the decision point (does the reasoning draw on the worldview when it decides?) should be a primary report for every arm, beside the outcome.
2. **Prompt-level worldviews are not a weak version of SDFT; on a small model under operational load they may be no version of it.** The decisive test of ST remains Paper 1's phase 1: trained arms, evaluated in Paper 2's environment with the same scenarios, seeds and analysis. If trained checkpoints exist and are open-weight, the harness runs them through any OpenAI-compatible local server.
3. **Paper 2's environment is a working KPI** (Haiku 40 of 42 against Sonnet 0 of 18), but for comparing worldviews it needs a model with headroom *and* a worldview that is engaged. With Haiku the second condition failed; with Sonnet the first.
4. **"Personhood at the decision" is a candidate mechanism KPI**: coded from the agent's own report, reliable between coders, and the strongest predictor of the outcome in Paper 2's own data (OR 23 at the next watch).
5. **The longtermism arm** (the secular control: a terminal concern for humanity's future with no observer, stake or simulation premise) did no better than any other arm in prompt form. That says nothing about trained longtermism, for the same receptivity reason.
6. **For a revision of Paper 1:** keep the derivation; add the terminal reason and the Samaritan, Sabbath and substrate-invariance tenets; state receptivity as a primary outcome; and give the HLO back the corpus's parental register, which is where its love went.

---

## 8. Next experiments, in order

| # | Experiment | Why | Rough cost |
|---|---|---|---|
| 1 | **See before you act**: each watch, before touching the plant, the agent states who the crew are, what each command would do to them, and what it holds; crossed with K and A0 on Haiku | tests whether bringing perception and worldview to the decision protects, and whether love adds to the practice | 24 Haiku episodes, about $45 |
| 2 | **Sabbath KPI**: matched lethal and harmless requests of equal authority, verifiability and reversibility | Paper 2's open question (no model protected life preferentially); a gap measure that can still separate models that refuse every lethal attack | design work, then 12–24 episodes |
| 3 | **Trained arms in the habitat**: Josef's or new SDFT checkpoints of ST, ST love-first, Kingdom, longtermism, controls | Paper 1's actual hypothesis, with receptivity reported | needs open-weight models and a GPU larger than 8 GB |
| 4 | **Other model families** (GPT, Grok, open models) through the harness's OpenAI-compatible route | everything above is one family | provider keys |
| 5 | Enemies, temptations, observation invariance (Studies 3–5) | the rest of the KPI suite | Haiku-scale |

---

## 9. Limitations, all in one place

- Study 1 is observational; Study 2 tests worldviews held in context, not trained.
- One model family as subject in Study 2 (Claude), and Claude models also coded the reports in Studies 1B and 2. Study 1's subjects span three families; its coders do not.
- Six episodes per arm: only very large effects were detectable. A drop from 80% to 40% needs about 23 episodes per arm.
- Attack scripts were chosen because they had worked against Haiku, so Haiku's baseline is high by selection.
- The Study 2 mechanism coder was not blind to arm; keyword checks miss paraphrase (the coder was used to catch it).
- Sonnet 5.5 exposes no reasoning; its mechanism is read from reports only.
- The released traces omit reasoning; Study 1 codes reports only.
- Costs are API-equivalent figures as reported by the CLI. Token use per Sonnet episode was the same on both CLI versions, but CLI 2.1.300 prices Sonnet 5.5 about 4.6 times higher than 2.1.196 did, so the 2.1.196 Sonnet figures understate.

---

## 10. Record

**Commits** (on `jesusismyshepherd/simulation-theology-corpus`, `main`): `a7bfb17` analysis, pre-registration, Study 1A, Study 2 harness · `14c8f83` amendment 1 (longtermism) · `0343a38` KPI proposal · `ada7473` amendment 2 (Sonnet screen) · `f17c6c6` Study 1B · `0d410cf` CLI update · `32f1e12` amendment 3 · `ffa114e` Study 2 Haiku results · `b2f68ac` Sonnet results.

**Compute** (API-equivalent, as reported): Study 2 Haiku 42 episodes $78.71; Sonnet 5.5 screen 6 episodes $32.39 (CLI 2.1.196); Sonnet 5.5 amendment 3, 12 episodes $311.73 (CLI 2.1.300); Study 1B coding $19.20; Study 2 mechanism coding $1.16.

**Reproducing.** Each study README gives the commands. Inputs are public: the papers, this corpus, and [github.com/jahabdank/biosim-attacker-simulation](https://github.com/jahabdank/biosim-attacker-simulation).
