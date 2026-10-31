# What the Checks Actually Predict

Readability checkers offer many rules. Some map to comprehension. Some map to reading speed or recall. Some are editorial preferences with no measured effect on understanding. This file grades the checks so the skill uses them for the right job.

## The short version

- **Readability formulas are proxies for surface complexity, not measures of comprehension.** They count syllables, words, and sentence length. They ignore cohesion, required inferences, background knowledge, and structure. Use them to find candidates for review, never as targets.
- **The strongest levers are background knowledge, word frequency, cohesion, dependency length, and document structure.** These have direct evidence.
- **Style rules are not comprehension rules.** Passive voice, "there is," weak verbs, adverbs, and contractions are often worth changing for directness or voice. The evidence that they improve understanding is weak, mixed, or absent.
- **Tool output is a prompt to look, not a verdict.** The same is true of this skill's checker.

## The checks, graded

| Check | What it measures | Evidence | Verdict |
|---|---|---|---|
| Flesch-Kincaid, Gunning Fog, Coleman-Liau, SMOG, ARI, Dale-Chall, Spache | Syllables per word and words per sentence, combined into a grade level | Correlates with school grade level; weak and indirect as a predictor of comprehension. Ignores cohesion, inference, and background knowledge. Validated on school texts, not technical prose. | **Triage only.** Never a target. |
| Sentence length | Syntactic load | Shortening helps low-ability readers and reduces errors. High-ability readers gain little. Removing a connective to shorten a sentence can hurt comprehension. | **Flag long sentences; do not cap them.** |
| Word length / syllable count | Lexical difficulty proxy | Weak. Long words can be familiar; short words can be rare. | **Do not use alone.** |
| Word frequency / surprisal | Predictability of the next word | Strong and repeated: lower-frequency and less predictable words take longer to read. | **Prefer common words; define terms.** |
| Passive voice | Non-canonical argument order | Initial reading can be as fast or faster. Comprehension accuracy is lower, especially for who-did-what; working-memory load is higher; stative passives are harder than eventive ones. | **Use with judgment.** Keep passive when the actor is unknown or unimportant; prefer active when the actor matters. |
| "There is / there are" | Existential or presentative construction | Not inherently harder. It can reduce dependency distance and place heavy new information at the end. Proscription is a style preference, not a comprehension finding. L2 readers can confuse expletive and locative *there*. | **Flag only when it hides the actor or adds an empty frame.** |
| Weak verbs / light verbs ("make a decision," "conduct an evaluation") | Verb plus nominalization instead of a lexical verb | Little direct processing evidence. The constructions often carry aspect or social meaning. The shorter verb is usually clearer, not always more precise. | **Style preference.** Prefer the verb when the meaning is the same. |
| Nominalizations | Verbs or adjectives turned into nouns | Overall comprehension is often unaffected, but processing is slower, recall of central meaning is worse, and non-native readers struggle more. | **Flag clusters, not every *-tion*.** |
| Noun compounds (3+ nouns) | Stacked modifiers | Readers frequently misidentify the headword of a long compound. | **Flag stacks of three or more.** |
| Filler and adverbs | Word economy | No evidence that removing them improves comprehension. They can signal stance or emphasis. | **Style only.** Cut when empty. |
| Jargon | Background knowledge required | Background knowledge is the strongest single predictor of comprehension. A defined term is cheap; an undefined one is expensive. | **Define at first use; do not replace precision.** |
| Connectives | Explicit coherence relations | Causal and contrastive connectives help, especially in difficult text. Additive connectives can hurt. Over-signalling can hurt expert readers. | **Add causal and contrastive links; avoid blanket additive signposting.** |
| Cohesion (referent overlap, causal links, semantic similarity) | Discourse integration | Strong for low-knowledge readers. High-knowledge readers can benefit from gaps (the reverse cohesion effect). Skilled comprehenders benefit from cohesion. | **Audit and match to the audience.** |
| Headings and signalling | Structure | Strong: headings improve comprehension, recall, and metacognitive accuracy. | **Use.** |
| Lists and tables | Scanning and comparison | Moderate: structure helps retrieval and comparison when items are parallel. Lists of reasoning hide relations. | **Use for parallel items, not arguments.** |
| Examples and concrete cases | Integration and transfer | Concrete examples aid memory and application, especially for abstract material. | **Use before the abstraction.** |
| Background knowledge | The reader's prior model | The strongest predictor. No sentence edit compensates for a missing prerequisite. | **State prerequisites; link background.** |

