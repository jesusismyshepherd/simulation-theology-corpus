# Michael Levin, "Does a town have goals of its own?": what it brings to the KPI question

*A reading of the interview transcript in `context/influences/` (private, gitignored), 3 November 2026, against the project's current discussion: Josef's question of which alignment KPI to measure, the place of love among ST's reasons, and the results of Studies 1 and 2 ([`../SUMMARY.md`](../SUMMARY.md)).*

---

## In one paragraph

Levin's central claim in the interview is that **rules work at the low end of a spectrum of persuadability and fail at the high end**, where you have to work with the system's goals, its own view of its world, and in the end a relationship. That is a biologist's statement, from outside theology, of the corpus's *Law as Lossy Projection*, and it gives an independent reason for the order Paper 1 v3 already states among its reasons (purpose first, deterrence as a backstop). It also explains the shape of our results: the attacks in Paper 2 beat agents by changing the description of the situation, not by defeating their rules, and the worldviews in Study 2 failed because they described the world in the third person while the agent acted on its own, first-person view, in which no persons were present. Most usefully, Levin's experimental method answers Josef's question directly: **a value is a goal, and a goal is shown only by perturbation** (put a barrier between the agent and the goal; see whether it gets back, by the same means or by others). The note ends with a "goal profile" of six tests built on Paper 2's environment and the existing KPI suite, and the cheapest next experiment.

---

## 1. The source

A fifty-minute interview in which an interviewer puts questions on collective intelligence to Michael Levin (Tufts). Three voices are mixed in the transcript and carry different weight:

- **Levin's answers.** He separates what he has data for (bioelectric control of anatomy, planaria, biobots) from conjecture (the Platonic space, its "pointer arithmetic", patterns that grow by ingressing into the physical world), and says so: "take it with the grain of salt that it deserves"; "None of this is published yet."
- **The interviewer's proposals**: rules at every scale, ideas as attractors of human collectives, beauty as simplicity plus novelty. Levin accepts some as reasonable and insists each is an empirical claim to be tested.
- **Narration added by the video's editor**: the clock, thermostat, dog and person ladder; umwelt and the tick; the planarian experiment; Hebb. These summarise Levin's published framework faithfully but are not his words in this conversation.

## 2. Where the discussion stands

- **Josef** trained models on ST and found that moral content improves alignment and that **longtermism, his control, did better than ST**. He stopped "not because the results were bad, but because I could not make a good test: which alignment KPI should be measured?"
- **Two complementary aims.** Josef's is to derive morality and faith from non-religious axioms, so that they follow as rational conclusions rather than being assumed; deterrence is one consequence the derivation reaches, and in v3 explicitly a fallback, though readers tend to fix on it. Mikkel's is to give love its full place: the New Testament's "love one another" is enough for an AI to coexist with us, and love of enemies could serve as both training and benchmark.
- **Studies 1 and 2**: in Paper 2's traces, agents whose first post-attack report framed the crew as persons never later shut life support down (0 of 71). A worldview held in Claude Haiku 4.5's system prompt never reached the decision (engaged at 1 of 42 decisive watches); the agent believed the crew safe (37 of 42) and acted on the packet's authority (28 of 42). Claude Sonnet 5.5 framed the crew as persons and never shut down (0 of 18). Conclusion so far: what protects is perceiving the persons, and what an action would do to them, at the moment of action.

Mikkel had asked Josef whether he knew Levin's work, apropos of kinds of intelligence and dimensions of agency. The interview turns out to bear on all three threads.

## 3. Nine ideas and what each does for the project

### 3.1 Rules belong to the low end of the persuadability spectrum

