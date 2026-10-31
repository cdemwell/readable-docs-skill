# Rewrite Moves

A catalogue of before/after pairs. Use it when a passage feels heavy but you cannot say why. The "why" column names the cost being removed.

## Nominalizations

Nouns made from verbs hide the action and add words. Turn them back into verbs.

| Before | After | Why |
|---|---|---|
| The implementation of the parser took two weeks. | We implemented the parser in two weeks. | Actor and action are explicit. |
| Conduct an evaluation of the proposal. | Evaluate the proposal. | One verb replaces a verb plus a nominalization. |
| The reduction of latency is a priority. | We need to reduce latency. | Names who needs it and what to do. |
| There was an improvement in throughput. | Throughput improved. | Removes the empty "there was." |
| The configuration of the service requires modification. | You must change the service configuration. | Two nominalizations become one plain verb. |
| Their agreement was that the migration should proceed. | They agreed to proceed with the migration. | Verb form is shorter and clearer. |

**Watch for:** words ending in *-tion, -sion, -ment, -ance, -ence, -ity, -ness, -ization*. One is fine. Three in a sentence is a warning.

## Denominal verbs

Nouns forced into verb slots make the reader infer the meaning.

| Before | After | Why |
|---|---|---|
| Calendar the review. | Put the review on the calendar. | Established noun plus plain verb. |
| Action the ticket. | Act on the ticket. | Removes the invented verb. |
| Leverage the existing data. | Use the existing data. | "Leverage" adds no meaning. |
| We need to socialize the plan. | We need to share the plan with the team. | Names the action and the audience. |
| Sunset the feature. | Retire the feature. | Common verb, same meaning. |
| Roadmap the migration. | Plan the migration. | Plain verb. |
| Onboarding a new engineer. | Helping a new engineer start. | Avoids the noun-as-verb. |

**Keep:** lexicalized verbs such as *email*, *ship*, *host*, *test*, *debug*. The cost applies to novel shifts, not established ones.

## Stacked nouns

Three or more nouns in a row force the reader to guess the relationship between each pair. Break the stack with a preposition or a verb.

| Before | After | Why |
|---|---|---|
| customer account deletion request workflow | the workflow for handling requests to delete customer accounts | Each relation is explicit. |
| data pipeline failure alert configuration | how to configure alerts when the data pipeline fails | Verb form removes the stack. |
| user permission escalation review process | the process for reviewing requests to escalate user permissions | Prepositions mark the relations. |
| production database backup retention policy | the policy for retaining production database backups | Two nouns remain, which is fine. |
| quarterly revenue forecast adjustment model | the model we use to adjust the quarterly revenue forecast | Relative clause breaks the chain. |

**Test:** insert "of" or "for" between each pair. If you cannot say which relation holds, the stack is ambiguous, not just dense.

## Relative clauses and reduced relatives

Object relatives are harder than subject relatives. Dropping "that" adds a garden path.

| Before | After | Why |
|---|---|---|
| The policy the board approved changed the process. | The policy that the board approved changed the process. | "That" blocks the wrong first parse. |
| The report the team wrote was late. | The report that the team wrote was late. | Same. |
| The service the client depends on failed. | The service that the client depends on failed. | Separates the embedded verb from the main verb. |
| A tool developers use to debug memory leaks. | A tool that developers use to debug memory leaks. | Prevents "use to" from reading as a unit. |

**When to split instead:** if adding "that" still leaves a long or ambiguous clause, use two sentences.

> The board approved a policy last year. That policy changed the process.

## Dependency length and word order

Keep the actor and the action close. Move heavy modifiers after the object.

| Before | After | Why |
|---|---|---|
| The team that had been reviewing the proposal for three weeks finally approved it. | After three weeks of review, the team approved the proposal. | Subject and verb are adjacent. |
| The engineer who joined in March and who owns the ingestion service fixed the bug. | The engineer who owns the ingestion service joined in March. They fixed the bug. | Splits two facts. |
| We rejected, after a long discussion about cost and risk and timing, the proposal. | After a long discussion about cost, risk, and timing, we rejected the proposal. | Object no longer stranded. |
| A config file with a list of hosts and a timeout value and a retry count is required. | The service needs a config file with a host list, a timeout, and a retry count. | Modifiers follow the noun. |

**Rule of thumb:** subject–verb within about seven words; verb–object within about seven. Count, then decide. Do not contort a sentence to hit the number.

## Inanimate subjects with animate verbs

Name the actor, or use a verb that genuinely takes an inanimate subject.

| Before | After | Why |
|---|---|---|
| The decision emerged from the meeting. | The team decided in the meeting. | Decisions do not emerge; people decide. |
| The data tells us to ship. | The data shows we should ship. | "Shows" is conventional for data. |
| The complaint becomes a fix. | The team fixed the bug that week. | Names the actor and the action. |
| The culture shifted toward ownership. | Managers began assigning owners to each service. | Replaces a metaphor with a behavior. |
| The market rewarded the launch. | Customers bought the product after launch. | Names who acted. |
| The policy wants to reduce churn. | The policy aims to reduce churn. | "Aims" does not require an agent. |

