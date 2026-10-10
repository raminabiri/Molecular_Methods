# PROGRESS

## Done
- 2026-10-09: Full repo review (structure + spot-check of calculations).
- 2026-10-10: Restructure on branch `restructure` (snapshot commit f72871c keeps all old content).
  - Cleanup: duplicates, .Rhistory removed; .gitignore added.
  - qPCR data-analysis files moved OUT to `/data/Molecular_Data_Analysis/qPCR/` (separate local git repo, uncommitted).
  - Topics rewritten (6 files each, old folders deleted): 01 Lab basics, 02 DNA, 03 RNA, 04 Protein, 05 Standard PCR, 06 Multiplex/Gradient, 07 LAMP/RPA.

## Decisions (user)
- One README for the whole repo only — no per-folder README.
- Per-folder files: 01_Theory, 02_Protocol, 03_Troubleshooting, 04_Assessment, 05_Answers, 06_Reference_Tables (+ figures/ when needed). YAML header (status/reviewer/last_reviewed) on every file. English-only filenames.
- Protocols: extremely detailed, for someone never in a lab (kit handling, ice, g + rpm). Kit-anchored with "check your kit manual" flags. NGS must be exact.
- Troubleshooting: expert level (senior lab supervisor).
- Theory: explain chemistry and instrument engineering wherever relevant (examples not exhaustive).
- Scope: no computational data analysis (moved out); bench QC/interpretation stays.
- Microarray: no folder — short section inside NGS chapter.
- Molecular typing: one folder with subfolders ERIC_rep-PCR, MLST, PFGE, VNTR_MLVA (incl. MIRU-VNTR), Spoligotyping (+ short WGS-typing note). MTB = BSL-3.
- MALDI-TOF chapter before typing; pick one platform; note it is protein MS.
- Repo goes public on GitHub; peer review by colleagues.
- Central formula sheet = 01_Lab_Basics/06_Reference_Tables.md.
- No fabricated links: only books / DOIs / official manuals.

## Final numbering (18 topics)
01 Lab_Basics_Buffers_and_Calculations ✔ | 02 DNA_Extraction ✔ | 03 RNA_Extraction_and_Handling ✔ | 04 Protein_Extraction_and_Quantification ✔ | 05 Standard_PCR ✔ | 06 Multiplex_and_Gradient_PCR ✔ | 07 Isothermal_Amplification_LAMP ✔ | 08 RealTime_qPCR | 09 Agarose_Gel_Electrophoresis | 10 Southern_and_Northern_Blotting | 11 Western_Blotting | 12 Sanger_Sequencing | 13 NGS (+ microarray) | 14 Prokaryotic_Cloning_and_Plasmids | 15 Eukaryotic_Cloning_and_Vectors | 16 Microbial_Identification_MALDI-TOF | 17 Molecular_Typing | 18 CRISPR_Cas
- Earlier chat listed MALDI=17/Typing=18/CRISPR=19; correct after dropping microarray is 16/17/18 → tell user.
- Some written files cross-reference old numbers (e.g. "فصل ۱۹" for CRISPR, "فصل ۱۸" for typing, "فصل ۱۵" for cloning, "فصل ۱۶" MALDI). Fix all at the end with grep.

## Next steps
1. Write topics 08–18. Old folders to merge then delete: 07_RealTime_qPCR→08; 08_Agarose→09 (its Southern/Northern theory file → 10); 09_Southern→10; 10_Western→11; 11_Microarray→13; 12_Sanger→12; 13_NGS→13; 14→14; 15→15; 16/17/18 typing→17; 19_CRISPR→18.
2. Rewrite root README.
3. Grep and fix cross-references.
4. Ask user before push / merge; ask which license.

## Bugs fixed (scientific errors in old content)
- PCR exercises: Tm question (primer is 50% GC → Wallace 60°C); genome copies in 10 ng (2.06e6, not 2.06e9); 1.85^5 = 21.7 (not 22.9); ΔTm 14°C answer was wrong.
- Old Bio-Rad text: gradient across 12 columns; Bio-Rad T100/C1000 gradient is across rows (flagged "verify on instrument").
- Old YouTube/JoVE links looked fabricated → removed.
- (Retracted) E = 10^slope in LinRegPCR sections is CORRECT.