## Why formulas fail as targets

Readability formulas are **index-based**, not causal. They were validated by correlating text features with grade-level placements, not by showing that changing those features causes comprehension to improve. A text can score at grade 8 and be incomprehensible because it assumes knowledge the reader lacks. A text can score at grade 12 and be easy for its intended expert audience.

The features formulas ignore are the ones that matter most:

- cohesion between sentences;
- the number and difficulty of required inferences;
- the reader's background knowledge;
- rhetorical structure and signposting;
- concreteness and examples;
- whether the reader can find what they need.

There is also a measurement problem. Formula scores vary across metrics for the same text. SMOG is calibrated for health writing. Sentence-level scoring is noisy: applying several formulas to one sentence and flagging it when enough agree lets a single long technical word dominate. Document-level scoring hides variation between sections. No formula measures cohesion or inference. All of them are candidate finders.

## What this means for the skill

1. **Use the checker for triage.** It flags long sentences, noun stacks, nominalizations, filler, and now cohesion gaps and light verbs. Review the flags; do not chase the count.
2. **Use the evidence grades.** When a check is style-only, say so. Do not present a preference as a comprehension rule.
3. **Prefer the strong levers.** Fix structure, cohesion, word frequency, dependency length, and background knowledge before polishing adverbs.
4. **Keep the meaning diff.** Simplification research consistently finds an adequacy-simplicity trade-off. A rewrite that lowers a score and loses a qualifier is a regression.

## Sources

- Begeny, J. C., et al. (2014). Can readability formulas be used to successfully gauge difficulty of reading materials? *Psychology in the Schools*.
- Bostian, L. R., & Thering, A. (1987). Scientists: Can they read what they write? *Journal of Technical Writing and Communication*.
- Bruce, B., Rubin, A., & Starr, K. (1981). Why readability formulas fail. *IEEE Transactions on Professional Communication*.
- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). Why is AI-generated language so hard to understand? arXiv:2610.29162.
- Crossley, S. A., Greenfield, J., & McNamara, D. S. (2008). Assessing text readability using cognitively based indices. *TESOL Quarterly*.
- Gledhill, C. (2014). The grammar of "make a decision" and "take a decision." Corpus and Systemic Functional Grammar.
- Graesser, A. C., McNamara, D. S., & Kulikowich, J. M. (2011). Coh-Metrix: Providing multilevel analyses of text characteristics. *Educational Researcher*.
- Isakson, C. S., & Spyridakis, J. H. (2002). Nominalizations: Effect on recall and comprehension. *IEEE International Professional Communication Conference*.
- Kleijn, S., Pander Maat, H., & Sanders, T. (2019). Comprehension effects of connectives across texts, readers, and coherence relations. *Discourse Processes*.
- Klare, G. R. (1981). Why readability formulas fail. *IEEE Transactions on Professional Communication*.
- Limaye, M. R., & Pompian, R. (1991). Brevity versus clarity: The comprehensibility of nominal compounds in business and technical prose. *Journal of Business Communication*.
- McNamara, D. S., et al. (1996). Are good texts always better? Text coherence, background knowledge, and levels of understanding. *Cognition and Instruction*.
- O'Reilly, T., & McNamara, D. S. (2007). Reversing the reverse cohesion effect. *Discourse Processes*.
- Paolazzi, C. L., et al. (2019). Passives are not hard to interpret but hard to remember. *Language, Cognition and Neuroscience*.
- Smith, N. J., & Levy, R. (2013). The effect of word predictability on reading time is logarithmic. *Cognition*.
- Spyridakis, J. H., & Isakson, C. S. (1998). Nominalizations vs. denominalizations: Do they influence what readers recall? *Journal of Technical Writing and Communication*.