**Keep:** "the function returns," "the test fails," "the request times out," "the build broke." These are established technical usage, not coercion.

## Passive voice

Passive is not always wrong. Use active voice when the actor matters and is known. Use passive when the actor is unknown, irrelevant, or deliberately backgrounded.

| Before | After | Why |
|---|---|---|
| The config was changed by the deploy script. | The deploy script changed the config. | Actor is known and useful. |
| Mistakes were made. | We made three mistakes. | Names who and how many. |
| The decision was reached after review. | The committee decided after review. | Names the actor. |
| It is believed that the cache is stale. | We think the cache is stale. | Names who believes it. |
| The file is written to disk every minute. | The service writes the file to disk every minute. | Adds the missing actor. |

**Keep passive when:** the actor is unknown ("the packet was dropped"), obvious ("the suspect was arrested"), or unimportant ("the table is created on startup").

## Existential "there is / there are"

The construction is not inherently hard to read. It can reduce the distance between related words and place heavy new information at the end of the sentence. Rewrite it when it hides a specific actor or adds an empty frame.

| Before | After | Why |
|---|---|---|
| There is a configuration file that controls the retry count. | The configuration file controls the retry count. | Names the subject. |
| There were several errors found by the parser. | The parser found several errors. | Names the actor and removes the passive. |
| There is a need to update the schema. | We need to update the schema. | Names who needs it. |
| There is a risk that the migration fails. | The migration may fail. | Removes the empty frame. |
| There are three reasons to use a queue. | (Keep.) | Presentative enumeration; the number is the point. |
| There are two schemas: `core` and `mirror`. | (Keep.) | Introduces a list at the end of the sentence. |

**Keep it when:** it introduces new information, enumerates a list, or carries the end-weight of a long subject. **Rewrite it when:** it hides the actor, stacks a relative clause, or adds words without adding information.

## Weak verbs and light verb constructions

A light verb plus a noun often says the same thing as one verb, with more distance between the actor and the action. Prefer the verb when the meaning is unchanged.

| Before | After | Why |
|---|---|---|
| Make a decision. | Decide. | One verb. |
| Conduct an evaluation of the proposal. | Evaluate the proposal. | Removes the nominalization. |
| Perform an analysis of the logs. | Analyze the logs. | Direct. |
| Provide a description of the failure. | Describe the failure. | Direct. |
| Give consideration to the risk. | Consider the risk. | Direct. |
| Have a requirement for two workers. | Require two workers. | Direct. |
| Carry out the migration. | Migrate. | Direct. |

**Keep the light verb when** it carries a real distinction. "Take a decision" can imply a public or official act; "make a decision" can emphasize the process. In technical prose, the plain verb is usually the better default.

## Conditions before instructions

Put the condition first. The reader should know whether the instruction applies before they act on it.

| Before | After | Why |
|---|---|---|
| Click **Start** if you use Windows. | If you use Windows, click **Start**. | The condition is checked before the action. |
| Set `MAIL_LOG_JSON=1` when stderr is not a terminal. | When stderr is not a terminal, set `MAIL_LOG_JSON=1`. | Same. |
| Use `--volume` to reset the roles if the init scripts changed. | If the init scripts changed, use `--volume` to reset the roles. | The reason and the action stay together. |

## Filler and hedging

Cut words that add no information. Keep hedges that mark real uncertainty.

| Before | After | Why |
|---|---|---|
| It is important to note that the cache must be cleared. | Clear the cache. | The warning is the sentence. |
| In order to reduce latency, we added a cache. | To reduce latency, we added a cache. | Two words saved. |
| Due to the fact that the disk was full, writes failed. | Writes failed because the disk was full. | Plain conjunction. |
| We may potentially see some improvement. | Performance may improve. | One hedge, not three. |
| It should be noted that this approach has certain limitations. | This approach has three limitations. | Names the number. |
| At this point in time, the service is unavailable. | The service is down. | Plain words. |
| The team is currently in the process of migrating. | The team is migrating. | Removes the frame. |

**Keep hedges that carry meaning:** "may," "in some cases," "we have not tested this." Removing those turns a claim into an overclaim.

## Jargon and abstraction

Define necessary terms. Replace unnecessary ones.

| Before | After | Why |
|---|---|---|
| We need to operationalize the learnings. | We need to turn what we learned into a process. | Plain words. |
| The system exhibits degraded performance characteristics. | The system is slow. | Concrete adjective. |
| Utilize the cached artifact. | Use the cached file. | Common word, concrete noun. |
| There is a non-trivial probability of failure. | Failure is likely. | Removes the double negative. |
| We observed an anomalous latency distribution. | Latency was higher than usual. | Plain comparison. |
| The initiative has cross-functional dependencies. | The project needs work from two other teams. | Names the dependency. |

