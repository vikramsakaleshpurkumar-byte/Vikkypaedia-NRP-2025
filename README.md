# Neonatal Resuscitation 2025

**A mastery-based, self-paced, offline-first module on resuscitation and stabilisation of the newborn infant at birth.**

Live: https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-NRP-2025/

Written to the **2025 AHA/AAP neonatal resuscitation guidelines** (Lee HC, Szyld E, et al. *Part 5: Neonatal Resuscitation.* Pediatrics 2025; doi:10.1542/peds.2025-074352) and the **ILCOR 2025 Consensus on Science with Treatment Recommendations**.

---

## What it is

One self-contained HTML file. No framework, no CDN, no network request, no account, no server. It works on a phone in aeroplane mode, and it will still work in five years when whatever platform you were considering has shut down.

- **24 units in 5 Parts**, ~30 notional hours
- **48 checkpoint items** + **30 fresh integrative items** for the final assessment
- **Mastery-gated**: Parts unlock in sequence; there is no "mark as read" control anywhere
- **Spaced retrieval** at 1 → 3 → 7 → 21 → 60 days, interleaved across units
- **Tiered hints** before every answer — a nudge, then a structured hint
- **Three-criterion certification**: coverage + retention + applied performance
- **Dual-track clinical content**: *ideal setting* and *resource-constrained setting* as equals
- **India lens** in every clinical unit
- Full-text search across every unit and appendix (Ctrl/Cmd K, or `/`)
- Key algorithms drawn as scalable SVG, each with a text version and a full-screen view
- Certificate as PNG and print-to-PDF

## Who it is for

| Audience | Track | Suggested scope |
|---|---|---|
| Staff nurses, ANMs, midwives, interns | ESSENTIALS | Parts A–C, Must-know filter on |
| MBBS doctors, PG residents (Paediatrics, OBG, Anaesthesia, EM) | ADVANCED | Parts A–D, all tiers |
| Paediatricians, neonatologists, faculty | EXPERT | All 24 units + Appendices A–G |

Three tracks live in one file. The toolbar switches between them; the placement questions set a sensible default.

## What makes it different from a MOOC

1. **Mastery, not completion.** A unit is mastered when both its checkpoint items are *currently* answered correctly. Fail one later and the unit loses its mastered status — which is what makes the coverage criterion mean something at the moment of certification.
2. **Certification on three independent criteria**, because a single score is not a defensible basis for a high-stakes decision about a clinician.
3. **Retention counts breadth across units**, not raw items — a raw count can be satisfied entirely from the units met earliest.
4. **Rationales explain why the wrong options are wrong**, and distractors are errors clinicians actually make.
5. **Emergency dosing is never gated.** Appendices E and F are open from the first minute.
6. **It publishes its own weaknesses** (Appendix G).

## Structure

- **Part A · Foundations and preparation** (Units 1–4) — epidemiology, transition physiology, the algorithm, anticipating the birth
- **Part B · The first sixty seconds** (5–9) — cord management, thermal care, initial steps and meconium, heart rate, oxygen and CPAP
- **Part C · Ventilation, the core skill** (10–14) — indications and settings, devices, mask technique, MR SOPA, alternative airways
- **Part D · When ventilation is not enough** (15–18) — compressions, vascular access, medications, knowing when to stop
- **Part E · Special populations, systems and futures** (19–24) — preterm, post-resuscitation care, special circumstances, CHD, outside the delivery room and NICU, teams and QI
- **Appendices A–G** — assessment bank, simulation library, faculty guide, curriculum mapping, drug annex, references, design evidence

## Certification

Three criteria, all required:

1. **Coverage** — all 48 checkpoint items currently correct
2. **Retention** — ≥18 of 24 units evidenced by an item answered correctly ≥24 h after first pass
3. **Applied performance** — 50 items sampled from 78, randomised, closed book, 75 minutes, 2 attempts, 24-hour lock, **cut score 90%**

> **The cut score is provisional.** Published comparisons of standard-setting methods applied to the *same* assessment have produced cuts from roughly 66% to 86%, which means the method can matter more than the candidates. Appendix C provides modified Angoff, Ebel and Hofstee worksheets and borderline-regression guidance. Do the standard setting before using this for any consequential decision.

## Enrolment and completion records

On first open the module runs a short four-step enrolment: what it is and how it works, your name and institution, the three placement questions, and a study plan with a target date you set by choosing minutes per sitting and days per week. It can be skipped, and edited later from the profile bar above the dashboard.

