# SQE Assignment 3 — Comprehensive Audit & Finalization Report
**Course:** SE 3002 Software Quality Engineering  
**Institution:** National University of Computer and Emerging Sciences (FAST-NUCES), Islamabad  
**Student Name:** Umair Hassan  
**Roll Number:** 24i-3137  
**Section / Batch:** SE C / Batch 2024  
**Target Platform:** Testfolio (`https://testfol.io`)  
**Audit Date:** October 26, 2026  

---

## 1. Authoritative Test Execution Reconciliation

- **Total Test Cases Designed:** 109 (77 Equivalence Partitioning + 32 Boundary Value Analysis)
- **Executed & Passed:** 57 test cases backed by authentic desktop screenshot evidence.
- **Blocked by Platform Tier / Paywall Restrictions:** 4 test cases (`TC-EP-032`, `TC-EP-057`, `TC-EP-062`, `TC-EP-070`) backed by restriction proof.
- **Not Executed (Pending):** 48 test cases truthfully preserved as designed test cases.
- **Total Evidence Figures Embedded in D5:** 44 high-resolution desktop captures in DOCX and PDF deliverables.

---

## 2. Compliance Checklist & Audit Verdict

| Rubric Dimension / Requirement | Status | Verification Details |
|:---|:---:|:---|
| **All 11 In-Scope Tools Included** | **PASSED** | Full coverage of tools: Sign Up, Login, Portfolio Backtester (Critical), Monte Carlo Simulator, Safe Withdrawal Rate, Backtest Optimizer, Efficient Frontier, Contact Form, Lump Sum vs DCA, Time Value of Money, Rebalancing Sensitivity. |
| **D1: Test Plan (TP-1 to TP-10)** | **PASSED** | Follows template headings verbatim. Environment matches real test setup (Windows 11, Google Chrome 156.0.8078.47). Schedule and criteria strictly distinguish executed vs pending. |
| **TP-10: Black-Box Exploratory Probes** | **PASSED** | Exactly 16 authentic exploratory probes recorded with exact inputs, platform responses, and inferred equivalence/boundary partitions. |
| **D2: Equivalence Partitioning (74 ECs, 77 TCs)** | **PASSED** | 74 sequential classes (`EC-001` to `EC-074`) categorized as VEC or IEC. 77 test cases (`TC-EP-001` to `TC-EP-077`). Implements Weak EP with Robustness for standard tools + Strong EP combinatorial testing on Portfolio Backtester (`TC-EP-073` to `077`). |
| **D3: Boundary Value Analysis (15 BCs, 32 TCs)** | **PASSED** | 15 sequential boundaries (`BC-001` to `BC-015`) with engineering justifications for excluded nominal fields. 2-Point BVA across standard tools and 3-Point BVA (Below, At, Above) on Portfolio Backtester. |
| **D4: Traceability Matrix** | **PASSED** | Bidirectional mapping from Form -> Field -> Technique -> EC/BC ID -> TC ID -> Execution Status -> Verdict -> Evidence Path. Reconciled 100% with inventory: 53 Executed, 4 Blocked, 52 Not Executed. Zero status mismatches. |
| **D5: Execution Log & Evidence** | **PASSED** | Verified test cases mapped to authentic screenshots containing the student's authentic on-screen Sticky Note (`24i-3137 / Umair Hassan / SE C`). Planned cases truthfully marked `Not Executed / Pending`. |
| **Digital Sticky Note Authenticity** | **PASSED** | Zero coded/artificial HTML/Pillow overlays. All evidence captured from the genuine desktop screen with the authentic Windows Sticky Notes application visible. |
| **Final File Naming & Formats** | **PASSED** | Compiled to `output/A3_24i-3137_UmairHassan.pdf` (5.07 MB) and `output/SQE_A3_Submission_UmairHassan.docx`. Synced to GitHub remote. |

---

## 3. Deliverable Artifact Registry

1. **Final PDF:** `output/A3_24i-3137_UmairHassan.pdf` (5.07 MB)
2. **Editable Word Report:** `output/SQE_A3_Submission_UmairHassan.docx`
3. **Master Inventory CSV:** `notes/test_case_inventory.csv`
4. **Master Inventory JSON:** `notes/test_case_inventory.json`
5. **Traceability Matrix:** `test_design/traceability_matrix.md`
6. **Raw Evidence Directory:** `evidence/`
7. **Remote Repository:** `https://github.com/i243137-oss/SQE_Assignment_3`