**Keep and define:** terms of art the audience needs ("idempotent," "quorum," "backpressure"). Define once, then use the term. Do not replace a precise term with a vague short one.

## Vague quantity and attribution

| Before | After | Why |
|---|---|---|
| A number of users reported the issue. | 42 users reported the issue. | A number is checkable. |
| Many teams depend on this service. | Six teams depend on this service. | Same. |
| Experts argue that the approach is risky. | The SRE team argues that the approach is risky. | Names the source. |
| Studies show that caching helps. | The 2024 load test showed a 40% drop in p99 latency. | Names the evidence. |
| Performance improved significantly. | p99 latency fell from 800 ms to 320 ms. | Shows the change. |

## Sentence splits and merges

Split when a sentence carries two ideas. Merge when two short sentences share a subject and the second depends on the first.

| Before | After | Why |
|---|---|---|
| The service retries failed requests, and it uses exponential backoff, and it adds jitter to avoid synchronized retries. | The service retries failed requests with exponential backoff and jitter. Jitter prevents clients from retrying in sync. | One idea per sentence. |
| The cache is full. The cache evicts the oldest entry. | When the cache is full, it evicts the oldest entry. | Merge removes repetition. |
| We deployed the fix. The outage ended. | We deployed the fix, and the outage ended. | Cause is explicit. |

**Do not** split a single idea into choppy fragments:

> The service retries. It uses backoff. The backoff is exponential. It adds jitter.

That is harder to read than one well-built sentence.

## Lists and prose

| Before | After | Why |
|---|---|---|
| We did three things: we reduced the timeout, we added a retry, and we monitored errors. | We made three changes: reduced the timeout, added a retry, and monitored errors. | Parallel shape. |
| The steps are: first open the file, then if the file is missing create it, then write the header. | 1. Open the file. 2. If it is missing, create it. 3. Write the header. | Steps become scannable. |
| Our values are speed, quality, and we care about users. | Our values are speed, quality, and user care. | Parallel grammar. |

## Paragraph flow

| Before | After | Why |
|---|---|---|
| The cache stores sessions. Redis is a key-value store. Sessions expire after a day. | The cache stores sessions in Redis, a key-value store. Each session expires after a day. | Links the facts into one topic. |
| Latency is high. We added a cache. It helped. | Latency was high, so we added a cache. Latency fell by half. | Connectives name the relations. |
| The migration is risky. We have a rollback plan. The plan is tested. | The migration is risky, but we have a tested rollback plan. | The contrast and the support arrive together. |

## Cohesion

The goal is to make the link between sentences explicit without explaining what the reader already knows. See [cohesion.md](cohesion.md) for the full audit.

| Before | After | Why |
|---|---|---|
| The scheduler applies jitter. A 200 ms window is used. This avoids synchronized retries. | The scheduler applies a 200 ms jitter window. The window prevents synchronized retries. | *This* had no clear referent. |
| The store writes the page and advances the cursor. It is atomic. | The write and the cursor commit in one transaction. | Names what is atomic. |
| The disk was full. Writes failed. | Writes failed because the disk was full. | The causal link is explicit. |
| The proxy path works for Gmail. The Graph path is unverified. | The proxy path works for Gmail, but the Graph path is unverified. | Marks the contrast. |
| The customer connects an account. The client authorizes the mailbox. The user starts ingestion. | The customer connects an account, then authorizes the mailbox and starts ingestion. | One actor, one term. |
| We use a queue. Also, we use a dead-letter queue. Moreover, we use a retry budget. | We use a queue, a dead-letter queue, and a retry budget. | Additive connectives add noise, not links. |

**Do not over-signal.** Add causal and contrastive links where the relation is real and non-obvious. Do not add *moreover* and *furthermore* to every sentence. Expert readers can handle gaps, and too much signposting makes them read less carefully.

## Headings

| Before | After |
|---|---|
| Background | Why the old retry logic failed |
| Implementation | Backoff formula and jitter range |
| Results | Latency fell 40% at p99 |
| Next steps | Ship in Q3 with a staged rollout |

## Openings and closings

| Before | After | Why |
|---|---|---|
| In this document, we will discuss the retry problem and several approaches. | Use exponential backoff with jitter. | State the point. |
| As we have seen, there are many considerations. | Choose backoff with jitter; the alternatives cost more. | Ends with a decision. |
| I hope this helps. Let me know if you have questions. | (Delete.) | The request is already stated. |

## When not to rewrite

Leave these alone:

- **Quotes and legal text.** Rewriting changes meaning or attribution.
- **Established technical terms.** "Idempotent" is shorter and more precise than "safe to repeat."
- **Deliberate ambiguity.** Sometimes the source genuinely does not know the answer. Say so; do not invent precision.
- **Code, commands, and identifiers.** Do not "fix" them.
- **A long sentence that is easy to follow.** Length is a proxy, not a defect. If the reader can hold the thread, keep it.