**Everything stays on the device.** There is no account and no server; the details are written to the same `localStorage` key as your progress, so they can be printed on the certificate and included in a record you choose to export.

Once all three criteria are met, **Download completion record** produces a small JSON file holding the learner's details, the three criteria, the verification code and a checksum. Faculty open it in `verify.html` — a second offline page in this repository — which reads it back in plain language and recomputes the checksum.

> **A completion record is self-attested.** It is produced on the learner's own device, and the checksum is a plain hash computed by code that ships inside the module, so anyone holding the file can recompute it. A match tells you the record has not been casually altered, mistyped or truncated in transit. It does **not** prove the learner sat the assessment, and it is not evidence issued by a third party. Records you can rely on for promotion, credentialling or audit need a server-side system with authenticated sign-in, which this deliberately is not.

## For learners

1. Open the file. Complete the four-step enrolment (or skip it).
2. Work through Part A. Both checkpoints per unit, answered cold.
3. Use the hints when stuck — a hinted item still counts, it simply returns sooner.
4. Answer the retention checks when they appear at the top of the page. That spacing is the point.
5. When all three criteria are met, generate your certificate.

**To keep it on your phone:** download the file and open it from your Downloads folder, or use "Add to Home Screen" in your browser. It never needs the internet again. Your progress lives in that browser on that device only.

## For faculty adopting it

1. Open **Final assessment → Faculty settings**. Set signatory, cut score, item count, time limit, attempts and retention bar, and upload a **signature image** if you want one on the certificate — scan or photograph your signature on white paper and the module downscales it to 600 px, mattes the paper out to transparency and stores it inside the file.
2. Click **Export a configured copy**.
3. Rename the download to `index.html`, upload to your repository, enable GitHub Pages. Upload `verify.html` alongside it if you want to read learners' completion records.

**Two traps that catch everyone:**
- Uploading the *unconfigured* file, so the certificate carries no signatory.
- Feeding the signature field a full-resolution photograph. It is downscaled for you, but start from a tight crop of the signature rather than a whole page: the stored size is shown next to the preview, and a good one is well under 20 KB.

See **Appendix C** for three delivery models, a worked flipped-classroom session plan, feedback structures, the six-domain rubric, standard-setting worksheets and a Kirkpatrick evaluation plan. See **Appendix B** for four branching simulation scenarios that run on a doll and printed vital-sign cards.

## Engine v2.1 (module v1.6.0, 2026-09-24)

This module now runs on the same shared engine as every other Vikkypaedia module. All module-specific values (Parts, cut score, certificate wording, placement text) live in `build/05_module.html`; `build/90_script.html`, `build/89_loops.js` and `build/06_loops.css` are identical across modules. Learner progress is kept (the storage key is unchanged). The version bump changes the certificate verification code for certificates issued from now on.

## Learning loops (Vikkypaedia Standard v2.1 · module v1.6.0)

Every loop is tied to mastery; nothing rewards clicking.

| Loop | What the learner sees | Why |
|---|---|---|
| **Review queue** | A "N due" badge in the topbar opens a runner that works the whole spaced-retrieval queue, one item at a time (keys 1–4, Esc) | Retention is one of the three certification criteria; this makes it one tap away |
| **Next step** | One named action on the dashboard — clear reviews, revisit a confident-and-wrong item, finish the unit in progress, start the next unit, or sit the assessment — plus when the next check returns | Removes the "what now?" decision that stalls self-paced learners |
| **Confidence** | "Sure / Fairly sure / Guessing" before answering; *confident and wrong* is flagged; a calibration tile reports how often "sure" was right | Hypercorrection effect; calibration is a clinical safety skill |
| **Study days** | A 14-day strip, days this week against the plan, and a best run — never reset, never shamed | Habit without punishing night duty |
| **Moments** | A brief notice when a unit is mastered or a Part unlocks | Recognition of earned progress only |
| **Passport** | Progress is summarised into `vkp.passport.v1`, shared by every Vikkypaedia module on this site; a second module pre-fills enrolment from it | One learner across modules, still no server |
| **Print any appendix** | A print button on each appendix — the drug and equipment annex prints on A4 portrait for the resus trolley | Safety material should never be screen-only |

Rejected by design: points, badges, leaderboards, streak resets.

## Privacy

All state lives in the learner's browser under one versioned `localStorage` key — progress, preferences, and the enrolment details if any were given. No account, no server, no analytics, no telemetry. Nothing is transmitted anywhere, and a completion record leaves the device only when the learner exports it and sends it themselves. The Digital Personal Data Protection Act 2023 is satisfied by collecting nothing centrally at all. One-click irreversible erase is provided.

