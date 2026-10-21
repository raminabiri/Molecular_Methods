# PROGRESS

## 1. Current goal
A Persian bench reference for molecular methods: **18 topics**, each with the same 6 files —
`01_Theory.md` (chemistry + instrument engineering), `02_Protocol.md` (written for someone who has
never been in a lab), `03_Troubleshooting.md` (senior-supervisor level), `04_Assessment.md`,
`05_Answers.md`, `06_Reference_Tables.md`.
All 18 topics are written and pushed. The work in progress now is a **teaching-consistency pass**
over every file (see section 2), not new content. After that: peer review and 🔎 number checks.

## 2. Done so far
- All **18 topics** written and pushed; every folder holds exactly 6 files. `README.md` (18 topics,
  6-file template, marker legend, review-status table, review instructions) and `LICENSE`
  (CC BY 4.0, bilingual) are in place.
- Topic 14 expanded earlier on user request (full vector taxonomy + all cloning methods with a
  "which method when" table).
- **Teaching-consistency pass, uncommitted (88 files changed).** The agreed format per file type:
  - `01_Theory.md`: header line (`پیش‌نیاز` · `زمان خواندن` · `فصل‌های مرتبط`), then
    **در یک نگاه** (5 learning outcomes), **داستان**, **مفهوم به زبان ساده**, the numbered
    technical sections (unchanged), then **اشتباه‌های رایج**, **📘 برای کنجکاوها**,
    **جمع‌بندی**, **واژه‌نامه‌ی درس**, `منابع`.
  - `03_Troubleshooting.md`: diagnosis **tables replaced by numbered prose scenarios**, each as
    *چه می‌بینید / علت / آزمون / چه کنید*, under a fixed intro line naming the level
    (`سطح این فایل: سرپرست آزمایشگاه مولکولی`).
  - `04_Assessment.md`: a `> راهنمایی:` line after **every** question — a formula or a pointer to
    the exact theory/troubleshooting section, never the answer.
  - `05_Answers.md`: closing section **اشتباه‌های رایج در این مجموعه** (4–5 items, each naming the
    question numbers it comes from).
  - `02_Protocol.md`: a **منطق کلی** paragraph in the intro explaining why the steps exist,
    `مثلاً` → `برای نمونه`, and 🔎 (not ❗) on kit-dependent numbers.
- **State of that pass, per file type:**
  - Theory: **all 18 done** (topic 18 framed this session from the topic-17 pattern).
  - Troubleshooting: **all 18 done** (01–13 earlier; 14–18 converted this session).
  - Assessment hints: **all 18 done** (13–18 added this session).
  - Answers "common mistakes": **all 18 done** (14–18 added this session).
  - Protocol: `منطق کلی` now in **01, 02, 03, 12, 14, 15, 16, 17, 18**; still missing in
    **04–11 and 13**. No `مثلاً` left in any protocol file (all → `برای نمونه`), and the
    kit-dependency intro lines of 02, 03, 14, 16, 17, 18 now carry 🔎 instead of ❗.
- Fixed this session: stale cross-reference in `15_…/01_Theory.md` (فصل ۰۱ بخش ۶.۶ → ۷.۶); topic 13
  troubleshooting rewritten in full; the hint cross-references in topic 15's assessment were
  corrected against the real section numbers of its theory file.

## 3. Files changed (uncommitted)
- `01_…` to `18_…`: theory, protocol, troubleshooting, assessment and answers files touched by the
  pass — 86 topic files plus `PROGRESS.md`.
- Helper scripts live in the session scratchpad, **not** in the repo:
  `/tmp/claude-1000/-data-Education-Molecular-Methods/5b05b9b0-3beb-443e-a779-786328a08885/scratchpad/`
  — `tables2prose.py` (troubleshooting tables → numbered prose) and `add_hints.py` (inserts
  `> راهنمایی:` lines from a JSON file keyed by question number). Copy them into the next session
  if the same transformation is needed again; the originals of the converted troubleshooting files
  are kept there as `1[4-8]_ts_orig.md`.
- ⚠️ Heading numbering inside `14_…/01_Theory.md` uses `۲.۳`–`۲.۹` and `۴.الف…` on purpose, so the
  existing section numbers and the references to them stay valid. **Do not renumber.**

