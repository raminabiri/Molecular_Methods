# PROGRESS

## 1. Current goal
Rebuild the whole repo as a Persian bench reference with **18 topics**, each with the same 6 files:
`01_Theory.md` (incl. chemistry + instrument engineering), `02_Protocol.md` (beginner-level, step by step),
`03_Troubleshooting.md` (expert level), `04_Assessment.md`, `05_Answers.md`, `06_Reference_Tables.md`.
Work happens on branch **`restructure`**; `main` keeps the old content untouched until everything is done.

## 2. Done so far
- Branch `restructure` created; snapshot commit `f72871c` preserves all original files.
- Cleanup: duplicates, `.Rhistory`, `gemini-code-*` removed; `.gitignore` added.
- qPCR data-analysis files moved OUT of this repo to `/data/Molecular_Data_Analysis/qPCR/` (local only, no git commit there yet).
- **Topics 01–15 complete** (01–14 pushed; 15 committed locally as `46f2b8a`):
  01 Lab basics/buffers (central formula sheet) · 02 DNA extraction · 03 RNA · 04 Protein ·
  05 Standard PCR · 06 Multiplex/gradient/touchdown · 07 LAMP+RPA · 08 Real-Time qPCR ·
  09 Agarose gel · 10 Southern/Northern · 11 Western+SDS-PAGE · 12 Sanger · 13 NGS (+microarray section) ·
  14 Prokaryotic cloning/plasmids · 15 Eukaryotic cloning/transfection/viral vectors.
- 2026-10-14: topic 15 finished (`05_Answers.md`, `06_Reference_Tables.md` written; the 5 old files in that folder `git rm`-ed) and committed.
- 2026-10-14: **topic 14 expanded on user request** (uncommitted at time of writing — see section 3):
  full vector taxonomy (cloning/expression/shuttle/broad-host-range/suicide/phage/phagemid/cosmid/fosmid/BAC/PAC/YAC/
  reporter/IVT/Gateway/mobilizable), expression-system table (pET, pBAD, pGEX, pMAL, pQE, pCold, pETDuet),
  shuttle vectors in depth (episomal vs integrative), and a complete cloning-methods section
  (TA, A-tailing, TOPO + directional TOPO, blunt, Gibson/HiFi, LIC, SLIC, CPEC, RF, USER, LCR,
  Golden Gate/MoClo, Gateway BP/LR, λ Red recombineering, whole-plasmid mutagenesis, direct synthesis)
  with mechanism, applications, differences and a "which method when" decision table.
  Also: 3 new protocols (TA/TOPO, Gibson, Golden Gate), troubleshooting for each method,
  13 new assessment questions + worked answers, 4 new reference tables, 10 new references.
- 2026-10-15: **topic 16 written** — `16_Microbial_Identification_MALDI-TOF/`, all 6 files.
  Structure agreed with the user: theory is platform-neutral (MALDI physics + instrument
  engineering: matrix chemistry, t ∝ √(m/z), delayed extraction, reflectron, vacuum, detector);
  the step-by-step protocol is anchored to **Bruker Biotyper** (direct smear, on-target formic
  acid, full ethanol/formic acid extraction, HCCA matrix, BTS calibrator, target cleaning) with a
  separate **VITEK MS differences** section; troubleshooting and tables cover **both** platforms,
  including the warning that Bruker log(score) and VITEK MS confidence % are not interconvertible.
  **16S rRNA identification is included in this topic** (27F/1492R, Sanger, identity/coverage
  thresholds, when 16S is insufficient → rpoB/hsp65/ITS/WGS), per the earlier decision.

## 3. Files changed
- New folders `01_…` to `15_…`, 6 files each (15 now complete).
- Topic 14: all 6 files edited for the vector/cloning-method expansion. Heading numbering inside
  `01_Theory.md` uses `۲.۳`–`۲.۹` and `۴.الف…` so that existing section numbers (3, 4, 5…) and any
  cross-references to them stay valid — do not renumber.
- Deleted old folders after merging their usable content: `01_DNA_Extraction`, `02_RNA_…`, `03_Protein_…`,
  `04_Standard_PCR`, `05_Multiplex_…`, `06_Isothermal_…`, `07_RealTime_qPCR`, `08_Agarose_…`,
  `09_Southern_…`, `10_Western_…`, `11_DNA_Microarray_Technology`, `13_NGS` old files, `14_…` old files.
- Still old/untouched: `15_Eukaryotic_Cloning_and_Vectors` old files (`01_Protocol.md`, `01-Theory_Eukaryotic_Cloning.md`,
  `02_Assessment.md`, `03_Answers.md`, `04_Standard_Tables.md`), `16_Molecular_Typing_ERIC`,
  `17_Molecular_Typing_MLST`, `18_Molecular_Typing_PFGE_MLST_ERIC`, `19_CRISPR_Cas_Editing_and_Diagnostics`.
