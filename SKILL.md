---
name: readable-docs
description: Make documents easier for people to read and understand. Use when writing, editing, or reviewing docs, READMEs, reports, design docs, proposals, emails, or any long-form prose where comprehension matters more than density.
license: MIT
metadata:
  version: 2.0
---

# Readable Docs

## The principle

Reading costs working memory. A document is easy to read when the reader can pursue a goal, predict what comes next, hold each dependency in mind, and connect each sentence to the one before it.

Difficulty is not the same as complexity. Complex ideas can be written clearly. Clear writing keeps the idea and removes the work of decoding it. Never delete necessary content to make text look simple.

## Reader goals come first

Every document exists for a reader goal. Name it before touching a sentence. The ISO plain-language standard reduces the goal to three verbs: the reader can **find**, **understand**, and **use** the information.

The goal determines the document type, the structure, and how much explanation the reader needs. A document that serves no goal is a container of facts. A document that serves two goals is usually two documents.

## What this skill is not

- **Not AI-detection evasion.** Do not sand off every pattern that looks machine-written. Fix what costs the reader, not what looks suspicious.
- **Not dumbing down.** Keep technical terms, precision, and nuance. A shorter word that loses a distinction is worse than a longer word that keeps it.
- **Not a grade-level target.** Readability formulas count syllables and sentence length, not understanding. See [references/evidence.md](references/evidence.md) for what each check actually predicts.
- **Not a style homogenizer.** Voice can stay. Comprehension comes first.
- **Not a license to rewrite everything.** Leave quotes, code, commands, legal text, and established technical terms alone. If the document is already clear, say so and stop.

## Two modes

**Drafting:** apply the rules while you write.
**Editing:** run the passes below on existing text. If the request is review-only, report findings and do not rewrite unless asked.

## Workflow

### 0. Set the contract

Ask or infer: who reads this, what must they find, understand, or do, and what can they skip? Write one sentence: "After reading this, the reader should be able to ___." If the document does not serve that sentence, fix the structure before touching sentences.

### 1. Choose the type and the template

Identify the document type: tutorial, how-to, reference, explanation, README, concept, troubleshooting, release notes, quickstart, installation guide, or glossary. Each type has a different reader goal and a different shape.

Then open the closest template from The Good Docs Project: <https://www.thegooddocsproject.dev/template>. Use its section order as a starting point. Adapt it to this document; do not copy its prose, and delete sections the reader does not need. If a document mixes types, split it or mark the mode change with a heading.

See [references/document-types.md](references/document-types.md) for the diagnostic and the template map.

### 2. Structural pass (highest leverage)

- **Put the conclusion first.** The first paragraph says what the document is, what it found, or what the reader should do.
- **Make the headings an outline.** Read only the headings. If they do not tell the story, rewrite them to state content, not topic labels. "Retry policy," not "Details."
- **One idea per section.** If a section has two jobs, split it.
- **Chunk for entry.** A reader should be able to start at any section and know where they are.
- **Do not assume the reader read the previous section.** Every section states its own context and defines terms at first use in that section. If context from elsewhere is genuinely required, deep-link to the exact heading (in this document or another) and say why. Never write "as we saw above."
- **Use lists for parallel items, not for reasoning.** If items depend on each other, use prose.
- **Concrete before abstract.** Give the case or example first, then the general rule.
- **Recommendation before justification.** Say what to do, then why.

See [references/document-structure.md](references/document-structure.md).

### 3. Paragraph pass

- **Topic sentence first.** The first sentence states the paragraph's claim.
- **One topic per paragraph.** Three to six sentences is a useful range, not a rule.
- **Follow given-new.** Start with what the reader already knows. End with the new thing.
- **Name the link.** If two paragraphs are not connected, the document is missing a step. Add the step or cut one paragraph.
- **Repeat the key term.** Synonym cycling makes readers wonder whether you mean the same thing.

### 4. Cohesion pass

Read one paragraph at a time and check the links between sentences:

1. **Referent:** does each sentence's subject connect to the previous sentence?
2. **Pronoun:** is every *it*, *this*, and *they* unambiguous?
3. **Causal:** are real cause-and-effect relations explicit?
4. **Contrast:** is an unexpected contrast marked with *but*, *however*, or *although*?
5. **Lexical consistency:** is the key term repeated instead of cycled through synonyms?
6. **Paragraph bridge:** does the first sentence of each paragraph follow from the last sentence of the previous one?
7. **Global topic:** do the section openings form a summary of the document?

Do not over-explain. Match cohesion to the audience's knowledge. Low-knowledge readers need explicit links; high-knowledge readers can benefit from gaps, and over-signalling can make them read less carefully. Causal and contrastive connectives help; additive connectives can hurt.

See [references/cohesion.md](references/cohesion.md).

### 5. Sentence pass

Target the six constructions that research links to processing cost:

| Cost | Looks like | Rewrite move |
|---|---|---|
| Long dependency | Subject and verb far apart; verb and object far apart | Put actor and action together; move modifiers after the object |
| Rare n-gram | Novel word pair; unusual collocation | Use the conventional phrase. "Evaluate," not "conduct an evaluation of" |
| Reduced object relative | "the report the team wrote" | Add "that," or split into two sentences |
| Stacked nouns | "customer account deletion request workflow" | Break with prepositions or a verb: "the workflow for deleting customer accounts" |
| Denominal verb | "calendar it," "action the ticket," "leverage the data" | Use the noun with a real verb: "put it on the calendar," "act on the ticket," "use the data" |
| Inanimate subject, animate verb | "the decision emerges," "the data tells us" | Name the actor, or use a plain copula: "the team decided," "the data shows" |

Rules of thumb:

- **Sentence length:** aim for 15–20 words on average. Treat 30 as a flag, not a hard cap. Vary length; a run of short sentences is its own kind of tiring.
- **Dependency distance:** keep subject and verb within about seven words, and verb and object within about seven. These are proxies, not laws.
- **Noun compounds:** break the stack when three nouns appear together. Two is usually fine.
- **One new concept per sentence.** If you need two, use two sentences.
- **Common word over rare word** when the meaning is the same.
- **Active voice when the actor matters.** Passive is fine when the actor is unknown or irrelevant. Do not contort a sentence to avoid "was."
- **Keep "that"** after verbs of thinking and saying, and in relative clauses, when its absence causes a garden path.
- **"There is / there are":** keep it when it introduces new information at the end of the sentence. Rewrite it when it hides a specific actor or adds an empty frame.
- **Weak verbs:** prefer the verb when the meaning is the same. "Make a decision" → "decide"; "conduct an evaluation" → "evaluate." Keep the light verb when it carries a real distinction of aspect or social meaning.
- **Conditions before instructions:** "If you use Windows, click **Start**," not "Click **Start** if you use Windows."
- **One instruction per sentence** in procedures. Procedural sentences should stay under 20 words; descriptive sentences under 25.

See [references/processing-costs.md](references/processing-costs.md), [references/rewrite-moves.md](references/rewrite-moves.md), and [references/evidence.md](references/evidence.md).

### 6. Word pass

- **Turn nominalizations back into verbs.** "The implementation of the parser" → "we implemented the parser."
- **Cut filler, hedges, and throat-clearing.** "It is important to note that" adds nothing. This is an economy edit, not a comprehension rule.
- **Define jargon and acronyms at first use.** Then use them consistently.
- **One term per concept** for the whole document.
- **Prefer concrete nouns and numbers** to abstractions. "Three retries" beats "a number of retries."

### 7. Verification

Do all eight. Do not skip the reader-goal test.

1. **Reader-goal test.** Can the intended reader find what they need, understand it, and act on it?
2. **Entry-point test.** Start at each section. Does it state its own context, or does it depend on a "previous section" the reader may never have seen? Where context is missing, is there a deep link to the exact place it lives?
3. **Cohesion test.** Read the last sentence of each paragraph and the first sentence of the next. Is the link obvious, or did you have to invent it?
4. **Reading test.** Read at speaking pace. Where you stumble, the reader stumbles.
5. **Prediction test.** Cover the next sentence. Can you guess its point? If not, the transition is missing.
6. **Who-does-what test.** For each sentence, find the actor and the action. If either is missing, rewrite.
7. **Meaning diff.** Compare against the original. Did you drop a qualifier, a number, a caveat, or a technical distinction? Restore it.
8. **Jargon audit.** List every term a non-specialist would not know. Define or remove each one.

When you can, test with real readers: give them a find/understand/use task and record where they hesitate. That is the test the standards actually require.

Optional: run `${CLAUDE_SKILL_DIR}/scripts/readability_check.py` before and after. It flags long sentences, noun stacks, nominalizations, filler, existential *there*, light verbs, and cohesion gaps. Treat flags as review prompts, not errors.

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/readability_check.py" document.md
python3 "${CLAUDE_SKILL_DIR}/scripts/readability_check.py" document.md --json
```

## Scoring

Rate 1–5. Revise anything below 4.

| Dimension | 1 | 5 |
|---|---|---|
| Structure | Reader cannot find the point | Headings alone tell the story |
| Entry | Sections depend on earlier ones | Any section works as an entry point |
| Cohesion | Sentences arrive unconnected | Each sentence follows from the last |
| Sentence load | Long dependencies in most sentences | Actor and action stay close |
| Word choice | Abstract, rare, nominalized | Concrete, common, consistent |
| Precision | Meaning was simplified away | Clear and still exact |

## References

- [references/evidence.md](references/evidence.md) — what each check actually predicts, with citations
- [references/document-types.md](references/document-types.md) — type diagnostic, Good Docs templates, entry points
- [references/document-structure.md](references/document-structure.md) — structure, signalling, cohesion, document types
- [references/cohesion.md](references/cohesion.md) — the cohesion audit and the over-explaining counterweight
- [references/processing-costs.md](references/processing-costs.md) — the research behind the sentence rules
- [references/rewrite-moves.md](references/rewrite-moves.md) — before/after catalogue

For AI stylistic tells (em dashes, tricolons, "not X but Y"), use the **stop-slop** skill. This skill targets comprehension; stop-slop targets voice.
