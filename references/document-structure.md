# Document Structure

Sentence-level edits are the last resort. Most unreadable documents are badly structured: the point is buried, sections mix topics, and nothing tells the reader where they are. Fix structure first, and many sentence problems disappear.

## Readers scan before they read

Assume the reader will:

1. Read the title.
2. Scan the headings.
3. Read the first paragraph.
4. Drop into whichever section looks relevant.

Design for that path. If the title and headings do not tell the story, the document fails before the first sentence.

## Set the contract

Write one sentence before you edit:

> After reading this, the reader should be able to **\_\_\_**.

If a section does not serve that sentence, cut it or move it to an appendix. This is also the test for whether the document needs a summary, a decision, or a tutorial.

## Put the answer first

State the conclusion in the first paragraph. Then support it. This is the inverted pyramid, and it works for reports, proposals, incident write-ups, and emails.

Bad:

> Over the last quarter we examined several approaches to the retry problem. We considered exponential backoff, fixed delays, and circuit breaking. Each has trade-offs. After discussion with the team, we recommend exponential backoff with jitter.

Good:

> Use exponential backoff with jitter for retries. It handles the thundering-herd case that fixed delays do not, and it needs no new infrastructure.

The second version lets a reader stop after one sentence. The first forces them to wait for the point.

## Headings are an outline

Headings do two jobs: they help readers find sections, and they function as signals that activate prior knowledge and improve comprehension. Research on signalling and headings consistently finds that they reduce extraneous load and improve readers' sense of how well they understand the text. Make them state content:

| Weak | Strong |
|---|---|
| Background | Why the old retry logic failed |
| Details | Backoff formula and jitter range |
| Considerations | Cost and operational risk |
| Conclusion | Ship it in Q3, with a staged rollout |

Read only the headings. If the sequence does not make an argument, rewrite the headings before rewriting prose.

## Chunk for entry

Assume a reader may land on any section from search. Do not assume they read the previous section of this document, or even the previous paragraph.

- Open with the section's claim and its context, not a transition from the previous section.
- Define terms the first time they appear in that section, or link to the definition.
- If the section genuinely needs context from another section, deep-link to the exact heading: `[the retry policy](operations.md#retry-policy)`. Say in one clause why the reader needs it. Never write "as we saw above" or "the previous section."
- Stay on one level. Do not jump between high-level rationale and low-level steps in the same section; link to the other level.
- Keep sections short enough to scan. If a section runs longer than a screen or two, look for a natural split.

Chunking reduces extraneous cognitive load: the reader spends less effort working out where they are and more on the content.

See [document-types.md](document-types.md) for the entry-point test and the type diagnostic.

## Paragraph architecture

A paragraph should do one job:

1. **Topic sentence** states the claim.
2. **Support** gives evidence, example, or mechanism.
3. **Close** draws the consequence, or hands off to the next paragraph.

The given-new contract: begin with information the reader already has, end with the new information. This is what makes prose feel like it flows. When a sentence starts with an unfamiliar term, the reader has nothing to attach it to.

Bad:

> A 200 ms jitter window is applied to each retry. The scheduler computes the window from the request ID. This avoids synchronized retries across clients.

Good:

> Each client applies a 200 ms jitter window to its retries. The scheduler derives the window from the request ID, so two clients rarely retry at the same moment. This avoids synchronized retries across clients.

The second version starts from the reader's existing model (clients retry), then adds the mechanism, then the consequence.

## Connectives

Name the relationship between sentences. Readers should not have to infer whether the next sentence is a cause, a contrast, or an example.

- Cause: because, so, therefore
- Contrast: but, however, unlike
- Consequence: as a result, which means
- Example: for example, in practice
- Sequence: first, then, finally

Connectives are cheap. Missing ones force inference, which is expensive. Do not stack them ("however, nevertheless, moreover") — one per link is enough.

## Lists

Use a list when:

- Items are parallel and order does not matter much (bullets), or
- Items are steps and order matters (numbers).

Do not use a list when items depend on each other. A list of causal steps hides the causal links. Write a paragraph instead.

Every list item should share a grammatical shape. If one item is a sentence and the next is a noun phrase, the reader has to reset.

## Repetition and terminology

Use one term for one concept, throughout. Synonym cycling — "customer," "client," "user," "account holder" for the same person — makes readers ask whether the distinctions are real. Repetition is a feature, not a flaw.

This is the opposite of the advice given to fiction writers. Technical documents are maps; consistent labels make the map readable.

## Formatting

In Markdown and rendered docs:

- **Bold** sparingly. If everything is bold, nothing is. Bold a term on first definition or a critical warning, not every noun phrase.
- **Code formatting** for identifiers, commands, and literal values.
- **Tables** for comparisons across consistent dimensions. Do not use a table for two paragraphs of prose.
- **Callouts** for warnings and prerequisites. Do not bury a prerequisite in a paragraph.
- **Link text** describes the destination. "See the retry design doc," not "click here."
- **No color-only or position-only instructions.** "Select the green button" fails for color-blind readers and screen readers.

## Document types

Choose the type before the order. See [document-types.md](document-types.md) for the diagnostic, the Diátaxis map, and the Good Docs Project templates. Start from the closest template and adapt it; do not copy its prose.

A document may mix types, but each section should have one job. Do not put reference detail in a tutorial, or tutorial steps in a reference page.

The orders below are common starting points.

### README

Order: what it is → why you would use it → install → minimal example → configuration → links. A reader should get a working example before the architecture discussion.

### Design doc

Order: problem → constraints → options considered → recommendation → risks → migration/test plan. Put the recommendation before the option-by-option analysis, so a reader who stops early still gets the decision.

### Report or analysis

Order: finding → evidence → method → limitations → recommendation. Do not make the reader reconstruct the finding from the data.

### Email

Order: request or decision → reason → deadline → context. One topic per email. If the reader skims only the first line, they should still know what you need.

### Incident write-up

Order: impact → timeline → root cause → fix → prevention. Separate what happened from what you think happened.

## Structure checklist

- [ ] Title says what the document is.
- [ ] The document has one type, or each section clearly declares its type.
- [ ] First paragraph states the point or the ask.
- [ ] Headings alone tell the story.
- [ ] Each section has one job and opens with its claim.
- [ ] Any section can be entered from search; its context is stated or deep-linked.
- [ ] Paragraphs are 3–6 sentences and start with a topic sentence.
- [ ] Each sentence connects to the previous one; connectives are explicit.
- [ ] One term per concept throughout.
- [ ] Lists contain parallel items, not reasoning.
- [ ] A reader can stop after any section and still have something useful.