## 4. Key decisions and rejected approaches
| Decision | Reason |
| :--- | :--- |
| Troubleshooting as prose scenarios, not tables | a table cell cannot hold *why* + *how to isolate*; the file is meant to be read, not scanned |
| Every question gets a hint pointing to a section | the files are used for self-study; a hint keeps the question solvable without the answer key |
| Hints must cite real section numbers | a wrong pointer is worse than none — all of them were verified against the theory files |
| "Common mistakes" lists cite question numbers | ties the general lesson back to concrete items |
| Protocols anchored to a named kit + 🔎 on every number to verify | kit versions change; prevents silently wrong volumes |
| Computational analysis kept out of the repo | wet-lab only; bench QC/interpretation stays |
| Microarray = a section inside NGS; typing = one shared 6-file set | avoids duplicated, drifting text |
| Topic 18: human germline/embryo editing and gene drives declared **out of scope** | ethics; stated in theory, protocol and tables |
| Licence **CC BY 4.0** | free reuse and translation with attribution |
| Rejected: fabricated YouTube/JoVE links from the old files | unverifiable; replaced with books, DOIs, official manuals |
| Rejected: a scheduled cloud routine to continue the work | cloud agents clone GitHub; the work was unpushed at the time |

## 5. Known bugs / corrections
No build or runtime errors — this is a documentation repo.

**(a) Scientific errors found in the OLD content and fixed in the rewrite**
- Old `04_Standard_PCR/03_pcr_exercises…` Q7: primer `ATGCGATCGATCGATCGATC` called 40% GC with
  A=4,T=4,G=6,C=6 → it is **5 of each base, 50% GC**, Wallace Tm = **60 °C** (answer said 64 °C).
- Same file, answer 18: genome copies in 10 ng of a 4.5 Mb genome → **≈2.06×10⁶**, not 2.06×10⁹.
- Same file, answer 15: 1.85⁵ = **21.7×**, not 22.9×.
- Old Bio-Rad text: gradient described across 12 columns; on T100/C1000 it runs across **rows** →
  flagged "verify on your instrument".
- Retracted earlier suspicion: `E = 10^slope` in the LinRegPCR sections is **correct**.

**(b) Environment quirk, not a repo bug — do not "fix" the user's git config**
Claude's shell cannot push. Exact error from `gh auth status`:
```
X Timeout trying to log in to github.com account raminabiri (keyring)
```
and `git push` then hangs with no output. Cause: `~/.gitconfig` registers
`credential.https://github.com.helper = !/usr/bin/gh auth git-credential` (**per-URL**, which is why
`git config --get credential.helper` prints nothing — do not read that as "no helper"), gh cannot
reach the OS keyring in a headless session, so git falls back to *prompting* — and Claude's shell
has no TTY (`tty` → `not a tty`), so the prompt can never be answered.
**The user's own terminal pushes normally.** Ask them to run `git push`; reconfigure nothing.

## 6. Next steps (priority order, one session each)
1. **Add the `منطق کلی` paragraph to the protocols of 04–11 and 13** — the only part of the
   teaching pass still open. Pattern: a `> **منطق کلی:** …` line in the intro blockquote saying why
   the steps exist and pointing at the theory sections (see 02, 14 or 18 for the shape).
2. **Apply `_tools/rtl_wrap.py` to the topic files.** Only `STYLE_GUIDE.md` is wrapped in
   `<div dir="rtl">` so far; the 108 topic files are not. Decide whether the whole set gets wrapped
   (GitHub then renders them right-to-left) and do it in one commit, since the diff is mechanical.
3. **Commit and push each batch as it is finished** (the teaching pass itself is committed as of
   this session: theory / troubleshooting / assessment+answers / protocol, plus STYLE_GUIDE and
   _tools). Push from the user's own terminal if Claude's shell cannot (see 5b).
4. **Peer review, topic by topic.** Per reviewed file set `status: reviewed`, fill `reviewer` and
   `last_reviewed`, and update the review-status table in `README.md`.
5. **Verify the 🔎 numbers** against the manuals used in this lab — highest value per hour. Start
   with 05 PCR, 08 qPCR, 16 MALDI-TOF.
6. **Decide what to do with `/data/Molecular_Data_Analysis/`** (separate GitHub repo?) — still local
   and uncommitted; ask the user.
7. Optional: decide whether the `restructure` branch can be deleted locally and on the remote.
