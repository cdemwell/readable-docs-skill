# readable-docs

An agent skill for making documents easier for people to read and understand.

`readable-docs` treats comprehension as a cognitive cost. A reader has limited working memory, predicts what comes next, and has to connect each sentence to the one before it. The skill gives an agent a repeatable editing workflow, a set of evidence-graded checks, and a small local checker that finds candidates for review.

This repository is the canonical source. The installed copy of the skill is a symlink to this directory, so future work belongs here.

## Why this exists

The starting point was Clark, Martin, and Mahowald (2026), [*Why is AI-generated language so hard to understand?*](https://arxiv.org/abs/2610.29162). They found that frontier models overuse constructions with known processing costs: rare n-grams, long dependencies, stacked nouns, reduced object relatives, denominal verbs, and inanimate subjects with animate verbs. Their explanation is that models are optimized for information density, not for successful communication.

That finding is useful, but it is not a style guide. The skill adds what the paper does not cover:

- **Reader goals.** A document exists for a reader who needs to find, understand, or use something.
- **Document types and templates.** A tutorial, a how-to, a reference page, and an explanation have different shapes.
- **Entry points.** A reader may arrive at any section from search. The skill does not assume they read the previous section.
- **Cohesion.** Short, clear sentences are not enough if the links between them are missing.
- **Evidence grades.** Some checks predict comprehension. Some predict reading speed or recall. Some are style preferences.

## What the skill does

The workflow runs in eight passes:

| Pass | Question it answers |
|---|---|
| 0. Contract | Who reads this, and what should they be able to do? |
| 1. Type and template | What kind of document is this, and what does its template require? |
| 2. Structure | Is the point first, and do the headings tell the story? |
| 3. Paragraphs | Does each paragraph make one claim and start with it? |
| 4. Cohesion | Does each sentence connect to the one before it? |
| 5. Sentences | Are the actor and action close, and are the constructions predictable? |
| 6. Words | Are the words concrete, common, consistent, and defined? |
| 7. Verification | Can a real reader find, understand, and use it? |

The sentence pass targets six constructions from the paper: long dependencies, rare n-grams, reduced object relatives, stacked nouns, denominal verbs, and inanimate subjects with animate verbs. It also covers existential *there*, weak verbs, conditions before instructions, and the 20/25-word limits used in Simplified Technical English for procedures.

The verification step has eight tests, including a reader-goal test, an entry-point test, a cohesion test, and a meaning diff. The optional ninth test is a real reader with a real task.

## Quick start

### Install as an agent skill

Clone or copy this repository, then link it into your agent's skills directory. From the repository root:

```sh
ln -s "$PWD" /path/to/skills/readable-docs
```

If the path is already a directory, move it aside first. The agent reads `SKILL.md` from the skill directory.

### Use it

Where the agent supports slash commands, invoke the skill directly:

```
/readable-docs
```

Or ask in plain language: "Make this document easier to read." The skill decides whether to draft or edit, then runs the appropriate passes.

### Run the checker

The checker is standard-library Python and has no dependencies.

```sh
python3 scripts/readability_check.py document.md
python3 scripts/readability_check.py document.md --json
cat document.md | python3 scripts/readability_check.py -
```

It reports sentence-length distribution, nominalizations, noun-stack candidates, passive-ish constructions, existential *there*, light verbs, filler, connective counts, and adjacent-sentence cohesion gaps. Every flag is a prompt to look, not a verdict. [The checker](#the-checker) explains why.

## Repository layout

```
.
├── SKILL.md                       # the skill entry point and workflow
├── references/
│   ├── evidence.md                # what each check actually predicts
│   ├── document-types.md          # type diagnostic, Good Docs templates, entry points
│   ├── document-structure.md      # structure, signalling, cohesion, formatting
│   ├── cohesion.md                # the cohesion audit and the over-explaining counterweight
│   ├── processing-costs.md        # the research behind the sentence rules
│   └── rewrite-moves.md           # before/after catalogue
├── scripts/
│   └── readability_check.py       # dependency-free candidate finder
├── LICENSE
└── README.md
```

`SKILL.md` stays short. The detail lives in `references/`, which the skill loads only when it needs them. This keeps the skill usable without burying the workflow in a long document.

## Design principles

### Reader goals come first

Every document serves a reader goal. The skill uses the ISO plain-language framing: the reader can find, understand, and use the information. A document that serves no goal is a container of facts. A document that serves two goals is usually two documents.

### Document type before prose

A reference page should be dry and scannable. A tutorial should teach through a worked example. A how-to should give steps and prerequisites. An explanation should give background and trade-offs. The skill diagnoses the type before editing.

### Templates are starting points

The skill points to [The Good Docs Project](https://www.thegooddocsproject.dev/template) and asks the agent to open the closest template. The template's section order is a checklist. Its prose is not a script. Adapt the template, delete sections the reader does not need, and split a document that mixes types.

### Entry points and deep links

Documentation is read by foraging. A reader may land on any section from search, a chat message, or a link. The skill therefore does not assume the reader saw the previous section. Each section states its own context and defines terms at first use.

When context from another section is genuinely required, link to the exact heading, in this document or another. "As we saw above" is banned. A deep link is more useful than a recap, and it does not pretend the reader was there.

### Cohesion is not sentence clarity

A document of short, clear sentences can still be exhausting if the reader has to infer how each sentence relates to the last. The cohesion pass checks referents, pronouns, causal links, contrast, lexical consistency, paragraph bridges, and global topic sentences.

The counterweight matters as much as the audit. The **reverse cohesion effect** shows that low-knowledge readers need explicit links, while high-knowledge readers can benefit from gaps that force inference. The skill says to match cohesion to the audience, not to maximize it. Add causal and contrastive links where the relation is real. Do not add *moreover* to every sentence.

### Evidence-graded checks

Not every common writing rule improves understanding. The skill grades them:

| Strength | Checks |
|---|---|
| Strong | Word frequency and surprisal, cohesion, dependency length, headings and signalling, background knowledge |
| Moderate | Passive voice, nominalizations, sentence length, noun compounds, connectives |
| Weak or stylistic | Existential *there*, weak verbs, filler, adverbs, sentence case, contractions |
| Triage only | Flesch-Kincaid, Gunning Fog, Coleman-Liau, SMOG, Automated Readability, Dale-Chall, Spache |

The full grading, with citations and caveats, is in [`references/evidence.md`](references/evidence.md).

### Preserve meaning

The skill never deletes necessary content to make text look simple. It keeps technical terms, qualifiers, numbers, and caveats. The meaning diff is a hard gate: a rewrite that lowers a score and loses a distinction is a regression.

### No external linters

The skill does not recommend or depend on external prose linters. Its checker is small, local, and transparent. It finds candidates. The agent and the reader decide.

## The checker

The checker is a proxy, not a comprehension test. It deliberately:

- skips code blocks, tables, and YAML frontmatter;
- skips bullet lists when measuring cohesion, because list items are parallel entries rather than prose;
- treats a pronoun as a link, because a lexical proxy cannot resolve it;
- reports connective counts without treating density as a target;
- refuses to produce a single "readability score."

The most useful signals are the sentence-length distribution, the long-sentence flags, the noun-stack candidates, and the cohesion gaps. The least useful are the raw counts of filler and adverbs, which are style preferences.

## Evidence and inspiration

### The paper that started it

- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). [Why is AI-generated language so hard to understand?](https://arxiv.org/abs/2610.29162) arXiv:2610.29162.

### Plain-language standards and accessibility

- [ISO 24495-1:2023 — Plain language: Governing principles and guidelines](https://www.iso.org/standard/78907.html).
- [WCAG 3.1.5 — Reading Level](https://www.w3.org/WAI/WCAG22/Understanding/reading-level).
- [WCAG technique G153 — Making text easier to read](https://w3c.github.io/wcag/techniques/general/G153).
- [Digital.gov plain language guide](https://digital.gov/guides/plain-language).

### Document architecture and templates

- [Diátaxis](https://diataxis.fr/) — tutorials, how-to guides, reference, and explanation.
- Mark Baker, [*Every Page is Page One*](https://everypageispageone.com/) — topic-based writing and information foraging.
- [The Good Docs Project templates](https://www.thegooddocsproject.dev/template).
- Robert Horn, [Information Mapping](https://informationmapping.com/pages/what-is-the-information-mapping-method) — information blocks, labels, chunking, and consistency.
- Barbara Minto, [The Pyramid Principle](https://www.barbaraminto.com/concept) — answer first, grouping, and logical order.

### Psycholinguistics and cohesion

- Graesser, McNamara, Louwerse, & Cai (2004). [Coh-Metrix: Analysis of text on cohesion and language](https://doi.org/10.3758/bf03195564). *Behavior Research Methods, Instruments, & Computers*.
- McNamara, Kintsch, Songer, & Kintsch (1996). Are good texts always better? *Cognition and Instruction*.
- O'Reilly & McNamara (2007). [Reversing the reverse cohesion effect](https://doi.org/10.1080/01638530709336895). *Discourse Processes*.
- Futrell, Mahowald, & Gibson (2015). [Large-scale evidence of dependency length minimization in 37 languages](https://doi.org/10.1073/pnas.1502134112). *PNAS*.
- Gibson (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*.
- Levy (2008). Expectation-based syntactic comprehension. *Cognition*.
- Staub (2010). Eye movements and processing difficulty in object relative clauses. *Cognition*.
- Paolazzi et al. (2019). [Passives are not hard to interpret but hard to remember](https://doi.org/10.1080/23273798.2019.1602733). *Language, Cognition and Neuroscience*.
- Kleijn, Pander Maat, & Sanders (2019). [Comprehension effects of connectives across texts, readers, and coherence relations](https://doi.org/10.1080/0163853X.2019.1605257). *Discourse Processes*.
- Isakson & Spyridakis. [Nominalizations: Effect on recall and comprehension](https://doi.org/10.1109/ipcc.1995.554908). IEEE IPCC.
- Bostian & Thering (1987). Scientists: Can they read what they write? *Journal of Technical Writing and Communication*.
- Limaye & Pompian (1991). [Brevity versus clarity: The comprehensibility of nominal compounds](https://doi.org/10.1177/002194369102800102). *Journal of Business Communication*.
- Clark & Clark (1979). When nouns surface as verbs. *Language*.
- Kuperberg (2007). Neural mechanisms of language comprehension. *Brain Research*.

### Controlled language

- [ASD-STE100 Simplified Technical English, Issue 9](https://asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) — 20-word procedural sentences, 25-word descriptive sentences, six sentences per paragraph, and one instruction per sentence.

### Style guides and courses

- [Google Technical Writing One](https://developers.google.com/tech-writing/one).
- [Google developer documentation style guide](https://developers.google.com/style/highlights).
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/developer-content/).

### Readability-formula critiques

- Klare (1981). [Why readability formulas fail](https://doi.org/10.1109/tpc.1981.6447826). *IEEE Transactions on Professional Communication*.
- Bruce, Rubin, & Starr (1981). Why readability formulas fail. *IEEE Transactions on Professional Communication*.
- Begeny et al. (2014). [Can readability formulas be used to successfully gauge difficulty of reading materials?](https://doi.org/10.1002/pits.21740) *Psychology in the Schools*.
- Crossley, Greenfield, & McNamara (2008). Assessing text readability using cognitively based indices. *TESOL Quarterly*.

Full citations and notes are in [`references/evidence.md`](references/evidence.md) and [`references/processing-costs.md`](references/processing-costs.md).

## Development

1. Edit `SKILL.md` for workflow changes. Move detail into `references/` so the entry point stays short.
2. Add new evidence to `references/evidence.md` with a citation and a verdict. Do not add a rule without saying how strong the evidence is.
3. Keep the checker dependency-free. Run `python3 -m py_compile scripts/readability_check.py` after changes.
4. Run the checker on the skill's own prose before committing:

   ```sh
   python3 scripts/readability_check.py SKILL.md
   python3 scripts/readability_check.py references/cohesion.md
   ```

5. Keep the installed skill a symlink to this repository. That way the skill and the source cannot drift.

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgements

This skill owes its shape to the researchers and writers listed above, and to the open documentation community around Diátaxis and The Good Docs Project. The idea that readability is a property of the reader's task, not only of the sentence, comes from the plain-language standards and from the cohesion research. The idea that a document should be tested with real readers comes from ISO 24495-1 and the plain-language movement.