## Search

`Ctrl`/`Cmd` + `K`, or just `/`, opens a palette that searches all 24 units and the appendices. Two deliberate limits:

- **Rationales, hints, option lists and remediation notes are never indexed.** Searching must not become a way to read the answer to a checkpoint you have not attempted. Question stems are indexed, because finding the item you half remember is useful and a stem alone reveals nothing.
- **Results from locked units are shown, but without their text** — you see that the answer lives in Unit 17 and which Part opens it, not the content itself. Gating that search could walk around would not be gating.

## Diagrams

The algorithms that matter most are drawn as inline SVG rather than monospace art: they scale, they stay legible on a phone, they follow the light and dark themes, and they open full screen on a tap. Every one keeps its original text version underneath, one click away, for screen readers and for anyone who prefers it. The remaining monospace blocks are unchanged and still readable.

## Rebuilding and testing it

`index.html` is generated. The source is the numbered fragments in `build/`, concatenated by `build.py`, which also asserts the structure (unit count, unique question ids, exactly one correct option per item, balanced sections, and every script `id` reference resolving).

```bash
python build.py
python tests/test_full.py      # and the other suites — see tests/README.md
```

Note that the **published `index.html` is a configured export**, carrying the signatory and cut score, so it will not be byte-identical to what `build.py` produces. That is intended: `build/` is the unconfigured source, and the published file is a distribution of it.

## Known limitations

Published in full in **Appendix G**. In summary: fixed spaced-retrieval intervals rather than fitted forgetting curves; thin item sampling (two items per unit); rule-based placement rather than adaptive testing; limited form-to-form equivalence; unproctored assessment; a verification code and completion-record checksum that are re-derivable rather than tamper-proof, making records self-attested; a provisional cut score; Kirkpatrick levels 3 and 4 unmeasured; accessibility targeted at WCAG 2.2 AA but not independently audited; clinical content not externally peer reviewed; single-author tiering judgements.

## Independence and trademark

This is an **original educational work**. It is not the Neonatal Resuscitation Program®, is not affiliated with, endorsed by, or derived from the text of the AAP *Textbook of Neonatal Resuscitation*, and completing it confers **no NRP® provider status or eCard**. NRP® is a registered trademark of the American Academy of Pediatrics and is used here only to identify that programme, not to describe this one. No AAP or AHA text, figures, tables or marks are reproduced.

## Contributing

Clinical corrections are welcome and expected. See `CONTRIBUTING.md`. Corrections with a primary source take priority over everything else in the queue.

## Licence

CC BY-NC-SA 4.0, **excluding** the *Vikkypaedia* name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and the certificate signature block. See `LICENSE.md`.

## How to cite

> Sakaleshpur Kumar V. *Neonatal Resuscitation 2025: an evidence-governed, competency-based digital module for resource-constrained settings.* Vikkypaedia; 2026. Available from: https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-NRP-2025/

## Disclaimer

Education, not a protocol, and not certification to practise. Verify every dose, threshold and device setting against your institution's current protocol and the manufacturer's instructions before use in a patient. Neonatal resuscitation guidance changes on roughly a five-year cycle — if you are reading this more than three years after the build date in the footer, assume something is out of date and check.

## Interactive megacodes (engine v2.2)

Six branching cases played one decision at a time against a patient monitor, in their own section before the final assessment. Each case opens when its Part opens. Wrong calls cost time or change the patient, critical errors (tenfold doses, a shock with a pulse, compressions before effective ventilation, and similar) are flagged, and every option is explained. Options are shuffled on every run. The debrief shows right decisions, critical errors, key times against targets, and links back to the units.

- **Formative only.** Results are stored locally, appear in the completion record (`detail.megacodes`, covered by the detail checksum) and in the faculty class report on the hub. They are not a certification criterion.
- **Authoring:** cases live in `megacodes/cases.py`. Every dose is taken from this module's drug annex (Appendix E) and worked out for the stated weight. Compile with `python megacodes/make.py`, which validates the graph (every node reachable, a correct option at every step, correct-only paths acyclic and ending well, only `<b>`/`<i>` markup) and writes `build/86_megacodes.html`. Then run `python build.py`.
- The player (`build/87_megacode.js`) is shared by every Vikkypaedia module and does nothing in a module without cases.
- Clinically reviewed against the 2025 AHA/AAP guidelines before release (2026-09-24). Re-review whenever the guidelines change.
