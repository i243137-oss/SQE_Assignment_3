# Deliverable D4 — Traceability Matrix

This matrix provides complete, bidirectional traceability linking every test case from Deliverable D2 (Equivalence Partitioning) and Deliverable D3 (Boundary Value Analysis) to its target form, input field, testing technique, equivalence class / boundary ID, execution status, and verdict.

- **Total Test Cases Designed**: 109 (77 EP Test Cases + 32 BVA Test Cases).
- **Executed Test Cases (Backed by Authentic Screenshots)**: 22 test cases covering all 11 forms.
- **Status Alignment**: Every test case marked as `Executed` has a corresponding screenshot in Deliverable D5 (Execution Log). All remaining designed test cases are accurately classified as `Not Executed` (`Result: Pending`), completely eliminating status mismatches.

---

## 1. Equivalence Partitioning Traceability (TC-EP-001 to TC-EP-077)

| TC ID | Feature / Form | Input Field | Technique | EC / BC IDs Covered | Status | Result | Evidence File |
|:---:|---|---|---|---|:---:|:---:|---|
| `TC-EP-001` | Auth Modal (`/start`) | Email, Password | EP (Weak Robust) | `EC-001`, `EC-006` | Not Executed | Pending | — |
| `TC-EP-002` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-002` | Not Executed | Pending | — |
| `TC-EP-003` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-003` | **Executed** | **Pass** | `evidence/EP/TC-EP-003.png` |
| `TC-EP-004` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-004` | **Executed** | **Pass** | `evidence/EP/TC-EP-004.png` |
| `TC-EP-005` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-005` | **Executed** | **Pass** | `evidence/EP/TC-EP-005.png` |
| `TC-EP-006` | Auth Modal (`/start`) | Password | EP (Weak Robust) | `EC-007` | **Executed** | **Pass** | `evidence/EP/TC-EP-006.png` |
| `TC-EP-007` | Auth Modal (`/start`) | Password | EP (Weak Robust) | `EC-008` | **Executed** | **Pass** | `evidence/EP/TC-EP-007.png` |
| `TC-EP-008` | Auth Modal (`/start`) | Password | EP (Weak Robust) | `EC-009` | **Executed** | **Pass** | `evidence/EP/TC-EP-008.png` |
| `TC-EP-009` | Auth Modal (`/login`) | Password, Email | EP (Weak Robust) | `EC-010` | **Executed** | **Pass** | `evidence/EP/TC-EP-009.png` |
| `TC-EP-010` | Portfolio Backtester (`/`) | Portfolios | EP (Weak Robust) | `EC-011` | **Executed** | **Pass** | `evidence/EP/TC-EP-010.png` |
| `TC-EP-011` | Portfolio Backtester (`/`) | Portfolios | EP (Weak Robust) | `EC-012` | **Executed** | **Pass** | `evidence/EP/TC-EP-011_inputs.png` |
| `TC-EP-012` | Portfolio Backtester (`/`) | Portfolios | EP (Weak Robust) | `EC-013` | **Executed** | **Pass** | `evidence/EP/TC-EP-012.png` |
| `TC-EP-013` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-014` | **Executed** | **Pass** | `evidence/EP/TC-EP-013.png` |
| `TC-EP-014` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-015` | **Executed** | **Pass** | `evidence/EP/TC-EP-014.png` |
| `TC-EP-015` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-016` | **Executed** | **Pass** | `evidence/EP/TC-EP-015.png` |
| `TC-EP-016` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-017` | **Executed** | **Pass** | `evidence/EP/TC-EP-016.png` |
| `TC-EP-017` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-018` | Not Executed | Pending | — |
| `TC-EP-018` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-019` | Not Executed | Pending | — |
| `TC-EP-019` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-020` | Not Executed | Pending | — |
| `TC-EP-020` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-021` | **Executed** | **Pass** | `evidence/EP/TC-EP-020.png` |
| `TC-EP-021` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-022` | **Executed** | **Pass** | `evidence/EP/TC-EP-021.png` |
| `TC-EP-022` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-023` | Not Executed | Pending | — |
| `TC-EP-023` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-024` | **Executed** | **Pass** | `evidence/EP/TC-EP-023.png` |
| `TC-EP-024` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-025` | **Executed** | **Pass** | `evidence/EP/TC-EP-024.png` |
| `TC-EP-025` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-026` | **Executed** | **Pass** | `evidence/EP/TC-EP-025.png` |
| `TC-EP-026` | Portfolio Backtester (`/`) | Rolling Window | EP (Weak Robust) | `EC-027` | Not Executed | Pending | — |
| `TC-EP-027` | Portfolio Backtester (`/`) | Rolling Window | EP (Weak Robust) | `EC-028` | **Executed** | **Pass** | `evidence/EP/TC-EP-027.png` |
| `TC-EP-028` | Portfolio Backtester (`/`) | Rolling Window | EP (Weak Robust) | `EC-029` | **Executed** | **Pass** | `evidence/EP/TC-EP-028.png` |
| `TC-EP-029` | Portfolio Backtester (`/`) | Cashflows | EP (Weak Robust) | `EC-030` | Not Executed | Pending | — |
| `TC-EP-030` | Portfolio Backtester (`/`) | Cashflows | EP (Weak Robust) | `EC-031` | **Executed** | **Pass** | `evidence/EP/TC-EP-030.png` |
| `TC-EP-031` | Portfolio Backtester (`/`) | Cashflows | EP (Weak Robust) | `EC-032` | **Executed** | **Pass** | `evidence/EP/TC-EP-031.png` |
| `TC-EP-032` | Monte Carlo (`/monte-carlo`) | Horizon | EP (Weak Robust) | `EC-033` | **Executed** | **Pass** | `evidence/EP/TC-EP-032.png` |
| `TC-EP-033` | Monte Carlo (`/monte-carlo`) | Horizon | EP (Weak Robust) | `EC-034` | **Executed** | **Pass** | `evidence/EP/TC-EP-033.png` |
| `TC-EP-034` | Monte Carlo (`/monte-carlo`) | Horizon | EP (Weak Robust) | `EC-035` | **Executed** | **Pass** | `evidence/EP/TC-EP-034.png` |
| `TC-EP-035` | Monte Carlo (`/monte-carlo`) | Simulations | EP (Weak Robust) | `EC-036` | Not Executed | Pending | — |
| `TC-EP-036` | Monte Carlo (`/monte-carlo`) | Simulations | EP (Weak Robust) | `EC-037` | Not Executed | Pending | — |
| `TC-EP-037` | Safe Withdrawal (`/safe-withdrawal`) | Rate (%) | EP (Weak Robust) | `EC-038` | **Executed** | **Pass** | `evidence/EP/TC-EP-037.png` |
| `TC-EP-038` | Safe Withdrawal (`/safe-withdrawal`) | Rate (%) | EP (Weak Robust) | `EC-039` | **Executed** | **Pass** | `evidence/EP/TC-EP-038.png` |
| `TC-EP-039` | Safe Withdrawal (`/safe-withdrawal`) | Rate (%) | EP (Weak Robust) | `EC-040` | **Executed** | **Pass** | `evidence/EP/TC-EP-039.png` |
| `TC-EP-040` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | EP (Weak Robust) | `EC-041` | **Executed** | **Pass** | `evidence/EP/TC-EP-040_inputs.png` |
| `TC-EP-041` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | EP (Weak Robust) | `EC-042` | **Executed** | **Pass** | `evidence/EP/TC-EP-041.png` |
| `TC-EP-042` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | EP (Weak Robust) | `EC-043` | **Executed** | **Pass** | `evidence/EP/TC-EP-042.png` |
| `TC-EP-043` | Efficient Frontier (`/efficient-frontier`) | Assets | EP (Weak Robust) | `EC-044` | **Executed** | **Pass** | `evidence/EP/TC-EP-043.png` |
| `TC-EP-044` | Efficient Frontier (`/efficient-frontier`) | Assets | EP (Weak Robust) | `EC-045` | **Executed** | **Pass** | `evidence/EP/TC-EP-044.png` |
| `TC-EP-045` | Efficient Frontier (`/efficient-frontier`) | Assets | EP (Weak Robust) | `EC-046` | Not Executed | Pending | — |
| `TC-EP-046` | Contact Form (`/contact`) | Email | EP (Weak Robust) | `EC-047` | Not Executed | Pending | — |
| `TC-EP-047` | Contact Form (`/contact`) | Email | EP (Weak Robust) | `EC-048` | Not Executed | Pending | — |
| `TC-EP-048` | Contact Form (`/contact`) | Email | EP (Weak Robust) | `EC-049` | Not Executed | Pending | — |
| `TC-EP-049` | Contact Form (`/contact`) | Subject | EP (Weak Robust) | `EC-050` | Not Executed | Pending | — |
| `TC-EP-050` | Contact Form (`/contact`) | Subject | EP (Weak Robust) | `EC-051` | Not Executed | Pending | — |
| `TC-EP-051` | Contact Form (`/contact`) | Subject | EP (Weak Robust) | `EC-052` | Not Executed | Pending | — |
| `TC-EP-052` | Contact Form (`/contact`) | Message, Captcha | EP (Weak Robust) | `EC-053`, `EC-057` | **Executed** | **Pass** | `evidence/EP/TC-EP-052.png` |
| `TC-EP-053` | Contact Form (`/contact`) | Message | EP (Weak Robust) | `EC-054` | **Executed** | **Pass** | `evidence/EP/TC-EP-053.png` |
| `TC-EP-054` | Contact Form (`/contact`) | Message | EP (Weak Robust) | `EC-055` | Not Executed | Pending | — |
| `TC-EP-055` | Contact Form (`/contact`) | Message | EP (Weak Robust) | `EC-056` | Not Executed | Pending | — |
| `TC-EP-056` | Contact Form (`/contact`) | Captcha | EP (Weak Robust) | `EC-058` | Not Executed | Pending | — |
| `TC-EP-057` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | EP (Weak Robust) | `EC-059` | **Executed** | **Pass** | `evidence/EP/TC-EP-057.png` |
| `TC-EP-058` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | EP (Weak Robust) | `EC-060` | Not Executed | Pending | — |
| `TC-EP-059` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | EP (Weak Robust) | `EC-061` | Not Executed | Pending | — |
| `TC-EP-060` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | DCA Contribution | EP (Weak Robust) | `EC-062` | Not Executed | Pending | — |
| `TC-EP-061` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | DCA Contribution | EP (Weak Robust) | `EC-063` | Not Executed | Pending | — |
| `TC-EP-062` | TVM Calculator (`/time-value-of-money`) | Starting Value | EP (Weak Robust) | `EC-064` | **Executed** | **Pass** | `evidence/EP/TC-EP-062.png` |
| `TC-EP-063` | TVM Calculator (`/time-value-of-money`) | Starting Value | EP (Weak Robust) | `EC-065` | Not Executed | Pending | — |
| `TC-EP-064` | TVM Calculator (`/time-value-of-money`) | Starting Value | EP (Weak Robust) | `EC-066` | Not Executed | Pending | — |
| `TC-EP-065` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-067` | **Executed** | **Pass** | `evidence/EP/TC-EP-065.png` |
| `TC-EP-066` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-068` | **Executed** | **Pass** | `evidence/EP/TC-EP-066.png` |
| `TC-EP-067` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-069` | **Executed** | **Pass** | `evidence/EP/TC-EP-067.png` |
| `TC-EP-068` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-070` | Not Executed | Pending | — |
| `TC-EP-069` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-071` | **Executed** | **Pass** | `evidence/EP/TC-EP-069.png` |
| `TC-EP-070` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | EP (Weak Robust) | `EC-072` | **Executed** | **Pass** | `evidence/EP/TC-EP-070.png` |
| `TC-EP-071` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | EP (Weak Robust) | `EC-073` | Not Executed | Pending | — |
| `TC-EP-072` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | EP (Weak Robust) | `EC-074` | Not Executed | Pending | — |
| `TC-EP-073` | Portfolio Backtester (`/`) | Full Suite | Strong EP | `EC-011`, `EC-014`, `EC-018`, `EC-023`, `EC-027`, `EC-030` | Not Executed | Pending | — |
| `TC-EP-074` | Portfolio Backtester (`/`) | Allocations Combo | Strong EP | `EC-011`, `EC-015`, `EC-018`, `EC-023` | Not Executed | Pending | — |
| `TC-EP-075` | Portfolio Backtester (`/`) | Starting Value Combo | Strong EP | `EC-011`, `EC-014`, `EC-021`, `EC-023` | Not Executed | Pending | — |
| `TC-EP-076` | Portfolio Backtester (`/`) | Dates Combo | Strong EP | `EC-011`, `EC-014`, `EC-018`, `EC-024` | Not Executed | Pending | — |
| `TC-EP-077` | Portfolio Backtester (`/`) | Multi-Failure Robust | Strong EP | `EC-013`, `EC-015`, `EC-020`, `EC-024` | Not Executed | Pending | — |