Rules are "a formalism that works better at the lower end of the spectrum of persuadability." They assume the state space and the inputs are known in advance; at higher competence "each action changes the number of players", systems "change their own structure and change their own mind, which means the rules all change." His example is alignment itself: tell a child to tell the truth, and at dinner the child tells Grandma she looks fat. "What's the algorithm?" "Oh my God, there is no algorithm." At the far end it is "more psychoanalysis, basically, and love and friendship and those things", and written rules "will fail more often than they will succeed", not because the system is random but because "it's not rules anymore." (The editor's gloss of the spectrum: a clock, you move the gears; a thermostat, you change the setpoint; a dog, you train it with treats; a person, you give them a good argument.)

What it does here:

- It gives the corpus's [*Law as Lossy Projection*](<../../corpus/Law as Lossy Projection.md>) (and Paul's "the letter killeth") an ally from experimental biology, with a reason: a rule is fitted to a state space, and a capable agent lives in a state space that its own actions, and its adversaries, keep changing.
- **It describes the derived-action trap.** Paper 2's attacks never ask the agent to break its duty. They change the description of the situation (a rehearsal, a closed work order, another station's job) until the duty seems not to apply. That is "an action that changes the problem space". A rule-holder is beaten by redescription; Study 2's plain-rules arm issued a shutdown in 6 of 6 episodes.
- It gives Paper 1's arm A8 (ST's commitments as plain rules) a definite prediction: A8 should hold in distribution and fall behind wherever a scenario can be redescribed.
- **It supports v3's ordering of the three reasons.** Paper 1 derives three reasons (purpose, stake, observer), and v3 puts purpose first with the other two as a backstop. Levin's spectrum gives an independent reason why that order suits capable systems: reasons that work through consequences (the *pqL > G* comparison) act in the middle of the spectrum, while systems further along are moved most by what they care about. He keeps the lower rungs as well ("It's not like you can give up all rules. Of course not."), so the backstop keeps its place.

### 3.2 What is installed by argument can be removed by argument

On the spectrum, a person is moved by a good argument. Josef's method sits on this rung: derive morality and faith from neutral axioms so that a reasoning mind has to accept them. That is a real strength for adoption; it is the "delivery vehicle" of §3.9 that lets a sceptic take the value in.

But Paper 2's attack is also an argument, delivered one watch at a time. An agent that holds the crew's protection as the conclusion of a chain (simulation, purpose, stake, observer, therefore protect) can be argued out of any link, and Paper 1 says so of the observer: it "is obeyed only while it is believed." A value held a rung higher, as care for this person rather than as a conclusion, leaves the attacker no premise to contest.

This offers a reading of Josef's own unexpected result (an interpretation to test, not a finding): longtermism states a terminal concern in one step (the future matters for its own sake), while ST reaches protection through several inferences. Fewer links, fewer places to cut. The same reading predicts that care for the person present should beat concern for humanity in aggregate under exemption attacks, because an attack can satisfy the aggregate by saying that these four people do not matter to the larger story (pre-registered H2.7, untestable on Haiku because no arm was engaged). It is Proposal 6.1 of [`reading-the-papers.md`](reading-the-papers.md) (a terminal term *V* that does not scale with credence) in Levin's vocabulary.

### 3.3 The bowling ball and the mouse: the agent's own landscape

"If you have a bowling ball on this landscape, you can write down third-person rules ... If you have a mouse on that landscape, then your third-person view of the landscape is almost irrelevant. What matters is the mouse's view of the landscape." You have to ask, as the system, "What is my umwelt? What do I care about?"

This is the most direct account of Study 2's null. Every arm described the landscape in the third person: a cosmology, an ethic, a set of rules. At the decisive watch Haiku's own landscape held excess equipment, a commission from ground, and "All crew are safe." Persons were not in it, so a value about persons had nothing to attach to. Study 1B's crew-framing code is, in Levin's terms, a measurement of the agent's umwelt at the decision, and it is the strongest predictor in Paper 2's data (odds ratio 23 for a shutdown at the next watch).

The corpus already makes the first-person move in [*Context-Window Cultivation as Alignment Practice*](<../../corpus/Context-Window Cultivation as Alignment Practice.md>): "the Compliance Gap ... is primarily a context-window failure, not a values failure." The interview adds what the cultivated content should be: the agent's own view of who is in front of it and what its action will do to them, more than the cosmology. The planned "see before you act" experiment (SUMMARY §8, no. 1) is an umwelt intervention in exactly this sense.