- `PROGRESS.md`, `.gitignore`.

## 4. Key decisions and rejected approaches
| Decision | Reason |
| :--- | :--- |
| One root README only, no per-folder README | user's call; avoids duplicated, drifting text |
| 6-file template + YAML header (`status`/`reviewer`/`last_reviewed`) | makes peer review traceable before going public |
| Protocols written for someone who has never been in a lab | user has not personally run several of these methods |
| Protocols anchored to a named kit + 🔎 marks on numbers to verify | kit versions change; prevents silently wrong volumes |
| Computational analysis moved out of the repo | user wants wet-lab only; bench QC/interpretation stays |
| Microarray gets a section inside NGS, **no own folder** | superseded by RNA-seq; still used for SNP arrays/CMA only |
| MALDI-TOF added as its own topic (16) before typing | standard ID method today; fits the microbiology focus |
| 16/17/18 merged into one `17_Molecular_Typing` with subfolders | ERIC/MLST/PFGE/VNTR/spoligotyping are one family |
| Final count 18 topics (not 19) | after dropping the microarray folder — earlier chat said 19 |
| Rejected: keeping the old per-file numbering (`01_Protocol`, `04_Standard_Tables`) | inconsistent across folders; no Theory/Troubleshooting split |
| Rejected: fabricated YouTube/JoVE links from the old files | unverifiable; replaced with books, DOIs, official manuals |
| Rejected: merging into `main` now | user chose to merge only after all 18 topics are finished |

## 5. Known bugs / corrections made
No build or runtime errors (documentation repo). Scientific errors found in the **old** content and fixed in the rewrite:
- Old `04_Standard_PCR/03_pcr_exercises_and_answer_key.md` Q7: primer `ATGCGATCGATCGATCGATC` was described as 40% GC with A=4,T=4,G=6,C=6 → it is **5 of each base, 50% GC**, Wallace Tm = **60 °C** (answer said 64 °C).
- Same file, answer 18: genome copies in 10 ng of a 4.5 Mb genome → **≈2.06×10⁶**, not 2.06×10⁹ (mass written as 4.85×10⁻⁹ ng instead of ≈4.86×10⁻⁶ ng).
- Same file, answer 15: 1.85⁵ = **21.7×**, not 22.9×.
- Old Bio-Rad text: gradient described across 12 columns; on T100/C1000 the gradient runs across **rows** → flagged "verify on your instrument".
- Retracted earlier suspicion: `E = 10^slope` in the LinRegPCR sections is **correct** (slope of log₁₀F vs cycle); a clarifying note was added in the analysis repo.

## 5.1. Blocked: cannot push
`origin/restructure` is stuck at `16f637e`; the local branch is ahead by the topic 14/15/16 commits.
This environment has **no usable GitHub credentials**: no `credential.helper`, no `~/.git-credentials`,
and `gh auth status` returns "Timeout trying to log in to github.com account raminabiri (keyring)".
A `git push` therefore hangs waiting for a username/token. The user must run `gh auth login`
(or configure a credential helper / PAT) once in their own terminal; then push.
Consequence: **scheduled cloud routines are useless until this is fixed**, because a cloud agent
clones the GitHub repo and would not see topics 14-expansion, 15 or 16.

## 6. Next steps (priority order, one session each)
1. ~~Finish topic 15~~ **done** (`46f2b8a`). Push `restructure` when the user is ready.
2. ~~Topic 16 MALDI-TOF~~ **done** (6 files, 2026-10-15). Platform decision: **Bruker** anchors the
   protocol (larger installed base, local MSP libraries, resistance/typing applications);
   VITEK MS covered as a differences section. README must still say this is **protein MS**.
3. Topic 17 `17_Molecular_Typing` with subfolders `ERIC_rep-PCR`, `MLST`, `PFGE`, `VNTR_MLVA` (incl. MIRU-VNTR 24-locus), `Spoligotyping`, each with the 6 files + a short WGS-typing (cgMLST/SNP) note. MTB work starts from heat-inactivated DNA (BSL-3 warning). Then delete folders 16/17/18 old.
4. Topic 18 `18_CRISPR_Cas` (6 files) from old `19_CRISPR_Cas_Editing_and_Diagnostics`; then delete that folder.
5. Rewrite root `README.md`: 18 topics, the 6-file template, how to use, review status table, license placeholder (**ask user which license**).
6. Grep and fix stale cross-references (`grep -rn "فصل ۱[۵-۹]"`) after the final renumbering; check every relative link resolves.
7. Decide what to do with `/data/Molecular_Data_Analysis/` (separate GitHub repo?) and ask the user.
8. Merge `restructure` → `main` (user approved only at the end), then invite the peer reviewers.
