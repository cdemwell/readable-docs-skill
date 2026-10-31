# Cohesion

Cohesion is the set of explicit links that let a reader connect one sentence to the next. Coherence is the reader's mental model. A text can be cohesive without being coherent, but weak cohesion makes coherence much harder to build.

Sentence-level clarity is not enough. A document of short, clear sentences can still be exhausting if the reader has to infer how each sentence relates to the last. Cohesion research measures this directly: referent overlap, causal links, connectives, and semantic similarity between sentences all predict comprehension, independent of sentence length.

## The audit

Run this after the paragraph pass and before the sentence pass. Read one paragraph at a time.

### 1. Referent check

Underline the subject of each sentence. Does it connect to something in the previous sentence, either by repeating a noun or by using an unambiguous pronoun?

**Break:** "The scheduler applies jitter. A 200 ms window is used. This avoids synchronized retries."

*This* has no clear referent. Name it: "The scheduler applies a 200 ms jitter window. The window prevents synchronized retries."

### 2. Pronoun check

Replace a pronoun with a noun when two possible referents exist, when the referent was more than one sentence ago, or when the pronoun is *this*, *it*, or *they* standing alone.

**Break:** "The store writes the page and advances the cursor. It is atomic."

What is atomic: the write, the cursor, or the pair? Say "The write and the cursor commit in one transaction."

### 3. Causal check

Mark every causal relation. If the relation is real and the reader might miss it, make it explicit with *because*, *so*, *therefore*, *as a result*, or a causal verb.

**Break:** "The disk was full. Writes failed."

**Better:** "Writes failed because the disk was full."

Do not add causal connectives where there is no cause. False causality is worse than a missing link.

### 4. Contrast check

If the reader might assume the opposite, mark the contrast with *but*, *however*, *although*, *whereas*, or *yet*.

**Break:** "The proxy path works for Gmail. The Graph path is unverified."

**Better:** "The proxy path works for Gmail, but the Graph path is unverified."

### 5. Lexical consistency check

Repeat the key term. Do not cycle through synonyms for the same concept.

**Break:** "The customer connects an account. The client then authorizes the mailbox. The user can start ingestion."

Are these three different entities or one? If one, pick one term and repeat it.

### 6. Paragraph bridge check

Read the last sentence of paragraph N and the first sentence of paragraph N+1. Does the second follow from the first, or does the reader have to invent the link?

If the link is missing, add a sentence or merge the paragraphs. If the paragraphs are unrelated, they belong in different sections.

### 7. Global topic check

Read the first sentence of each section. Do they form a summary of the document? If not, the section openings are not doing their job.

## What Coh-Metrix measures

Coh-Metrix is the standard computational toolkit for cohesion. Its most useful dimensions:

- **Referential cohesion.** Noun, argument, and stem overlap between adjacent sentences and across the whole text. Low overlap means the reader must infer what each sentence is about.
- **Causal cohesion.** The ratio of causal particles (*because*, *therefore*) to causal verbs. Low causal cohesion makes explanations feel like lists of facts.
- **Connectives.** Additive, temporal, causal, contrastive, and clarifying connectives. Density alone is not the goal; the type matters.
- **Semantic cohesion.** Latent semantic similarity between sentences. Adjacent sentences that share no meaning force a bridge.
- **Syntactic complexity.** Sentence and dependency structure, including the distance between related words.
- **Lexical diversity.** Variety of vocabulary. High diversity is not automatically good; repetition of key terms is a cohesion device.

## Do not over-explain

Cohesion is not the same as explaining everything. The research calls the counterweight the **reverse cohesion effect**:

- **Low-knowledge readers** benefit from high-cohesion text. They lack the background to fill gaps, so explicit links act as scaffolding.
- **High-knowledge readers** can benefit from lower-cohesion text, because the gaps force them to generate inferences. Over-signalling can make them read less carefully.
- **Skilled comprehenders** with high knowledge still benefit from high cohesion. The effect depends on both knowledge and skill.
- **Additive connectives** (*and*, *also*, *moreover*) can reduce comprehension when overused. **Causal and contrastive** connectives are the ones that reliably help, especially in difficult text.
- **Easy text** gains little from extra signalling. The relations are already obvious, and the markers become noise.

The practical rule: **match cohesion to the audience's knowledge.** Explain what the reader cannot infer. Do not explain what they already know. If background is needed, link to it or put it in an appendix rather than repeating it in every section.

## Rewrites

| Before | After | Why |
|---|---|---|
| The cache is full. The cache evicts the oldest entry. | When the cache is full, it evicts the oldest entry. | The relation is explicit and the repetition goes. |
| Latency was high. We added a cache. It helped. | Latency was high, so we added a cache. Latency fell by half. | Causal link and a concrete result. |
| The migration is risky. We have a rollback plan. The plan is tested. | The migration is risky, but we have a tested rollback plan. | Contrast and support arrive together. |
| The service retries. It uses backoff. The backoff is exponential. | The service retries with exponential backoff. | One idea, one sentence, no choppy fragments. |
| The customer connects an account. The client authorizes the mailbox. | The customer connects an account, then authorizes the mailbox. | One term for one actor. |

## Measurement

The checker reports a proxy:

- **Adjacent-sentence overlap.** The share of content-word stems two adjacent sentences have in common. Low overlap is a prompt to check for a missing bridge, not proof of a defect.
- **Cohesion gaps.** A sentence that shares no content word with any earlier sentence in its paragraph, and carries no pronoun that could link it. Review these; some are fine, especially at a topic change.
- **Connective counts.** Causal, contrastive, additive, and temporal. Look for an imbalance: many additive links and few causal ones often means the text lists facts without explaining them.

The proxy deliberately ignores bullet lists, because list items are parallel entries rather than prose. It cannot resolve pronouns, so a pronoun counts as a link. Treat the output as a reading list, not a score.

Do not optimize the number. A high overlap can mean healthy repetition or a paragraph that says the same thing twice.
