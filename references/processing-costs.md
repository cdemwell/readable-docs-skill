# Processing Costs

The rules in this skill come from psycholinguistics, not taste. This file explains what each rule costs the reader and where the evidence comes from. Read it when you need to justify a rewrite or decide whether a construction is worth keeping.

## The model

Three costs account for most comprehension difficulty:

1. **Working memory.** A reader must hold an unfinished phrase in mind until it resolves. The longer the dependency, the more likely it decays or gets confused with something else. This is why dependency length matters.
2. **Prediction.** Readers predict the next word. A predictable word is cheap; an unexpected one triggers a spike in processing effort. This is surprisal, and it is why rare n-grams and novel collocations slow people down.
3. **Reanalysis.** When a sentence is ambiguous or violates an expectation, the reader builds one interpretation and has to rebuild it. Garden paths, reduced relatives, denominal verbs, and inanimate subjects with animate verbs all cause reanalysis.

These costs are additive within a sentence. One long dependency is fine. A long dependency inside a reduced relative with three stacked nouns is not.

## The evidence base

Clark, Martin, and Mahowald (2026) analyzed AI-generated text across chat, coding, and essays from nine frontier and near-frontier models. They compared it with human writing and with paraphrases produced by round-trip translation (English → Japanese → English), which normalizes meaning while removing model-specific style. Compared with human writing:

- All nine models used **more low-frequency n-grams** and **more inanimate subjects with animate verbs**.
- Most used **longer dependencies**, **more stacked nouns**, and **more reduced object relatives** in conversation.
- The authors argue the cause is a training pressure for **information density**, driven by optimization for math, code, and reasoning, rather than for successful communication.
- A proof-of-concept fine-tune with a length penalty produced a near-categorical preference for shorter syntactic alternatives, supporting the density hypothesis.

The finding is statistical. Models overuse these constructions; individual instances are not errors. Edit for density, not for the presence of a pattern.

## The six features

### Low-frequency n-grams and surprisal

**What it is.** Word combinations that rarely or never occur in ordinary text. Measured as unattested bigrams and trigram perplexity.

**Why it costs.** The reader cannot predict the phrase, so every word is a small surprise. Novel compounds and unusual verb–object pairings are especially expensive because the reader must infer the relationship rather than retrieve it.

**In practice.** "Conduct an evaluation of" instead of "evaluate." "Provide a mechanism for the mitigation of" instead of "reduce." "Utilize" instead of "use." Abstract nouns paired with generic verbs.

**Fix.** Use the conventional phrase. Prefer the verb form. If a phrase feels clever, check whether the plain version says the same thing.

**Caution.** Technical terms are often low-frequency by necessity. Keep them and define them. The target is gratuitous novelty, not precision.

### Dependency length

**What it is.** The linear distance between a syntactic head and its dependent — for example, between a subject and its verb, or a verb and its object.

**Why it costs.** The reader holds the first element in working memory until the second arrives. Longer spans mean more maintenance and more interference from intervening material. Dependency length minimization is a robust cross-linguistic tendency (Futrell et al., 2015).

**In practice.** "The team that had been reviewing the proposal for three weeks finally approved it." The subject and verb are nine words apart. "The proposal the committee had been discussing since March was rejected" hides the main clause behind a relative clause.

**Fix.** Put the actor and the action next to each other. Move modifiers after the object, or split the sentence. "The team approved the proposal after three weeks of review."

**Caution.** Some separation is unavoidable and useful. Heavy modifiers often belong after the noun. Do not produce "The team approved it after reviewing for three weeks the proposal" to satisfy a distance count.

### Reduced object relative clauses

**What it is.** A relative clause modifying an object, with the relativizer omitted: "the report **the team wrote**" rather than "the report **that** the team wrote."

**Why it costs.** Without "that," the reader initially parses the embedded noun as the object of the main verb, then has to reanalyze. Object relatives are harder than subject relatives even with the relativizer (Staub, 2010); removing it adds a garden path.

**In practice.** "The policy the board approved last year changed the process." On first read, "approved" can attach to "policy" in the wrong way.

**Fix.** Add "that," or split: "The board approved a policy last year. It changed the process."

**Caution.** Short, unambiguous reduced relatives are common in good prose ("the car I bought"). Fix them when the reader can misparse, not on sight.

### Stacked noun compounds

**What it is.** Three or more nouns in a modifier relationship: "customer account deletion request workflow."

**Why it costs.** The reader must infer the relation between each pair — is it a workflow for deleting accounts, or a request to delete an account? Processing novel compounds requires decomposition and inference; the first noun sets a context for the rest, and a long stack multiplies the possibilities (Lauer, 1995; Nakov & Hearst, 2005; Staub et al., 2007).

**In practice.** "Data pipeline failure alert configuration" and "user permission escalation review process."

