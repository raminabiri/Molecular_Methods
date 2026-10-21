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

## 3. State of the tree
- **Nothing uncommitted, and `main` is pushed** (as of 2026-10-21, head `7f28023`). The teaching
  pass went up as five commits — theory / troubleshooting / assessment+answers / protocols /
  STYLE_GUIDE+_tools — plus one merge commit for the GitHub edit (see 5c).
- `STYLE_GUIDE.md` is the written convention the pass follows, with a checklist a file must pass
  before it can be marked `reviewed`. It is the first thing to read before editing content.
- Helper scripts are **in the repo** now, as `_tools/`: `add_hints.py` (inserts `> راهنمایی:` lines
  from a JSON file keyed by question number), `persian_words.py` (the safe replacements of
  STYLE_GUIDE §6, with `--report` for the ones needing judgement), `check_internal_links.py`
  (reports broken relative links; currently 0) and `rtl_wrap.py` (wraps a file in
  `<div dir="rtl">` — applied to `STYLE_GUIDE.md` only, not yet to the topic files).
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

**(b) Pushing from Claude's shell — it works now (2026-10-21)**
`git push origin main` from Claude's shell succeeds, so the earlier diagnosis
("Claude's shell cannot push") is no longer true; nothing in the git config was changed to make it
work. Run it with `GIT_TERMINAL_PROMPT=0` and a `timeout`, so that if the credential helper ever
falls back to prompting again the command fails fast instead of hanging with no output (Claude's
shell has no TTY, `tty` → `not a tty`, so a prompt can never be answered). It is **slow and not always
reliable**: one of the three pushes in this session hung and was killed by a 90-second `timeout`,
then the same push went through on the next try. So allow ~150 s, and on a timeout simply retry
before concluding anything is broken.

Still true, and still not a repo bug: `~/.gitconfig` registers
`credential.https://github.com.helper = !/usr/bin/gh auth git-credential` **per-URL**, which is why
`git config --get credential.helper` prints nothing — do not read that as "no helper" and do not
"fix" the user's git config.

**(c) The remote can be ahead: the user also edits files on GitHub**
Commit `4fc4d9e` ("Update 01_Theory.md", 2026-10-20) was a wording edit made in the GitHub web
editor, against the pre-pass version of `02_DNA_Extraction/01_Theory.md`. Always `git fetch` and
check `HEAD..origin/main` before pushing. When such an edit lands on text the pass has rewritten,
keep the rewritten file and carry over only the preferences that still apply, naming in the commit
message what was dropped and why (see `7f28023`).

**Open wording decision:** that edit changed استافیلوکوک → استافیلوکوکوس. It is now applied in
`02_DNA_Extraction/01_Theory.md` only. Elsewhere (02's protocol, troubleshooting and assessment,
and topic 16) the word still reads استافیلوکوک, mostly inside lists next to انتروکوک and
استرپتوکوک — so applying it repo-wide means deciding on those two as well. Ask the user.

## 6. Next steps (priority order, one session each)
1. **Add the `منطق کلی` paragraph to the protocols of 04–11 and 13** — the only part of the
   teaching pass still open. Pattern: a `> **منطق کلی:** …` line in the intro blockquote saying why
   the steps exist and pointing at the theory sections (see 02, 14 or 18 for the shape).
2. **Apply `_tools/rtl_wrap.py` to the topic files.** Only `STYLE_GUIDE.md` is wrapped in
   `<div dir="rtl">` so far; the 108 topic files are not. Decide whether the whole set gets wrapped
   (GitHub then renders them right-to-left) and do it in one commit, since the diff is mechanical.
3. **Commit and push each batch as it is finished** (the teaching pass itself is committed as of
   this session: theory / troubleshooting / assessment+answers / protocol, plus STYLE_GUIDE and
   _tools), and pushed. Fetch first — the remote may be ahead (see 5b and 5c).
4. **Peer review, topic by topic.** Per reviewed file set `status: reviewed`, fill `reviewer` and
   `last_reviewed`, and update the review-status table in `README.md`.
5. **Verify the 🔎 numbers** against the manuals used in this lab — highest value per hour. Start
   with 05 PCR, 08 qPCR, 16 MALDI-TOF.
6. **Decide what to do with `/data/Molecular_Data_Analysis/`** (separate GitHub repo?) — still local
   and uncommitted; ask the user.
7. Optional: decide whether the `restructure` branch can be deleted locally and on the remote.