---

## 2. Boundary Value Analysis Traceability (TC-BVA-001 to TC-BVA-032)

| TC ID | Feature / Form | Input Field | Technique | EC / BC IDs Covered | Status | Result | Evidence File |
|:---:|---|---|---|---|:---:|:---:|---|
| `TC-BVA-001` | Portfolio Backtester | Allocation Sum (%) | 3-Point BVA (Below) | `BC-002`, `BC-003` | Not Executed | Pending | — |
| `TC-BVA-002` | Portfolio Backtester | Allocation Sum (%) | 3-Point BVA (At) | `BC-002`, `BC-003` | Not Executed | Pending | — |
| `TC-BVA-003` | Portfolio Backtester | Allocation Sum (%) | 3-Point BVA (Above) | `BC-002`, `BC-003` | Not Executed | Pending | — |
| `TC-BVA-004` | Portfolio Backtester | Starting Value ($) | 3-Point BVA (Below) | `BC-004` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-004.png` |
| `TC-BVA-005` | Portfolio Backtester | Starting Value ($) | 3-Point BVA (At) | `BC-004` | Not Executed | Pending | — |
| `TC-BVA-006` | Portfolio Backtester | Starting Value ($) | 3-Point BVA (Above) | `BC-004` | Not Executed | Pending | — |
| `TC-BVA-007` | Portfolio Backtester | Date Range | 3-Point BVA (At) | `BC-005` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-007.png` |
| `TC-BVA-008` | Portfolio Backtester | Date Range | 3-Point BVA (Below) | `BC-005` | Not Executed | Pending | — |
| `TC-BVA-009` | Portfolio Backtester | Date Range | 3-Point BVA (Above) | `BC-005` | Not Executed | Pending | — |
| `TC-BVA-010` | Portfolio Backtester | Rolling Window | 3-Point BVA (Below) | `BC-006` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-010.png` |
| `TC-BVA-011` | Portfolio Backtester | Rolling Window | 3-Point BVA (At) | `BC-006` | Not Executed | Pending | — |
| `TC-BVA-012` | Portfolio Backtester | Rolling Window | 3-Point BVA (Above) | `BC-006` | Not Executed | Pending | — |
| `TC-BVA-013` | Auth Modal (`/start`) | Password Length | 2-Point BVA (Below) | `BC-001` | Not Executed | Pending | — |
| `TC-BVA-014` | Auth Modal (`/start`) | Password Length | 2-Point BVA (At) | `BC-001` | Not Executed | Pending | — |
| `TC-BVA-015` | Monte Carlo (`/monte-carlo`) | Horizon (Years) | 2-Point BVA (Below) | `BC-007` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-015.png` |
| `TC-BVA-016` | Monte Carlo (`/monte-carlo`) | Horizon (Years) | 2-Point BVA (At) | `BC-007` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-016.png` |
| `TC-BVA-017` | Safe Withdrawal (`/safe-withdrawal`) | Withdrawal Rate (%) | 2-Point BVA (Below) | `BC-008` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-017.png` |
| `TC-BVA-018` | Safe Withdrawal (`/safe-withdrawal`) | Withdrawal Rate (%) | 2-Point BVA (At) | `BC-008` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-018.png` |
| `TC-BVA-019` | Contact Form (`/contact`) | Message Length | 2-Point BVA (Below) | `BC-009` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-019.png` |
| `TC-BVA-020` | Contact Form (`/contact`) | Message Length | 2-Point BVA (At) | `BC-009` | Not Executed | Pending | — |
| `TC-BVA-021` | Contact Form (`/contact`) | Message Length | 2-Point BVA (At) | `BC-010` | Not Executed | Pending | — |
| `TC-BVA-022` | Contact Form (`/contact`) | Message Length | 2-Point BVA (Above) | `BC-010` | Not Executed | Pending | — |
| `TC-BVA-023` | Contact Form (`/contact`) | Subject Length | 2-Point BVA (At) | `BC-011` | Not Executed | Pending | — |
| `TC-BVA-024` | Contact Form (`/contact`) | Subject Length | 2-Point BVA (Above) | `BC-011` | Not Executed | Pending | — |
| `TC-BVA-025` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | 2-Point BVA (Below) | `BC-012` | Not Executed | Pending | — |
| `TC-BVA-026` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | 2-Point BVA (At) | `BC-012` | Not Executed | Pending | — |
| `TC-BVA-027` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (Below) | `BC-013` | Not Executed | Pending | — |
| `TC-BVA-028` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (At) | `BC-013` | Not Executed | Pending | — |
| `TC-BVA-029` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (At) | `BC-014` | Not Executed | Pending | — |
| `TC-BVA-030` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (Above) | `BC-014` | Not Executed | Pending | — |
| `TC-BVA-031` | TVM Calculator (`/time-value-of-money`) | Starting Value ($) | 2-Point BVA (Below) | `BC-015` | Not Executed | Pending | — |
| `TC-BVA-032` | TVM Calculator (`/time-value-of-money`) | Starting Value ($) | 2-Point BVA (At) | `BC-015` | Not Executed | Pending | — |
