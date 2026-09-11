# Contributing

Thank you for reading closely enough to want to change something.

## Clinical corrections come first, and they come separately

**Open a separate issue or pull request for every clinical correction. Do not bundle a clinical correction with a stylistic one.** A clinical fix should be reviewable and mergeable in minutes; a discussion about phrasing should never be able to delay it.

A clinical correction must include:

1. **Exactly what is wrong** — unit number, section, and the sentence as written.
2. **What it should say.**
3. **A primary source.** The 2025 AHA/AAP Part 5 guideline, the ILCOR 2025 CoSTR, a named national guideline, or a peer-reviewed paper. Please cite the specific recommendation or page, not the document as a whole.
4. **Whether it is a safety issue.** Label it `safety` if a learner acting on the current text could harm a patient. These are triaged first and fixed same-day where possible.

Textbook secondary sources, lecture slides, and "this is how we do it at my hospital" are welcome as *context* but are not sufficient on their own to change a stated recommendation.

## Guideline updates

Neonatal resuscitation guidance changes on roughly a five-year cycle, with intermediate updates. If a guideline changes, open an issue titled:

> `[GUIDELINE UPDATE] <organisation> <year> — <what changed>`

List every unit, appendix table and assessment item affected. A guideline change usually touches the unit text, Appendix E, the checkpoint items, the fresh exam items, and the "what changed" table in Unit 3 — missing one of those leaves the module internally contradictory, which is worse than being uniformly out of date.

## Stylistic and structural suggestions

Very welcome, in their own issues. Particularly useful:

- Places where the prose is longer than it needs to be. A sentence that can be deleted without loss should be deleted.
- Items where a distractor is implausible, or where two options are defensible.
- Rationales that explain the right answer but not why the wrong ones are wrong.
- Accessibility problems, especially from screen-reader users. The module targets WCAG 2.2 AA but has not been independently audited, and real user reports are worth more than any automated check.

## Technical constraints — these are not negotiable

The module exists to work where other things do not. Please do not submit changes that:

- **Add a dependency.** No framework, no library, no build step, no package manager. One HTML file.
- **Add a network request.** No CDN, no web font, no remote image, no analytics endpoint. It must work with the network disconnected, and it must be verifiable that it does.
- **Add telemetry.** No analytics, no tracking, no "anonymous usage statistics", no error reporting service. The privacy position is that the module collects nothing, and that must remain literally true.
- **Require an account or a server.**
- **Break the single-file property.** Images must be embedded as data URIs, and only when they genuinely earn their size.
- **Introduce a "mark as read" control** or any other way to record progress without demonstrating it. This is the central design commitment.

If you think one of these constraints should change, open an issue arguing the case before writing code.

## Building

Content lives in `build/` as numbered fragments and is concatenated by `build.py` into `index.html`. Run:

```
python3 build.py
```

It enforces structural checks: unit count, unique question ids, exactly one correct option per item, balanced sections, no leftover markers, and that every `getElementById` has a matching `id`. **A pull request that does not build cleanly will not be reviewed.**

## Translation

Translations are genuinely valuable and genuinely welcome — Hindi, Bengali, Marathi, Tamil, Telugu, Kannada and Malayalam would each reach people this module currently does not.

Two requirements:

1. **Clinical review.** A translation must be reviewed by a clinician fluent in the target language who works in newborn care. Translation errors in doses are the failure mode here, and they are silent.
2. **The identity carve-out applies.** A translated version must remove the *Vikkypaedia* name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and the certificate signature block, and must not issue certificates bearing his name, photograph or signature. Put your own name on it — you did the work, and you are the one standing behind the clinical accuracy of the text in that language. See `LICENSE.md`.

Please open an issue before starting a translation so effort is not duplicated.

## Code of conduct

Be decent. Assume the person on the other end is trying to get it right. Disagree about the evidence as much as you like; that is the point.