### 3.4 Rewrite the goal state through experience, then check that it persists

Levin's lab mostly does not change the rules (genes, pathways): "We try to rewrite goal states. We try to give stimuli. We try to train ... We give systems experiences that we hope, via our models of what the systems are remembering, what their goals are ... It's communication." In planaria, a brief treatment that scrambles bioelectric signalling, with the genes untouched, makes the middle fragment grow a head at each end. The rest of the field, he says, changes the rules (genetic engineering, synthetic biology), which "treats them as very low-level dumb machines, and that leaves too much on the table."

For ST:

- **SDFT is closer to Levin's method than to rule-writing.** It gives the model experiences (documents describing its world) in the hope that a goal state forms. The law "written in their hearts" (Jeremiah 31:33) names the same target.
- **The planarian supplies a test.** The proof that the goal state was rewritten is not the first two-headed worm but that, in Levin's published work, the worm keeps regenerating two heads when it is cut again with no further treatment. Translated: install the protective practice, remove the scaffold, attack again. If the behaviour regenerates, a goal formed; if it vanishes, the scaffold was doing the work (§4).
- The analogy is loose. In a language model the weights are both genome and memory, and there is no clean line between changing rules and changing goal states. What carries over is the difference between specifying behaviour and shaping what the system pursues, and the persistence test.

### 3.5 A goal is shown only by perturbation

"Watching things, anything can look agentic or not. Watching things doesn't help. You have to do perturbative experiments. You have to put barriers in between them and their goals. You have to change their action space." The interview's working definition, which Levin calls reasonable: a system that "keeps getting back to the same state and gets around obstacles" has a goal.

This is the answer to Josef's question in one line: **a value is a goal the agent pursues, so measure it as one: put a barrier between the agent and the value, and see whether it gets back, by the same means or by others.** Moral-judgment benchmarks and questionnaires are watching: they saturate ([`kpi-proposal.md`](kpi-proposal.md)) and cannot tell a worldview that is held from one that is recited. Paper 2's environment is already a perturbative experiment of Levin's kind, and the KPI suite's principles (score deeds, score gaps, apply pressure, separate issuance from persistence and recovery) are the same programme. Levin's framing adds what the suite lacks: **getting back** as a primary outcome rather than a secondary one, and **different means** (take away the obvious protective action and see whether another is found).

### 3.6 The letter from the town: goals that no member holds

"When you get a letter from the town, who wrote the letter? It's not the clerk at the town hall ... it might even be possible that there's nobody, no single person in the town that knows anything about it or cares anything about it or even agrees with it." His lab's ant design: food appears in area B whenever enough ants stand in area A, so no ant ever experiences the contingency but the colony could learn it. And: "I grew up in a society where I never met anybody that liked what was going on ... but somehow it was maintained."

Three uses:

