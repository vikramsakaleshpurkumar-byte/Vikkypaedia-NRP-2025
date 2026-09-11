# How to get this onto GitHub

The folder you are reading this in is a complete, ready-to-publish repository.
Everything is already in place — you only need to create the repo and push.

**Repo name:** `Vikkypaedia-NRP-2025`
(GitHub does not allow spaces; "Vikkypaedia NRP 2025" becomes this automatically.)

**Live URL once Pages is on:**
https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-NRP-2025/

---

## Option A — Web browser only (no software needed, ~3 minutes)

1. Go to https://github.com/new
2. **Repository name:** `Vikkypaedia-NRP-2025`
3. **Description:** `Mastery-based, offline-first neonatal resuscitation module aligned to the 2025 AHA/AAP guidelines and ILCOR 2025. One HTML file. No account, no tracking.`
4. Set it to **Public**. Do **not** tick "Add a README" — you already have one.
5. Click **Create repository**.
6. On the next page click **uploading an existing file**.
7. Open this folder (`Documents\Vikkypaedia-NRP-2025`), select **all files**
   (Ctrl+A) **and the `build` folder**, and drag them into the browser window.
   - Windows Explorer hides `.gitignore` and `.nojekyll` by default.
     Turn on **View → Show → Hidden items** first so they get included.
8. Commit message: `Neonatal Resuscitation 2025 v1.0.0`
9. Click **Commit changes**.

Then turn on Pages — see "Enable GitHub Pages" below.

---

## Option B — Command line (if you have Git installed)

Open **Git Bash** or **PowerShell** in this folder and run:

```bash
git init -b main
git add -A
git commit -m "Neonatal Resuscitation 2025 v1.0.0"
git remote add origin https://github.com/vikramsakaleshpurkumar-byte/Vikkypaedia-NRP-2025.git
git push -u origin main
```

You must create the empty repo at https://github.com/new first (steps 1–5 above).

---

## Enable GitHub Pages

1. In the repository, go to **Settings → Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `main`, folder `/ (root)`
4. **Save**

Wait 1–2 minutes, then open:
https://vikramsakaleshpurkumar-byte.github.io/Vikkypaedia-NRP-2025/

`.nojekyll` is already included so GitHub serves the file as-is without
running Jekyll over it.

---

## IMPORTANT — do this before you share the link

The `index.html` currently in this folder is the **unconfigured** build.
The certificate will carry the default signatory and no photograph.

To fix that:

1. Open `index.html` in your browser (double-click it).
2. Scroll to **Final assessment → Faculty settings**.
3. Set the signatory name, designation, course title, and — if you want one —
   your cut score, item count, time limit, attempts and retention bar.
4. Click **Export a configured copy**.
5. Rename the downloaded file to `index.html` and replace the one in this
   folder (and in the repo).

Two traps that catch everyone:
- Publishing the unconfigured file, so the certificate has no signatory.
- Embedding a full-resolution photograph. Base64 adds about a third to the
  file size — resize to roughly 400×400 pixels first.

---

## Suggested repository settings

**Topics** (Settings → General, or the gear beside "About"):
`neonatal-resuscitation` `medical-education` `paediatrics` `neonatology`
`cbme` `global-health` `open-educational-resources` `offline-first`

**About → Website:** paste the GitHub Pages URL once it is live.

---

## What is in this folder

| File | What it is |
|---|---|
| `index.html` | The entire module. This is the deliverable. 603 KB, works offline. |
| `README.md` | Repository front page — audience, structure, certification, limitations. |
| `ANNOUNCEMENT.md` | Ready-to-post copy: Substack, LinkedIn, WhatsApp, one-liners. |
| `CONTRIBUTING.md` | How corrections are submitted. Clinical fixes first, with sources. |
| `LICENSE.md` | CC BY-NC-SA 4.0 with the identity carve-out, plus the trademark notice. |
| `build/` | The source fragments the module is assembled from. |
| `build.py` | Rebuilds `index.html` from `build/` and runs structural checks. |
| `.nojekyll` | Tells GitHub Pages to serve the file as-is. |
| `.gitignore` | Keeps screenshots and scratch files out of the repo. |

To rebuild after editing anything in `build/`:

```bash
python3 build.py
```

It will refuse to produce a broken file — it checks the unit count, that every
question id is unique, that each item has exactly one correct option, that the
section tags balance, and that every JavaScript element lookup has a matching id.
