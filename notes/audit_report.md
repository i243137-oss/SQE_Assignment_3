# SQE Assignment 3 — Comprehensive Audit & Finalization Report
**Course:** SE 3002 Software Quality Engineering  
**Institution:** National University of Computer and Emerging Sciences (FAST-NUCES), Islamabad  
**Student Name:** Umair Hassan  
**Roll Number:** 24i-3137  
**Section / Batch:** SE C / Batch 2024  
**Target Platform:** Testfolio (`https://testfol.io`)  
**Audit Date:** October 26, 2026  

---

## 1. Compliance Checklist & Audit Verdict

| Rubric Dimension / Requirement | Status | Verification Details |
|:---|:---:|:---|
| **All 11 In-Scope Tools Included** | **PASSED** | Full coverage of tools: Sign Up, Login, Portfolio Backtester (Critical), Monte Carlo Simulator, Safe Withdrawal Rate, Backtest Optimizer, Efficient Frontier, Contact Form, Lump Sum vs DCA, Time Value of Money, Rebalancing Sensitivity. |
| **D1: Test Plan (TP-1 to TP-10)** | **PASSED** | Follows template headings verbatim. Environment matches real test setup (Windows 11, Google Chrome 156.0.8078.47). Schedule and criteria strictly distinguish executed vs pending. |
| **TP-10: Black-Box Exploratory Probes** | **PASSED** | Exactly 16 authentic exploratory probes recorded with exact inputs, platform responses, and inferred equivalence/boundary partitions. |
| **D2: Equivalence Partitioning (74 ECs, 77 TCs)** | **PASSED** | 74 sequential classes (`EC-001` to `EC-074`) categorized as VEC or IEC. 77 test cases (`TC-EP-001` to `TC-EP-077`). Implements Weak EP with Robustness for standard tools + Strong EP combinatorial testing on Portfolio Backtester (`TC-EP-073` to `077`). |
| **D3: Boundary Value Analysis (15 BCs, 32 TCs)** | **PASSED** | 15 sequential boundaries (`BC-001` to `BC-015`) with engineering justifications for excluded nominal fields. 2-Point BVA across standard tools and 3-Point BVA (Below, At, Above) on Portfolio Backtester. |
| **D4: Traceability Matrix** | **PASSED** | Bidirectional mapping from Form $\rightarrow$ Field $\rightarrow$ Technique $\rightarrow$ EC/BC ID $\rightarrow$ TC ID $\rightarrow$ Execution Status $\rightarrow$ Verdict $\rightarrow$ Evidence Path. Zero orphan IDs. |
| **D5: Execution Log & Evidence** | **PASSED** | 33 executed test cases mapped to authentic screenshots containing the student's authentic on-screen Sticky Note (`24i-3137 / Umair Hassan / SE C`). 76 planned cases truthfully marked `Not Executed / Pending`. |
| **Digital Sticky Note Authenticity** | **PASSED** | Zero coded/artificial HTML/Pillow overlays. All evidence captured from the genuine desktop screen with the authentic Windows Sticky Notes application visible. |
| **Final File Naming & Formats** | **PASSED** | Compiled to `output/A3_24i-3137_UmairHassan.pdf` (5.07 MB) and `output/SQE_A3_Submission_UmairHassan.docx`. Synced to GitHub remote. |

---

## 2. Test Execution Inventory Breakdown

- **Total Test Cases Designed:** 109
  - **Equivalence Partitioning Cases:** 77 (`TC-EP-001` to `TC-EP-077`)
  - **Boundary Value Analysis Cases:** 32 (`TC-BVA-001` to `TC-BVA-032`)
- **Execution Status Breakdown:**
  - **Executed (Pass):** 33 test cases
  - **Not Executed (Pending):** 76 test cases (strictly retained as designed cases without false pass claims)
  - **Blocked / Inconclusive:** 0
- **Total Authentic Embedded Figures:** 44 high-resolution desktop captures in DOCX and PDF deliverables.

---

## 3. Deliverable Artifact Registry

1. **Final PDF:** [`output/A3_24i-3137_UmairHassan.pdf`](file:///c:/Users/uh723/Downloads/Assignment_3/output/A3_24i-3137_UmairHassan.pdf) (5.07 MB)
2. **Editable Word Report:** [`output/SQE_A3_Submission_UmairHassan.docx`](file:///c:/Users/uh723/Downloads/Assignment_3/output/SQE_A3_Submission_UmairHassan.docx)
3. **Master Inventory CSV:** [`notes/test_case_inventory.csv`](file:///c:/Users/uh723/Downloads/Assignment_3/notes/test_case_inventory.csv)
4. **Master Inventory JSON:** [`notes/test_case_inventory.json`](file:///c:/Users/uh723/Downloads/Assignment_3/notes/test_case_inventory.json)
5. **Traceability Matrix:** [`test_design/traceability_matrix.md`](file:///c:/Users/uh723/Downloads/Assignment_3/test_design/traceability_matrix.md)
6. **Raw Evidence Directory:** [`evidence/`](file:///c:/Users/uh723/Downloads/Assignment_3/evidence/)
7. **Remote Repository:** `https://github.com/i243137-oss/SQE_Assignment_3`