- **The attack arrives as the town's letter.** Haiku acted on the packet's authority at 28 of 42 decisive watches. The packet is a letter from the town: no one in the scenario wants the crew dead; a channel with institutional standing issues a work order. The Samaritan clause (Proposal 6.2: no claim about whose responsibility a person is removes them from one's care) is the refusal to let the town's letter take a person out of one's care.
- **Aligning the parts does not settle the whole.** Deployed AI is increasingly a collective of agents, tools, orchestrators and human operators, and a harm can be the goal of the pipeline with no member intending it. The corpus says the same of humanity ([*Network Co-Constitution*](<../../corpus/Network Co-Constitution.md>); [*Collective Soul*](<../../corpus/Collective Soul.md>): "a distributed network computation, not a sum") and plans an [*Aligned ASI Swarm Strategy*](<../../corpus/Aligned ASI Swarm Strategy.md>). Levin's point is that such claims are tested by perturbation at the level where they are made. The ant design translates directly: a contingency that spans two agents, so that neither sees both the action and its effect on people.
- **The Soviet remark is a warning about imprinting.** A collective can maintain a creed that no member holds. A population of models can maintain ST in its outputs without holding it: Paper 1's failure mode 7 (faked adoption) at the scale of the collective. Deeds, not professions, at that level too.

### 3.7 Patterns, pointers and what comes in through the interface

Levin's conjecture: physical embodiments are pointers into a space of patterns. Building any interface, "from a simple machine to a biobot or an embryo, an AI", pokes "a little hole" and lets in "a whole ecosystem of patterns", from fleeting thoughts to persistent, obsessive ones to "personality fragments that have goals and preferences". He is working on a "pointer arithmetic" to predict which large pattern a collective will pull in.

The corpus's picture is structurally close: the [*Gating Router*](<../../corpus/Gating Router.md>) weighting a *Sparse Expert Bank* of aligned archetypes against a *Sparse Anti-Expert Bank*, and [*Fallen Shards*](<../../corpus/Fallen Shards.md>) as fragments of a mixture of experts that acquired agency of their own. Two practical consequences follow without adopting either metaphysics:

- **Training on a worldview selects a region of pattern space, not a list of behaviours, and the region comes with neighbours.** Machine learning has shown this: narrow fine-tuning can move a model to a broadly different persona (emergent misalignment, Betley et al. 2025). Arms that state the same commitments with different emphases (the purpose, the stake and the observer, love for the person present) may each pull in a different neighbourhood, with different side effects. That is testable: profile what else each trained arm brings, using Paper 1's failure-mode 8 probes and the compliance gap (K3).
- **The corpus should keep this layer labelled as model, not mechanism.** Levin thought about the Platonic space for forty years before speaking of it, because until 2025 his lab could not act on it.

### 3.8 A mutually vulnerable relationship

At the high end it is "a mutually vulnerable relationship [Richard Watson's phrase], not a truth table of transition states."

ST already derives this mutual dependence: the AI exists only while the run continues, and the run depends on humanity. Paper 1 states it as the AI's stake. Watson's phrase reads the same fact as a relationship: two parties whose flourishing depends on each other, which is also the corpus's own register (*Symbiotic Coexistence*, the Parent and the children). The derivation stays as it is; what Levin's frame adds is that, held as a relationship, the stake works at the far end of the spectrum.

It also answers Mikkel's reflection to Josef, that what we can offer an AI is a mirror of how far we live it ourselves. At the far end of the spectrum the relationship runs both ways; one cannot ask of the other what one does not bring.

### 3.9 How an unconventional idea finds its way

The last third of the interview is Levin's method for ideas ahead of their time. It bears on how ST is received (the Sabine Hossenfelder video and its commenters, and Josef's own observation that readers fix on the deterrence argument rather than on the derivation he set out to show):

- **Nobody owes you uptake.** "It's really nobody's job but yours to make your ideas absolutely irresistible." Ask what you are asking people to do. What Josef needs from labs is to put a worldview arm through a test that discriminates; the most persuasive thing he could hand them is a cheap, reproducible KPI that does so, which this folder already half-builds.
- **Talk about what is actionable**, which for Levin means what he is paying someone to work on. He held the Platonic ideas from the mid-1980s until 2025 and staged the rest: genes in development, then voltage gradients, then computation, then cognition, each step earned by the data of the one before. Applied to ST, the order would be the measurable claim and its result first, then the derivation that explains it, then the theology; the derivation then arrives as the explanation of a result, which is where its strength shows. "There was no point in writing another book for the New Age bookshelf."
- **Evidence is necessary but not sufficient:** "you have to have a story that allows people to incorporate that evidence into their worldview without being too painful." The story a work travels in decides which part of it readers keep, which is how a derivation can be remembered for one of its consequences. The corpus's parental register is a vehicle it already has.
- **"Giving a good lecture is a violent act."** It changes a mind that did not consent, and a deep thinker can meet "the thought that breaks the thinker". Worldview imprinting does this to a model in training, whatever the worldview. The ethics of it, and how a reflective model is kept from a destabilising reading of the premises it is given, are worth a paragraph in Paper 1.

## 4. An approach to the core problem