**Fix.** Break the stack with a preposition or a verb: "the workflow for handling requests to delete customer accounts." Two nouns are usually fine. Three is a prompt to check.

**Caution.** Established terms such as "database connection pool" read as one unit. Do not break a term the audience knows.

### Denominal verbs

**What it is.** A noun used as a verb: "calendar it," "action the ticket," "leverage the data," "socialize the plan."

**Why it costs.** The verb is not in the reader's lexicon in that sense, so meaning must be inferred pragmatically from the noun (Clark & Clark, 1979; Thierry et al., 2008). That inference takes time and can fail.

**In practice.** "We'll sunset the feature and then roadmap the migration." Business and engineering writing is full of these.

**Fix.** Use the noun with a plain verb: "put it on the calendar," "act on the ticket," "use the data," "retire the feature," "plan the migration."

**Caution.** Some denominal verbs are fully lexicalized and cheap ("email me," "ship it," "host a service"). The cost applies to novel shifts, not established ones.

### Inanimate subjects with animate verbs

**What it is.** A non-human subject given a verb that normally requires a human agent: "the decision emerges," "the data tells us," "the policy wants to…", "the system believes…"

**Why it costs.** The reader's parser expects an animate agent for verbs like *decide*, *want*, and *tell*. Violating that expectation triggers reanalysis (Kuperberg, 2007). It also hides who actually acted.

**In practice.** "The complaint becomes a fix." "The culture shifted." "The market rewarded the move."

**Fix.** Name the actor: "The team fixed it that week." If there is no actor, use a plain copula or a state verb: "The data shows…" is acceptable because *show* takes an inanimate subject conventionally. The target is metaphor that hides agency, not every non-human subject.

**Caution.** Technical writing legitimately says "the function returns," "the test fails," "the request times out." These are established, not coercive. Do not rewrite them into "the developer sees the function return."

## The density hypothesis

The paper's explanation matters for editing strategy. Human language evolved under pressure to be *communicable*; LLMs are optimized for tasks where *density* wins. The result is prose that packs more information per word than a person can unpack at reading speed.

This means the fix is not "use simpler words" in isolation. It is to **spread the same information over more predictable structure**: more sentences, more explicit links, more repeated terms, more paragraph-level signposting. Do not delete content. Repackage it.

## Cohesion and over-explaining

The six features are sentence-level. Comprehension also depends on the links between sentences. Coh-Metrix measures referent overlap, causal cohesion, connective type, and semantic similarity between sentences; these predict comprehension independently of sentence length. See [cohesion.md](cohesion.md) for the audit.

The counterweight is the **reverse cohesion effect**. Low-knowledge readers need explicit links. High-knowledge readers can benefit from gaps, because filling them forces inference. Causal and contrastive connectives help; additive connectives and redundant signposting can hurt. Match cohesion to the audience's knowledge, and link to background instead of repeating it.

## Readability formulas

Flesch-Kincaid and similar scores count syllables and words per sentence. They do not measure conceptual complexity, cohesion, required inferences, or background knowledge (Klare, 1981; Begeny et al., 2014). Writing to a score often produces choppier, less coherent text. Use a formula only as a rough flag for sentence length, never as a target. [evidence.md](evidence.md) grades every common check, including the formula-based readability scores.

## References

- Begeny, J. C., et al. (2014). Can readability formulas be used to successfully gauge difficulty of reading materials? *Psychology in the Schools*.
- Chomsky, N. (1965). *Aspects of the Theory of Syntax*.
- Clark, E. V., & Clark, H. H. (1979). When nouns surface as verbs. *Language*.
- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). Why is AI-generated language so hard to understand? arXiv:2610.29162.
- Futrell, R., Mahowald, K., & Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37 languages. *PNAS*.
- Gibson, E. (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*.
- Grodner, D., & Gibson, E. (2005). Consequences of the serial nature of linguistic input. *Cognitive Science*.
- Hale, J. (2001). A probabilistic Earley parser as a psycholinguistic model. *NAACL*.
- Klare, G. R. (1981). Why readability formulas fail. *IEEE Transactions on Professional Communication*.
- Kuperberg, G. R. (2007). Neural mechanisms of language comprehension. *Brain Research*.
- Lauer, M. (1995). *Designing Statistical Language Learners: Experiments on Noun Compounds*.
- Levy, R. (2008). Expectation-based syntactic comprehension. *Cognition*.
- Nakov, P., & Hearst, M. (2005). Search engine statistics beyond the n-gram. *NAACL*.
- Smith, N. J., & Levy, R. (2013). The effect of word predictability on reading time is logarithmic. *Cognition*.
- Staub, A. (2010). Eye movements and processing difficulty in object relative clauses. *Cognition*.
- Staub, A., et al. (2007). The distributional structure of grammatical categories in speech to young children. *Cognitive Science*.
- Thierry, G., et al. (2008). Knowing what you can and cannot do with a word. *Cognition*.
