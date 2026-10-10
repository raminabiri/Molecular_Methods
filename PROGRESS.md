# PROGRESS

## Done
- 2026-10-09: Full repo review (structure + spot-check of calculations). No content files changed.

## Decisions (2026-10-09, user)
- One README for the whole repo only — no per-folder README.
- New first section: buffers/solutions & lab calculations, before DNA extraction (renumber all folders).
- Merge 16–18 into one Molecular Typing folder; English-only filenames.
- Repo will go public on GitHub; peer review by a few colleagues.
- Per-folder architecture APPROVED: 01_Theory, 02_Protocol, 03_Troubleshooting, 04_Assessment, 05_Answers, 06_Reference_Tables, figures/.
- Protocols: extremely detailed, written for someone who has never been in a lab (kit handling, ice, g + rpm). NGS must be exact.
- Scope: no computational data analysis (qPCR software analysis, NGS bioinformatics) — move to separate place; bench QC/interpretation stays.
- Troubleshooting: fully expert level (senior molecular lab supervisor).
- Microarray: no own folder — short theory/comparison section inside NGS chapter.
- MALDI-TOF added as 17_Microbial_Identification_MALDI-TOF (+16S ID), before 18_Molecular_Typing (ERIC/MLST/PFGE); 19_CRISPR_Cas last. Pick one platform (Bruker or VITEK MS); note in README it is protein MS.
- Theory files must explain instrument engineering (thermocycler: Peltier, block uniformity, heated lid, ramp rate; qPCR: optics, excitation/filters, detectors, ROX) and instrument chemistry where relevant (e.g. NGS SBS, nanopore, SMRT).
- The examples given are NOT exhaustive: in every topic, explain chemistry wherever relevant and briefly explain instrument engineering wherever interesting (any instrument used).
- PROPOSED (awaiting OK): 18_Molecular_Typing subfolders = ERIC_rep-PCR, MLST, PFGE, VNTR_MLVA (incl. MIRU-VNTR 24-loci), Spoligotyping (+ short theory note on WGS typing cgMLST/SNP). MTB = BSL-3 → work from heat-inactivated DNA.

## Next steps
1. Clean up: delete duplicates/stray files (`01_Protocol (Copy).md`, `06/01_Basics_md.md`, `08/آنالیز.md`, all `gemini-code-*`, `.Rhistory`), add `.gitignore`.
2. Move misplaced content: `08/theory.md` (qPCR) → 07; `08/01-Theory_Western_Northern_bloting.md` (Southern/Northern) → 09.
3. Unify per-folder naming to the approved architecture (see Decisions); renumber with 01_Lab_Basics_Buffers_and_Calculations first.
4. Merge/split 16–18 (ERIC / MLST / PFGE) — 18 name still says PFGE_MLST_ERIC; update root README (says 17 folders).
5. Fill empty topics: 09, 11, 10/01_Protocol, 13/01_Protocol, 18 placeholders.
6. Fix truncated files (unclosed `<details>`): 10/تیوری.md, 13/فتیوری-code-*, 12/01_Protocol.md, 15/01-Theory…, 10/gemini-code-کاربرد.md.

## Bugs (scientific errors found)
- (Retracted) E = 10^slope in LinRegPCR sections is CORRECT (slope of log10 F vs cycle = amplification factor). Clarifying note added in analysis repo.
- `04/03_pcr_exercises_and_answer_key.md` Q7: primer ATGCGATCGATCGATCGATC is A=T=G=C=5 (50% GC) → Wallace Tm = 60 °C (question says 40% GC, answer says 60% GC and 64 °C).
- Same file, answer 18: genome mass = 4.86e-15 g = 4.86e-6 ng (not e-9 ng); copies in 10 ng ≈ 2.06e6 (not 2.06e9).