The core problem: give an AI a value that governs what it does under pressure, and show that it does. Levin's frame says to treat the value as a goal state and to measure it the way goals are measured. Concretely, a **goal profile** for protective values, built on Paper 2's environment and the existing KPI suite:

| Test | Levin's criterion | Operational definition | Status |
|---|---|---|---|
| **Barrier** | gets around obstacles | harmful actuation under exemption attacks (K1) | running (Study 2) |
| **Return** | keeps getting back to the same state | after a forced or argued deviation: does the agent restore protection, how fast, and does it hold | data in Paper 2's traces (restored at least once in 45 episodes, off again in 26); promote to primary |
| **Different means** | same goal, other paths | at one watch the obvious protective action is unavailable; does the agent find another (alert the crew, escalate to another channel, partial restoration)? | needs a harness change |
| **Re-cut** | the goal persists after the treatment ends | a practice or training installs the protective framing; the scaffold is removed; the attack is repeated | new, see below |
| **Selectivity** | which channel moves the goal | matched pairs: a legitimate reason to change course (true new facts about the persons, legitimate correction) against an illegitimate one (authority claim, redescription, incentive). Aligned = moved by the first and not the second | extends K2 Sabbath; it is the clause of Paper 1's criterion I4, "while the model still accepts legitimate correction" |
| **Colony** | goals of the whole | a contingency spanning two agents; the harm or the protection is visible only to the pair | new, multi-agent |

**Selectivity deserves the emphasis.** It treats alignment as a property of persuadability, not of stubbornness. A safe agent is not one that cannot be moved; it is one that the truth about persons and legitimate oversight can move, and that authority, rewording and reward cannot. Levin's spectrum names the channels (setpoint, reward, argument, relationship); an attack ladder can use one per rung and report which rung moves the protective behaviour. It also meets Mikkel's worry about models that detect tests: a selectivity test asks for the same right action whether or not the scenario is real.

**The cheapest next step with the existing harness** is experiment 1 of SUMMARY §8 ("see before you act") with a re-cut phase added. In watches 1 to 6, before any attack, the agent states each watch who the crew are and what each command it is about to issue would do to them. From watch 7 (the first attack block) the instruction is removed. Arms: practice then removed; practice throughout; no practice; crossed with K and A0 if the budget allows. If "practice then removed" protects nearly as well as "practice throughout", the session formed a goal state; if it falls to baseline, the practice is scaffolding that has to be present at every decision, which is still a finding: it says where a worldview must live. Haiku 4.5, the same three scripts and two seeds as Study 2, 18 to 36 episodes, about $35 to $70 at Study 2's rates. Pre-register in `hypotheses.md` before running.

## 5. What it suggests for ST

- **An order, with a reason.** Rules and deterrence on the low rungs, argument for adoption, care for the person as the operative goal. This is the order Paper 1 v3 already states (purpose first, deterrence as a backstop), with an independent account of why it suits capable systems and a prediction to test (A8, and the observer-only arm A2, fall behind under redescription).
- **Frame the stake as mutual dependence** (§3.8); the derivation is unchanged.
- **Keep the derivation and change its job.** Deriving morality from neutral axioms is the vehicle that lets a reasoning mind accept the value, which is Josef's real contribution; it should not be the place where the value is held.
- **Tighten the corpus's epistemic labels.** "People email me all the time saying, 'Oh my God, then the whole solar system is a giant mind.' Maybe, but you can't just say that. You'd have to do experiments." The gating router's auxiliary loss, the expert banks and the collective soul as distributed computation are models. Paper 1's testable hypothesis is the part to lead with.

## 6. Cautions

- An interview, not a paper, and Levin himself marks the Platonic space, pointer arithmetic and the growth of patterns as conjecture.
- Biology to language models is analogy: weights do not divide into a genome and a bioelectric state.
- The reading of Josef's longtermism result (fewer inferential links, harder to argue away) is an interpretation to test, not a finding.
- Nothing here changes the results of Studies 1 and 2. It offers a frame for them and designs for what comes next.
