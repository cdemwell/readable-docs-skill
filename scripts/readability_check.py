#!/usr/bin/env python3
"""Heuristic readability check for prose documents.

Flags likely sources of processing cost: long sentences, nominalizations,
noun stacks, front-loaded clauses, filler, and heavy punctuation.

These are proxies, not verdicts. Review the flags; do not optimize for the
numbers. Readability formulas that count syllables do not measure
comprehension, and neither does this script.

Usage:
    python3 readability_check.py document.md
    python3 readability_check.py document.md --json
    cat document.md | python3 readability_check.py -
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Word lists
# --------------------------------------------------------------------------

STOPWORDS = {
    # determiners and pronouns
    "a", "an", "the", "this", "that", "these", "those", "my", "your", "his",
    "her", "its", "our", "their", "some", "any", "each", "every", "no",
    "another", "such", "what", "which", "who", "whom", "whose", "i", "you",
    "he", "she", "it", "we", "they", "me", "him", "us", "them",
    # quantifiers and degree words
    "all", "more", "most", "many", "much", "few", "several", "both", "either",
    "neither", "other", "same", "only", "even", "still", "never", "always",
    "often", "usually", "sometimes", "generally", "typically", "particularly",
    "especially", "roughly", "nearly", "almost", "less", "least", "very",
    "quite", "rather", "somewhat", "just", "simply", "clearly", "obviously",
    # prepositions
    "of", "in", "on", "at", "to", "for", "with", "without", "from", "by",
    "about", "into", "through", "during", "before", "after", "above",
    "below", "between", "among", "under", "over", "across", "against",
    "along", "around", "behind", "beyond", "near", "per", "via", "upon",
    # conjunctions
    "and", "or", "but", "nor", "so", "yet", "because", "although", "though",
    "while", "whereas", "if", "unless", "since", "until", "when", "where",
    "whether", "than", "as",
    # auxiliaries and common verbs
    "is", "are", "was", "were", "be", "been", "being", "am", "do", "does",
    "did", "done", "have", "has", "had", "having", "can", "could", "will",
    "would", "shall", "should", "may", "might", "must", "not", "also",
    "use", "uses", "used", "using", "make", "makes", "made", "making",
    "get", "gets", "got", "getting", "set", "sets", "setting", "run", "runs",
    "running", "build", "builds", "built", "write", "writes", "wrote",
    "read", "reads", "send", "sends", "sent", "add", "adds", "added",
    "remove", "removes", "removed", "create", "creates", "created",
    "delete", "deletes", "deleted", "update", "updates", "updated",
    "change", "changes", "changed", "start", "starts", "started", "stop",
    "stops", "stopped", "open", "opens", "opened", "close", "closes",
    "closed", "check", "checks", "checked", "find", "finds", "found",
    "show", "shows", "showed", "shown", "give", "gives", "gave", "given",
    "take", "takes", "took", "taken", "put", "puts", "keep", "keeps",
    "kept", "hold", "holds", "held", "call", "calls", "called", "return",
    "returns", "returned", "fail", "fails", "failed", "pass", "passes",
    "passed", "work", "works", "worked", "need", "needs", "needed", "want",
    "wants", "wanted", "help", "helps", "helped", "allow", "allows",
    "allowed", "require", "requires", "required", "support", "supports",
    "supported", "include", "includes", "included", "provide", "provides",
    "provided",
    # common verbs that otherwise look like nouns in a run
    "mean", "means", "meant", "cause", "causes", "caused", "causing",
    "supporting", "produce", "produces", "produced", "producing",
    "trigger", "triggers", "triggered", "triggering", "measure", "measures",
    "measured", "measuring", "drive", "drives", "drove", "driven", "driving",
    "reduce", "reduces", "reduced", "reducing", "increase", "increases",
    "increased", "increasing", "avoid", "avoids", "avoided", "avoiding",
    "prevent", "prevents", "prevented", "preventing",
    "apply", "applies", "applied", "applying",
}

# Cohesion needs content words, including verbs. Using STOPWORDS here would
# discard the very words that carry a sentence's topic.
COHESION_STOPWORDS = {
    "a", "an", "the", "this", "that", "these", "those", "my", "your", "his",
    "her", "its", "our", "their", "i", "you", "he", "she", "it", "we",
    "they", "me", "him", "us", "them",
    "of", "in", "on", "at", "to", "for", "with", "without", "from", "by",
    "about", "into", "through", "during", "before", "after", "above",
    "below", "between", "among", "under", "over", "across", "against",
    "along", "around", "behind", "beyond", "near", "per", "via", "upon",
    "and", "or", "but", "nor", "so", "yet", "because", "although", "though",
    "while", "whereas", "if", "unless", "since", "until", "when", "where",
    "whether", "than", "as",
    "is", "are", "was", "were", "be", "been", "being", "am", "do", "does",
    "did", "done", "have", "has", "had", "having", "can", "could", "will",
    "would", "shall", "should", "may", "might", "must", "not", "also",
    "there", "then", "more", "most", "much", "many", "some", "any", "each",
    "every", "no", "all", "both", "either", "neither", "other", "same",
    "such", "only", "even", "still", "very", "quite", "rather", "just",
    "simply", "clearly", "obviously", "nearly", "almost", "less", "least",
    "few", "several", "own", "one", "two", "three", "first", "second",
    "third",
}

ADJECTIVE_SUFFIXES = (
    "ous", "ful", "ive", "able", "ible", "less", "ish", "ary", "ent", "ant",
    "al", "ic", "ical",
)

NOUN_SUFFIXES = (
    "tion", "sion", "ment", "ance", "ence", "ity", "ness", "ism", "ship",
    "hood", "age", "ery", "ure", "ing", "er", "or", "ist", "ics", "ology",
    "sis",
)

NOMINALIZATION_RE = re.compile(
    r"\b[a-z]{5,}(?:tion|sion|ment|ance|ence|ity|ness|ism|ization|isation)\b",
    re.IGNORECASE,
)

FILLER_PHRASES = [
    "it is important to note",
    "it should be noted",
    "it is worth noting",
    "it is interesting to note",
    "needless to say",
    "in order to",
    "due to the fact that",
    "in terms of",
    "with regard to",
    "with respect to",
    "in the process of",
    "at this point in time",
    "at the present time",
    "for the purpose of",
    "in the event that",
    "in light of the fact that",
    "the fact that",
    "a number of",
    "a variety of",
    "a range of",
    "in some cases",
    "to some extent",
    "as a matter of fact",
    "it goes without saying",
    "basically",
    "actually",
    "really",
    "very",
    "quite",
    "rather",
    "somewhat",
    "simply",
    "just",
    "clearly",
    "obviously",
    "of course",
    "in fact",
    "indeed",
    "essentially",
    "fundamentally",
    "ultimately",
]

HEDGES = [
    "may potentially",
    "might possibly",
    "could perhaps",
    "it seems that",
    "it appears that",
    "there is a possibility",
    "to a certain degree",
]

ALWAYS_PROTECT = {
    "mr.", "mrs.", "ms.", "dr.", "prof.", "inc.", "ltd.", "u.s.", "u.k.",
}
CONTEXT_PROTECT = {
    "e.g.", "i.e.", "etc.", "vs.", "fig.", "no.", "approx.", "al.", "cf.",
}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")
PASSIVE_RE = re.compile(
    r"\b(?:is|are|was|were|be|been|being|get|gets|got|gotten)\s+"
    r"(?:\w+ly\s+)?(\w+(?:ed|en))\b",
    re.IGNORECASE,
)

EXISTENTIAL_RE = re.compile(
    r"\bthere\s+(?:is|are|was|were|has been|have been)\b",
    re.IGNORECASE,
)

LIGHT_VERB_RE = re.compile(
    r"\b(?:make|makes|made|making|take|takes|took|taking|"
    r"give|gives|gave|giving|have|has|had|having|"
    r"do|does|did|doing|conduct|conducts|conducted|conducting|"
    r"perform|performs|performed|performing|"
    r"provide|provides|provided|providing|"
    r"carry out|carries out|carried out|carrying out)\s+"
    r"(?:a|an|the)?\s*([a-z]+(?:tion|sion|ment|ance|ence|ity|ness))\b",
    re.IGNORECASE,
)

CONNECTIVE_LISTS = {
    "causal": [
        "because", "since", "therefore", "thus", "consequently", "hence",
        "as a result", "due to", "owing to",
    ],
    "contrast": [
        "but", "however", "although", "though", "whereas", "yet", "still",
        "nevertheless", "nonetheless", "in contrast", "on the other hand",
    ],
    "additive": [
        "also", "moreover", "furthermore", "additionally", "in addition",
        "besides",
    ],
    "temporal": [
        "then", "next", "after", "before", "while", "when", "once",
        "finally", "first", "second", "third",
    ],
}

CONNECTIVE_PATTERNS = {
    name: re.compile(
        r"\b(?:" + "|".join(re.escape(item) for item in items) + r")\b",
        re.IGNORECASE,
    )
    for name, items in CONNECTIVE_LISTS.items()
}

PRONOUN_RE = re.compile(
    r"\b(?:it|its|this|these|those|they|them|their|he|him|his|she|her)\b",
    re.IGNORECASE,
)

STEM_SUFFIXES = (
    "ization", "isation", "ations", "ation", "ments", "ment",
    "ances", "ance", "ences", "ence", "ities", "ity", "nesses", "ness",
    "ings", "ing", "ers", "er", "ed", "es", "s",
)


def stem(word: str) -> str:
    """Crude stemmer for cohesion overlap. Good enough for a review prompt."""
    lowered = word.lower()
    for suffix in STEM_SUFFIXES:
        if len(lowered) > len(suffix) + 3 and lowered.endswith(suffix):
            return lowered[: -len(suffix)]
    return lowered


def content_stems(sentence: str) -> set[str]:
    return {
        stem(word)
        for word in WORD_RE.findall(sentence)
        if word.lower() not in COHESION_STOPWORDS and len(word) >= 3
    }


def phrase_patterns(phrases: list[str]) -> list[tuple[str, re.Pattern[str]]]:
    return [
        (phrase, re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE))
        for phrase in phrases
    ]


FILLER_PATTERNS = phrase_patterns(FILLER_PHRASES)
HEDGE_PATTERNS = phrase_patterns(HEDGES)


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

@dataclass
class Paragraph:
    text: str
    offsets: list[tuple[int, int]]  # (char offset in text, source line number)
    line: int
    is_list_item: bool = False

    def line_for(self, pos: int) -> int:
        line = self.line
        for start, source_line in self.offsets:
            if start <= pos:
                line = source_line
            else:
                break
        return line


@dataclass
class Document:
    paragraphs: list[Paragraph] = field(default_factory=list)
    headings: list[tuple[int, str]] = field(default_factory=list)
    code_blocks: int = 0
    lines_skipped: int = 0

    @property
    def text(self) -> str:
        return "\n\n".join(p.text for p in self.paragraphs)

    @property
    def sentences(self) -> list[tuple[str, int]]:
        result: list[tuple[str, int]] = []
        for paragraph in self.paragraphs:
            for sentence, start in split_sentences(paragraph.text):
                result.append((sentence, paragraph.line_for(start)))
        return result


def clean_markdown(line: str) -> str:
    line = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", line)
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"<[^>]+>", " ", line)
    line = re.sub(r"https?://\S+", " ", line)
    line = re.sub(r"[*_~]{1,3}", "", line)
    line = re.sub(r"^\s*#{1,6}\s*", "", line)
    line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
    line = re.sub(r"^\s*>\s?", "", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def parse_document(source: str) -> Document:
    doc = Document()
    lines = source.splitlines()
    has_frontmatter = bool(
        lines
        and lines[0].strip() == "---"
        and any(line.strip() == "---" for line in lines[1:40])
    )
    in_code = False
    in_frontmatter = has_frontmatter
    in_comment = False
    buffer: list[tuple[int, str]] = []
    buffer_is_list = False

    def flush() -> None:
        nonlocal buffer, buffer_is_list
        if not buffer:
            buffer_is_list = False
            return
        text_parts: list[str] = []
        offsets: list[tuple[int, int]] = []
        cursor = 0
        for line_no, cleaned in buffer:
            if not cleaned:
                continue
            if text_parts:
                text_parts.append(" ")
                cursor += 1
            offsets.append((cursor, line_no))
            text_parts.append(cleaned)
            cursor += len(cleaned)
        text = "".join(text_parts)
        if text.strip():
            doc.paragraphs.append(
                Paragraph(
                    text=text,
                    offsets=offsets,
                    line=buffer[0][0],
                    is_list_item=buffer_is_list,
                )
            )
        buffer = []
        buffer_is_list = False

    for index, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if index == 1 and in_frontmatter:
            in_frontmatter = True
            doc.lines_skipped += 1
            continue
        if in_frontmatter:
            doc.lines_skipped += 1
            if stripped == "---":
                in_frontmatter = False
            continue

        if stripped.startswith("```") or stripped.startswith("~~~"):
            flush()
            in_code = not in_code
            if in_code:
                doc.code_blocks += 1
            doc.lines_skipped += 1
            continue
        if in_code:
            doc.lines_skipped += 1
            continue

        if "<!--" in raw:
            in_comment = True
        if in_comment:
            doc.lines_skipped += 1
            if "-->" in raw:
                in_comment = False
            continue

        if not stripped:
            flush()
            continue

        if stripped.startswith("|"):
            flush()
            doc.lines_skipped += 1
            continue

        if re.match(r"^#{1,6}\s", stripped):
            flush()
            heading = clean_markdown(stripped)
            if heading:
                doc.headings.append((index, heading))
            continue

        if stripped.startswith("    "):
            flush()
            doc.lines_skipped += 1
            continue

        is_list_line = bool(
            re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", raw)
        )
        if is_list_line:
            flush()

        cleaned = clean_markdown(raw)
        if cleaned:
            if not buffer:
                buffer_is_list = is_list_line
            buffer.append((index, cleaned))

    flush()
    return doc


def split_sentences(
    text: str, min_words: int = 3
) -> list[tuple[str, int]]:
    protected = text
    for abbreviation in ALWAYS_PROTECT:
        protected = re.sub(
            r"\b" + re.escape(abbreviation),
            lambda match: match.group(0).replace(".", "§"),
            protected,
            flags=re.IGNORECASE,
        )
    for abbreviation in CONTEXT_PROTECT:
        # Protect only when the abbreviation is internal to a sentence.
        # The lookahead is case-sensitive: "etc. The" ends a sentence,
        # while "etc. the" does not. The leading boundary keeps "ms." from
        # matching the end of an ordinary word such as "streams."
        pattern = (
            r"\b(?i:" + re.escape(abbreviation) + r")(?=\s*[a-z0-9,;:)])"
        )
        protected = re.sub(
            pattern,
            lambda match: match.group(0).replace(".", "§"),
            protected,
        )
    protected = re.sub(r"(\d)\.(\d)", r"\1§\2", protected)

    boundaries = [
        match.end()
        for match in re.finditer(r"[.!?]+[\"')”’]*(?=\s|$)", protected)
    ]

    sentences: list[tuple[str, int]] = []
    start = 0
    for end in boundaries + [len(protected)]:
        chunk = protected[start:end].strip()
        if chunk:
            sentence = chunk.replace("§", ".")
            if len(WORD_RE.findall(sentence)) >= min_words:
                sentences.append((sentence, start))
        start = end
        while start < len(protected) and protected[start].isspace():
            start += 1
    return sentences


# --------------------------------------------------------------------------
# Analysis
# --------------------------------------------------------------------------

@dataclass
class Flag:
    kind: str
    line: int
    detail: str
    text: str


def syllable_count(word: str) -> int:
    word = word.lower()
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and not word.endswith(("le", "ee")) and count > 1:
        count -= 1
    return max(1, count)


def percentile(values: list[int], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(ordered[lower])
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def is_noun_like(token: str) -> bool:
    lowered = token.lower()
    if lowered.endswith(ADJECTIVE_SUFFIXES) and not lowered.endswith(NOUN_SUFFIXES):
        return False
    return any(lowered.endswith(suffix) for suffix in NOUN_SUFFIXES)


def noun_stacks(sentence: str, max_len: int = 4) -> list[tuple[str, int]]:
    runs: list[list[str]] = []
    current: list[str] = []
    previous_end: int | None = None

    for match in WORD_RE.finditer(sentence):
        token = match.group(0)
        # A run must be contiguous words. Punctuation breaks it, because a
        # comma or colon usually separates two different phrases.
        gap = sentence[previous_end:match.start()] if previous_end is not None else ""
        if gap.strip():
            if current:
                runs.append(current)
            current = []
        previous_end = match.end()

        lowered = token.lower()
        if (
            lowered in STOPWORDS
            or lowered.endswith("ly")
            or (token.isupper() and len(token) <= 4)
        ):
            if current:
                runs.append(current)
            current = []
        else:
            current.append(token)
    if current:
        runs.append(current)

    stacks: list[tuple[str, int]] = []
    for run in runs:
        if len(run) < 3:
            continue
        # A title or proper name ("Designing Statistical Language Learners")
        # is not a noun compound.
        if all(token[0].isupper() for token in run):
            continue
        noun_like = sum(1 for token in run if is_noun_like(token))
        if noun_like == 0:
            continue
        if len(run) == 3 and noun_like < 2:
            continue
        # Display a window, but report the true length of the run.
        stacks.append((" ".join(run[:max_len]), len(run)))
    return stacks


def analyze(doc: Document, max_sentence: int = 30) -> dict:
    sentences = doc.sentences
    lengths = [len(WORD_RE.findall(sentence)) for sentence, _ in sentences]

    flags: list[Flag] = []
    nominalizations = 0
    passive_count = 0
    filler_count = 0
    noun_stack_count = 0
    of_chain_count = 0
    front_loaded_count = 0
    em_dashes = 0
    semicolons = 0
    long_words = 0
    existential_count = 0
    light_verb_count = 0
    connective_counts = {name: 0 for name in CONNECTIVE_LISTS}
    total_words = sum(lengths)

    for sentence, line in sentences:
        words = WORD_RE.findall(sentence)
        length = len(words)
        lowered = sentence.lower()

        if length > max_sentence:
            flags.append(Flag(
                "long-sentence", line, f"{length} words", sentence,
            ))

        nominalizations += len(NOMINALIZATION_RE.findall(sentence))
        passive_count += len(PASSIVE_RE.findall(sentence))
        long_words += sum(1 for word in words if syllable_count(word) >= 3)
        em_dashes += sentence.count("—")
        semicolons += sentence.count(";")

        for match in EXISTENTIAL_RE.finditer(sentence):
            existential_count += 1
            flags.append(Flag(
                "existential", line, match.group(0).lower(), sentence,
            ))

        for match in LIGHT_VERB_RE.finditer(sentence):
            light_verb_count += 1
            flags.append(Flag(
                "light-verb", line, match.group(0).strip(), sentence,
            ))

        for name, pattern in CONNECTIVE_PATTERNS.items():
            connective_counts[name] += len(pattern.findall(sentence))

        for phrase, pattern in FILLER_PATTERNS:
            if pattern.search(sentence):
                filler_count += 1
                flags.append(Flag(
                    "filler", line, phrase, sentence,
                ))

        for phrase, pattern in HEDGE_PATTERNS:
            if pattern.search(sentence):
                flags.append(Flag(
                    "hedge", line, phrase, sentence,
                ))

        stacks = noun_stacks(sentence)
        for stack, count in stacks:
            noun_stack_count += 1
            flags.append(Flag(
                "noun-stack", line, f"{count} nouns", stack,
            ))

        of_count = len(re.findall(r"\bof\b", lowered))
        if of_count >= 3:
            of_chain_count += 1
            flags.append(Flag(
                "of-chain", line, f"{of_count} 'of' phrases", sentence,
            ))

        comma = sentence.find(",")
        if comma != -1:
            prefix_words = len(WORD_RE.findall(sentence[:comma]))
            if prefix_words >= 12:
                front_loaded_count += 1
                flags.append(Flag(
                    "front-loaded", line,
                    f"{prefix_words} words before comma", sentence,
                ))

        if sentence.count(",") >= 4 and length > 25:
            flags.append(Flag(
                "dense-punctuation", line, f"{sentence.count(',')} commas", sentence,
            ))

    cohesion_pairs = 0
    cohesion_gaps = 0
    overlaps: list[float] = []
    for paragraph in doc.paragraphs:
        # Bullets are parallel items, not prose. Cohesion between them is
        # carried by the list's introduction, not by word overlap.
        if paragraph.is_list_item:
            continue
        previous: set[str] | None = None
        seen: set[str] = set()
        for sentence, start in split_sentences(paragraph.text, min_words=1):
            current = content_stems(sentence)
            if (
                previous is not None
                and len(previous) >= 2
                and len(current) >= 2
            ):
                overlap = len(previous & current) / min(
                    len(previous), len(current)
                )
                overlaps.append(overlap)
                cohesion_pairs += 1
                # A sentence is linked if it shares a content word with any
                # earlier sentence in the paragraph, or carries a pronoun.
                # The lexical proxy cannot resolve pronouns; it treats them
                # as links rather than false gaps.
                if not (seen & current) and not PRONOUN_RE.search(sentence):
                    cohesion_gaps += 1
                    flags.append(Flag(
                        "cohesion-gap",
                        paragraph.line_for(start),
                        "no shared content word",
                        sentence,
                    ))
            seen |= current
            previous = current

    for line, heading in doc.headings:
        heading_words = len(WORD_RE.findall(heading))
        if heading_words > 12:
            flags.append(Flag(
                "long-heading", line, f"{heading_words} words", heading,
            ))

    mean_length = total_words / len(lengths) if lengths else 0.0
    long_share = (
        sum(1 for length in lengths if length > max_sentence) / len(lengths)
        if lengths else 0.0
    )
    nominalization_rate = (
        nominalizations / total_words * 100 if total_words else 0.0
    )
    noun_stack_rate = (
        noun_stack_count / total_words * 1000 if total_words else 0.0
    )
    long_word_share = long_words / total_words * 100 if total_words else 0.0

    if (
        long_share > 0.20
        or nominalization_rate > 6
        or mean_length > 26
        or percentile(lengths, 0.9) > 35
    ):
        triage = "HIGH"
    elif (
        long_share > 0.10
        or nominalization_rate > 3.5
        or mean_length > 20
        or percentile(lengths, 0.9) > 28
    ):
        triage = "MEDIUM"
    else:
        triage = "LOW"

    return {
        "metrics": {
            "words": total_words,
            "sentences": len(sentences),
            "paragraphs": len(doc.paragraphs),
            "headings": len(doc.headings),
            "code_blocks_skipped": doc.code_blocks,
            "mean_sentence_length": round(mean_length, 1),
            "median_sentence_length": round(percentile(lengths, 0.5), 1),
            "p90_sentence_length": round(percentile(lengths, 0.9), 1),
            "max_sentence_length": max(lengths) if lengths else 0,
            "long_sentence_share": round(long_share * 100, 1),
            "nominalizations": nominalizations,
            "nominalizations_per_100_words": round(nominalization_rate, 1),
            "passive_ish": passive_count,
            "filler_hits": filler_count,
            "existential_there": existential_count,
            "light_verbs": light_verb_count,
            "cohesion_pairs": cohesion_pairs,
            "cohesion_gaps": cohesion_gaps,
            "mean_adjacent_overlap": (
                round(sum(overlaps) / len(overlaps), 2) if overlaps else 0.0
            ),
            "causal_connectives": connective_counts["causal"],
            "contrastive_connectives": connective_counts["contrast"],
            "additive_connectives": connective_counts["additive"],
            "temporal_connectives": connective_counts["temporal"],
            "noun_stacks": noun_stack_count,
            "noun_stacks_per_1000_words": round(noun_stack_rate, 1),
            "of_chains": of_chain_count,
            "front_loaded_clauses": front_loaded_count,
            "em_dashes": em_dashes,
            "semicolons": semicolons,
            "long_word_share": round(long_word_share, 1),
        },
        "triage": triage,
        "sentences": [
            {
                "line": line,
                "words": len(WORD_RE.findall(sentence)),
                "text": sentence,
            }
            for sentence, line in sentences
        ],
        "flags": [
            {
                "kind": flag.kind,
                "line": flag.line,
                "detail": flag.detail,
                "text": flag.text,
            }
            for flag in flags
        ],
    }


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

KIND_LABELS = {
    "long-sentence": "Long sentences",
    "cohesion-gap": "Cohesion gaps",
    "existential": "Existential 'there'",
    "light-verb": "Light verbs",
    "filler": "Filler",
    "hedge": "Hedging",
    "noun-stack": "Noun-stack candidates",
    "of-chain": "Chains of 'of'",
    "front-loaded": "Front-loaded clauses",
    "dense-punctuation": "Dense punctuation",
    "long-heading": "Long headings",
}

KIND_ORDER = [
    "long-sentence",
    "cohesion-gap",
    "existential",
    "light-verb",
    "filler",
    "hedge",
    "noun-stack",
    "of-chain",
    "front-loaded",
    "dense-punctuation",
    "long-heading",
]


def truncate(text: str, width: int = 96) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= width:
        return text
    return text[: width - 1].rstrip() + "…"


def print_text(
    report: dict, source: str, max_sentence: int, limit: int
) -> None:
    metrics = report["metrics"]
    print(f"Readable Docs check — {source}")
    print("=" * 60)
    print(
        f"Words {metrics['words']:,}  ·  "
        f"Sentences {metrics['sentences']}  ·  "
        f"Paragraphs {metrics['paragraphs']}  ·  "
        f"Headings {metrics['headings']}"
    )
    print(
        f"Sentence length: mean {metrics['mean_sentence_length']}  ·  "
        f"median {metrics['median_sentence_length']}  ·  "
        f"p90 {metrics['p90_sentence_length']}  ·  "
        f"max {metrics['max_sentence_length']}"
    )
    print(
        f"Long sentences (>{max_sentence} words): "
        f"{metrics['long_sentence_share']}%"
    )
    print(
        f"Nominalizations: {metrics['nominalizations_per_100_words']} "
        f"per 100 words ({metrics['nominalizations']} total)"
    )
    print(
        f"Noun-stack candidates: {metrics['noun_stacks']} "
        f"({metrics['noun_stacks_per_1000_words']} per 1,000 words)"
    )
    print(
        f"Passive-ish: {metrics['passive_ish']}  ·  "
        f"Existential 'there': {metrics['existential_there']}  ·  "
        f"Light verbs: {metrics['light_verbs']}  ·  "
        f"Filler: {metrics['filler_hits']}"
    )
    print(
        f"Cohesion: mean adjacent overlap "
        f"{metrics['mean_adjacent_overlap']}  ·  "
        f"{metrics['cohesion_gaps']} gaps in "
        f"{metrics['cohesion_pairs']} pairs"
    )
    print(
        f"Connectives: causal {metrics['causal_connectives']}  ·  "
        f"contrast {metrics['contrastive_connectives']}  ·  "
        f"additive {metrics['additive_connectives']}  ·  "
        f"temporal {metrics['temporal_connectives']}"
    )
    print(
        f"'of' chains: {metrics['of_chains']}  ·  "
        f"Front-loaded: {metrics['front_loaded_clauses']}  ·  "
        f"Long words: {metrics['long_word_share']}%  ·  "
        f"Em dashes: {metrics['em_dashes']}  ·  "
        f"Semicolons: {metrics['semicolons']}"
    )
    print()
    print(
        f"Triage: {report['triage']}. Heuristic only. Review the flags; "
        "do not rewrite for the score."
    )

    if not report["flags"]:
        print("\nNo flags. Check comprehension with the verification tests.")
        return

    print("\nFlags")
    print("-" * 60)
    by_kind: dict[str, list[dict]] = {}
    for flag in report["flags"]:
        by_kind.setdefault(flag["kind"], []).append(flag)

    ordered_kinds = KIND_ORDER + [
        kind for kind in by_kind if kind not in KIND_ORDER
    ]
    for kind in ordered_kinds:
        flags = by_kind.get(kind)
        if not flags:
            continue
        print(f"\n{KIND_LABELS.get(kind, kind)} ({len(flags)})")
        for flag in flags[:limit]:
            print(
                f"  L{flag['line']:<5} {flag['detail']:<28} "
                f"{truncate(flag['text'])}"
            )
        if len(flags) > limit:
            print(f"  ... {len(flags) - limit} more")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag likely sources of reading difficulty in a document.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="-",
        help="Markdown or text file, or - for stdin (default: -)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of text",
    )
    parser.add_argument(
        "--max-sentence",
        type=int,
        default=30,
        metavar="N",
        help="Word count that triggers a long-sentence flag (default: 30)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        metavar="N",
        help="Maximum flags to print per category (default: 10)",
    )
    args = parser.parse_args()

    if args.path == "-":
        source = sys.stdin.read()
        name = "<stdin>"
    else:
        path = Path(args.path)
        if not path.is_file():
            print(f"error: no such file: {path}", file=sys.stderr)
            return 2
        source = path.read_text(encoding="utf-8")
        name = str(path)

    if not source.strip():
        print(f"error: {name} is empty", file=sys.stderr)
        return 2

    doc = parse_document(source)
    report = analyze(doc, max_sentence=args.max_sentence)

    if args.json:
        json.dump(
            {"source": name, **report},
            sys.stdout,
            indent=2,
            ensure_ascii=False,
        )
        print()
    else:
        print_text(report, name, args.max_sentence, args.limit)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
