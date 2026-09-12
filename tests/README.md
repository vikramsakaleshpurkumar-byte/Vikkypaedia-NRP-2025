# Test suites

Six Playwright suites that check the built `index.html` and `verify.html`. They open the files
directly from disk — no server, no network — and resolve paths relative to this folder, so they
run wherever the repository is cloned.

## Running them

```bash
pip install playwright
playwright install chromium

python build.py          # regenerate index.html from build/ first
python tests/test_full.py
python tests/test_ui.py
python tests/test_enrol.py
python tests/contrast.py
python tests/offline_test.py
python tests/print_test.py
```

Each prints `OK` / `FAIL` per check and ends with `FAILURES: none` when the build is sound.
`build.py` itself must print no `ERROR:` lines before any of these are worth running.

## What each one proves

| Suite | Checks |
|---|---|
| `test_full.py` | Part gating and lock enforcement (click, expand-all, hash), mastery reversal, tier/level/track filters, themes, the exam runner and scoring, the remediation plan, item review, the certificate canvas and print sheet, the configured-copy export, and a clean reload of that export in a fresh browser context |
| `test_ui.py` | Hints hidden on load and revealed one at a time, the progress ring and `--progress` and stat tiles and bar all agreeing, sticky topbar, styled mobile drawer, no horizontal scroll at 390 px, `scroll-behavior:auto` under reduced motion |
| `test_enrol.py` | The four-step first run and its required fields, plan recomputation, the profile bar and its persistence, Edit and Escape, the completion-record download and contents, and `verify.html` accepting a genuine record, rejecting a tampered score and surviving malformed JSON |
| `contrast.py` | Computed foreground/background ratio on every text element that matters, in light **and** dark. Everything must read `ok` (≥4.5:1) |
| `offline_test.py` | Zero non-`file://` requests on load, on opening a unit and on switching theme |
| `print_test.py` | The certificate renders and the printed PDF is exactly one A4 page |

## Two things that will bite you

**Seed `onboarded` before loading.** The first-run overlay is modal and blocks every click.
Each suite already does this with `ctx.add_init_script(SKIP_ONB)`; any new test must too.

**Use `reduced_motion="reduce"` for screenshots.** Smooth scrolling otherwise produces
half-painted captures that look like layout bugs and are not.
