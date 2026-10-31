# Document Types and Templates

The reader's goal determines the shape of the document. Before editing a sentence, identify the type. A reference page that reads like a tutorial is hard to scan. A tutorial that reads like a reference is hard to follow.

## The diagnostic

Answer three questions:

1. **What is the reader trying to do?** Learn a skill, accomplish a task, look up a fact, or understand why something works.
2. **What do they already know?** A beginner needs a lesson and prerequisites. An expert needs a fact and a link.
3. **How will they arrive?** Top to bottom, or from search at one section?

The answers pick the type. If two answers conflict, split the document.

## The four core types (Diátaxis)

| Type | Reader question | Shape | Common failure |
|---|---|---|---|
| **Tutorial** | "Teach me to do this." | A lesson: one worked example, small steps, a result the reader can see. | Dumping reference material into the lesson. |
| **How-to** | "How do I do this?" | A recipe: prerequisites, numbered steps, expected result. Assumes basic competence. | Explaining theory instead of giving steps. |
| **Reference** | "What is this?" | Dry, complete, consistent entries: parameters, flags, fields, limits. | Mixing in advice, tutorials, or rationale. |
| **Explanation** | "Why is it like this?" | Discursive background: design decisions, trade-offs, history, mental models. | Turning into a procedure. |

The two axes are **action versus cognition** and **learning versus application**. A tutorial is action plus learning. A how-to is action plus application. Reference is cognition plus application. Explanation is cognition plus learning.

## Other common types

| Type | Reader goal | Shape |
|---|---|---|
| **README** | Decide whether to use the project, then start it. | What it is, why use it, install, minimal example, configuration, links. |
| **Concept** | Build a mental model. | Definition, why it exists, how it relates to other concepts, examples. |
| **Troubleshooting** | Get unstuck. | Symptom, likely cause, fix, prevention. |
| **Release notes** | Learn what changed. | New, changed, fixed, known issues, upgrade notes. |
| **API reference** | Call the thing correctly. | Endpoint or symbol, parameters, returns, errors, examples. |
| **Quickstart** | Reach first success fast. | One path, minimal prerequisites, a working result. |
| **Installation guide** | Get the software running. | Requirements, steps, verification, uninstall. |
| **Glossary** | Resolve a term. | Term, definition, aliases, related terms. |

## Start from a template

The Good Docs Project publishes community templates for these types: <https://www.thegooddocsproject.dev/template>. The core pack contains Concept, How-to, README, Reference, Release notes, Troubleshooting, and Tutorial. The miscellaneous templates include API getting started, API reference, Contact support, Glossary, Installation guide, Quickstart, SDK overview, Style guide, Terminology system, and User personas.

Use a template as a starting point, not a cage:

1. **Identify the type** with the diagnostic above.
2. **Open the matching template** and read its section order.
3. **Use the headings as a checklist** for what the reader expects.
4. **Keep what serves the goal.** Delete boilerplate and sections the reader does not need.
5. **Add project-specific sections** only when they serve the reader's goal.
6. **Check for mode mixing.** If a section changes type, split it or mark the change with a heading.

Do not copy a template's prose. Copy its structure and ask whether each section earns its place.

## Entry points and deep links

Documentation is read by foraging, not by marching from page one. A reader may land on any section from a search engine, a chat message, or a link in another document. Write every section as a possible entry point.

- **State the context in the first sentence.** Say what this section covers and what it assumes.
- **Define terms at first use in that section.** A term defined three sections ago is not defined here.
- **Do not write "as we saw above" or "the previous section."** The reader may not have seen it.
- **Deep-link when context is genuinely needed.** Link to the exact heading, not the document: `[the retry policy](operations.md#retry-policy)`. The same rule applies within one document: link to `#that-heading`, not "see above." State in one clause why the reader needs it.
- **Stay on one level.** Do not jump from a high-level rationale to a command in the same paragraph. Link to the other level instead.
- **Link richly and descriptively.** The link text says where it goes: "the migration sequence in `db_ops.md` §5," not "click here."

A section that cannot stand alone is a section that has not stated its context, or one that should be merged with the section it depends on.

## The type check

Before finishing, answer:

- [ ] What type is this document?
- [ ] Does every section serve that type?
- [ ] Can a reader landing on any section understand it without the previous one?
- [ ] Where context is missing, is there a deep link to the exact place it lives?
- [ ] Did I start from the closest template, and did I adapt rather than copy?
