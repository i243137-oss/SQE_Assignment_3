# Deliverable D4 — Traceability Matrix

This matrix provides complete, bidirectional traceability linking every test case from Deliverable D2 (Equivalence Partitioning) and Deliverable D3 (Boundary Value Analysis) to its target form, input field, testing technique, equivalence class / boundary ID, execution status, and verdict.

Total Test Cases Mapped: **109** (77 EP Test Cases + 32 BVA Test Cases).

---

## 1. Equivalence Partitioning Traceability (TC-EP-001 to TC-EP-077)

| TC ID | Feature / Form | Input Field | Technique | EC / BC IDs Covered | Status | Result |
|:---:|---|---|---|---|:---:|:---:|
| `TC-EP-001` | Auth Modal (`/start`) | Email, Password | EP (Weak Robust) | `EC-001`, `EC-006` | Executed | Pass |
| `TC-EP-002` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-002` | Executed | Pass |
| `TC-EP-003` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-003` | Executed | Pass |
| `TC-EP-004` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-004` | Executed | Pass |
| `TC-EP-005` | Auth Modal (`/start`) | Email | EP (Weak Robust) | `EC-005` | Executed | Pass |
| `TC-EP-006` | Auth Modal (`/start`) | Password | EP (Weak Robust) | `EC-007` | Executed | Pass |
| `TC-EP-007` | Auth Modal (`/start`) | Password | EP (Weak Robust) | `EC-008` | Executed | Pass |
| `TC-EP-008` | Auth Modal (`/start`) | Password | EP (Weak Robust) | `EC-009` | Executed | Pass |
| `TC-EP-009` | Auth Modal (`/login`) | Password, Email | EP (Weak Robust) | `EC-010` | Executed | Pass |
| `TC-EP-010` | Portfolio Backtester (`/`) | Portfolios | EP (Weak Robust) | `EC-011` | Executed | Pass |
| `TC-EP-011` | Portfolio Backtester (`/`) | Portfolios | EP (Weak Robust) | `EC-012` | Executed | Pass |
| `TC-EP-012` | Portfolio Backtester (`/`) | Portfolios | EP (Weak Robust) | `EC-013` | Executed | Pass |
| `TC-EP-013` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-014` | Executed | Pass |
| `TC-EP-014` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-015` | Executed | Pass |
| `TC-EP-015` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-016` | Executed | Pass |
| `TC-EP-016` | Portfolio Backtester (`/`) | Allocations | EP (Weak Robust) | `EC-017` | Executed | Pass |
| `TC-EP-017` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-018` | Executed | Pass |
| `TC-EP-018` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-019` | Executed | Pass |
| `TC-EP-019` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-020` | Executed | Pass |
| `TC-EP-020` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-021` | Executed | Pass |
| `TC-EP-021` | Portfolio Backtester (`/`) | Starting Value | EP (Weak Robust) | `EC-022` | Executed | Pass |
| `TC-EP-022` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-023` | Executed | Pass |
| `TC-EP-023` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-024` | Executed | Pass |
| `TC-EP-024` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-025` | Executed | Pass |
| `TC-EP-025` | Portfolio Backtester (`/`) | Dates | EP (Weak Robust) | `EC-026` | Executed | Pass |
| `TC-EP-026` | Portfolio Backtester (`/`) | Rolling Window | EP (Weak Robust) | `EC-027` | Executed | Pass |
| `TC-EP-027` | Portfolio Backtester (`/`) | Rolling Window | EP (Weak Robust) | `EC-028` | Executed | Pass |
| `TC-EP-028` | Portfolio Backtester (`/`) | Rolling Window | EP (Weak Robust) | `EC-029` | Executed | Pass |
| `TC-EP-029` | Portfolio Backtester (`/`) | Cashflows | EP (Weak Robust) | `EC-030` | Executed | Pass |
| `TC-EP-030` | Portfolio Backtester (`/`) | Cashflows | EP (Weak Robust) | `EC-031` | Executed | Pass |
| `TC-EP-031` | Portfolio Backtester (`/`) | Cashflows | EP (Weak Robust) | `EC-032` | Executed | Pass |
| `TC-EP-032` | Monte Carlo (`/monte-carlo`) | Horizon | EP (Weak Robust) | `EC-033` | Executed | Pass |
| `TC-EP-033` | Monte Carlo (`/monte-carlo`) | Horizon | EP (Weak Robust) | `EC-034` | Executed | Pass |
| `TC-EP-034` | Monte Carlo (`/monte-carlo`) | Horizon | EP (Weak Robust) | `EC-035` | Executed | Pass |
| `TC-EP-035` | Monte Carlo (`/monte-carlo`) | Simulations | EP (Weak Robust) | `EC-036` | Executed | Pass |
| `TC-EP-036` | Monte Carlo (`/monte-carlo`) | Simulations | EP (Weak Robust) | `EC-037` | Executed | Pass |
| `TC-EP-037` | Safe Withdrawal (`/safe-withdrawal`) | Rate (%) | EP (Weak Robust) | `EC-038` | Executed | Pass |
| `TC-EP-038` | Safe Withdrawal (`/safe-withdrawal`) | Rate (%) | EP (Weak Robust) | `EC-039` | Executed | Pass |
| `TC-EP-039` | Safe Withdrawal (`/safe-withdrawal`) | Rate (%) | EP (Weak Robust) | `EC-040` | Executed | Pass |
| `TC-EP-040` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | EP (Weak Robust) | `EC-041` | Executed | Pass |
| `TC-EP-041` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | EP (Weak Robust) | `EC-042` | Executed | Pass |
| `TC-EP-042` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | EP (Weak Robust) | `EC-043` | Executed | Pass |
| `TC-EP-043` | Efficient Frontier (`/efficient-frontier`) | Assets | EP (Weak Robust) | `EC-044` | Executed | Pass |
| `TC-EP-044` | Efficient Frontier (`/efficient-frontier`) | Assets | EP (Weak Robust) | `EC-045` | Executed | Pass |
| `TC-EP-045` | Efficient Frontier (`/efficient-frontier`) | Assets | EP (Weak Robust) | `EC-046` | Executed | Pass |
| `TC-EP-046` | Contact Form (`/contact`) | Email | EP (Weak Robust) | `EC-047` | Executed | Pass |
| `TC-EP-047` | Contact Form (`/contact`) | Email | EP (Weak Robust) | `EC-048` | Executed | Pass |
| `TC-EP-048` | Contact Form (`/contact`) | Email | EP (Weak Robust) | `EC-049` | Executed | Pass |
| `TC-EP-049` | Contact Form (`/contact`) | Subject | EP (Weak Robust) | `EC-050` | Executed | Pass |
| `TC-EP-050` | Contact Form (`/contact`) | Subject | EP (Weak Robust) | `EC-051` | Executed | Pass |
| `TC-EP-051` | Contact Form (`/contact`) | Subject | EP (Weak Robust) | `EC-052` | Executed | Pass |
| `TC-EP-052` | Contact Form (`/contact`) | Message, Captcha | EP (Weak Robust) | `EC-053`, `EC-057` | Executed | Pass |
| `TC-EP-053` | Contact Form (`/contact`) | Message | EP (Weak Robust) | `EC-054` | Executed | Pass |
| `TC-EP-054` | Contact Form (`/contact`) | Message | EP (Weak Robust) | `EC-055` | Executed | Pass |
| `TC-EP-055` | Contact Form (`/contact`) | Message | EP (Weak Robust) | `EC-056` | Executed | Pass |
| `TC-EP-056` | Contact Form (`/contact`) | Captcha | EP (Weak Robust) | `EC-058` | Executed | Pass |
| `TC-EP-057` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | EP (Weak Robust) | `EC-059` | Executed | Pass |
| `TC-EP-058` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | EP (Weak Robust) | `EC-060` | Executed | Pass |
| `TC-EP-059` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | EP (Weak Robust) | `EC-061` | Executed | Pass |
| `TC-EP-060` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | DCA Contribution | EP (Weak Robust) | `EC-062` | Executed | Pass |
| `TC-EP-061` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | DCA Contribution | EP (Weak Robust) | `EC-063` | Executed | Pass |
| `TC-EP-062` | TVM Calculator (`/time-value-of-money`) | Starting Value | EP (Weak Robust) | `EC-064` | Executed | Pass |
| `TC-EP-063` | TVM Calculator (`/time-value-of-money`) | Starting Value | EP (Weak Robust) | `EC-065` | Executed | Pass |
| `TC-EP-064` | TVM Calculator (`/time-value-of-money`) | Starting Value | EP (Weak Robust) | `EC-066` | Executed | Pass |
| `TC-EP-065` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-067` | Executed | Pass |
| `TC-EP-066` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-068` | Executed | Pass |
| `TC-EP-067` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-069` | Executed | Pass |
| `TC-EP-068` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-070` | Executed | Pass |
| `TC-EP-069` | TVM Calculator (`/time-value-of-money`) | Contribution | EP (Weak Robust) | `EC-071` | Executed | Pass |
| `TC-EP-070` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | EP (Weak Robust) | `EC-072` | Executed | Pass |
| `TC-EP-071` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | EP (Weak Robust) | `EC-073` | Executed | Pass |
| `TC-EP-072` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | EP (Weak Robust) | `EC-074` | Executed | Pass |
| `TC-EP-073` | Portfolio Backtester (`/`) | Full Suite (Multi-field) | Strong EP | `EC-011`, `EC-014`, `EC-018`, `EC-023`, `EC-027`, `EC-030` | Executed | Pass |
| `TC-EP-074` | Portfolio Backtester (`/`) | Allocations + Context | Strong EP | `EC-011`, `EC-015`, `EC-018`, `EC-023` | Executed | Pass |
| `TC-EP-075` | Portfolio Backtester (`/`) | Starting Value + Context | Strong EP | `EC-011`, `EC-014`, `EC-021`, `EC-023` | Executed | Pass |
| `TC-EP-076` | Portfolio Backtester (`/`) | Dates + Context | Strong EP | `EC-011`, `EC-014`, `EC-018`, `EC-024` | Executed | Pass |
| `TC-EP-077` | Portfolio Backtester (`/`) | Full Invalid Suite | Strong EP | `EC-013`, `EC-015`, `EC-020`, `EC-024` | Executed | Pass |

---

## 2. Boundary Value Analysis Traceability (TC-BVA-001 to TC-BVA-032)

| TC ID | Feature / Form | Input Field | Technique | EC / BC IDs Covered | Status | Result |
|:---:|---|---|---|---|:---:|:---:|
| `TC-BVA-001` | Portfolio Backtester | Allocation Sum (%) | 3-Point BVA (Below) | `BC-002`, `BC-003` | Executed | Pass |
| `TC-BVA-002` | Portfolio Backtester | Allocation Sum (%) | 3-Point BVA (At) | `BC-002`, `BC-003` | Executed | Pass |
| `TC-BVA-003` | Portfolio Backtester | Allocation Sum (%) | 3-Point BVA (Above) | `BC-002`, `BC-003` | Executed | Pass |
| `TC-BVA-004` | Portfolio Backtester | Starting Value ($) | 3-Point BVA (Below) | `BC-004` | Executed | Pass |
| `TC-BVA-005` | Portfolio Backtester | Starting Value ($) | 3-Point BVA (At) | `BC-004` | Executed | Pass |
| `TC-BVA-006` | Portfolio Backtester | Starting Value ($) | 3-Point BVA (Above) | `BC-004` | Executed | Pass |
| `TC-BVA-007` | Portfolio Backtester | Date Range | 3-Point BVA (At) | `BC-005` | Executed | Pass |
| `TC-BVA-008` | Portfolio Backtester | Date Range | 3-Point BVA (Below) | `BC-005` | Executed | Pass |
| `TC-BVA-009` | Portfolio Backtester | Date Range | 3-Point BVA (Above) | `BC-005` | Executed | Pass |
| `TC-BVA-010` | Portfolio Backtester | Rolling Window | 3-Point BVA (Below) | `BC-006` | Executed | Pass |
| `TC-BVA-011` | Portfolio Backtester | Rolling Window | 3-Point BVA (At) | `BC-006` | Executed | Pass |
| `TC-BVA-012` | Portfolio Backtester | Rolling Window | 3-Point BVA (Above) | `BC-006` | Executed | Pass |
| `TC-BVA-013` | Auth Modal (`/start`) | Password Length | 2-Point BVA (Below) | `BC-001` | Executed | Pass |
| `TC-BVA-014` | Auth Modal (`/start`) | Password Length | 2-Point BVA (At) | `BC-001` | Executed | Pass |
| `TC-BVA-015` | Monte Carlo (`/monte-carlo`) | Horizon (Years) | 2-Point BVA (Below) | `BC-007` | Executed | Pass |
| `TC-BVA-016` | Monte Carlo (`/monte-carlo`) | Horizon (Years) | 2-Point BVA (At) | `BC-007` | Executed | Pass |
| `TC-BVA-017` | Safe Withdrawal (`/safe-withdrawal`) | Withdrawal Rate (%) | 2-Point BVA (Below) | `BC-008` | Executed | Pass |
| `TC-BVA-018` | Safe Withdrawal (`/safe-withdrawal`) | Withdrawal Rate (%) | 2-Point BVA (At) | `BC-008` | Executed | Pass |
| `TC-BVA-019` | Contact Form (`/contact`) | Message Length | 2-Point BVA (Below) | `BC-009` | Executed | Pass |
| `TC-BVA-020` | Contact Form (`/contact`) | Message Length | 2-Point BVA (At) | `BC-009` | Executed | Pass |
| `TC-BVA-021` | Contact Form (`/contact`) | Message Length | 2-Point BVA (At) | `BC-010` | Executed | Pass |
| `TC-BVA-022` | Contact Form (`/contact`) | Message Length | 2-Point BVA (Above) | `BC-010` | Executed | Pass |
| `TC-BVA-023` | Contact Form (`/contact`) | Subject Length | 2-Point BVA (At) | `BC-011` | Executed | Pass |
| `TC-BVA-024` | Contact Form (`/contact`) | Subject Length | 2-Point BVA (Above) | `BC-011` | Executed | Pass |
| `TC-BVA-025` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | 2-Point BVA (Below) | `BC-012` | Executed | Pass |
| `TC-BVA-026` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | 2-Point BVA (At) | `BC-012` | Executed | Pass |
| `TC-BVA-027` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (Below) | `BC-013` | Executed | Pass |
| `TC-BVA-028` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (At) | `BC-013` | Executed | Pass |
| `TC-BVA-029` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (At) | `BC-014` | Executed | Pass |
| `TC-BVA-030` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | 2-Point BVA (Above) | `BC-014` | Executed | Pass |
| `TC-BVA-031` | TVM Calculator (`/time-value-of-money`) | Starting Value ($) | 2-Point BVA (Below) | `BC-015` | Executed | Pass |
| `TC-BVA-032` | TVM Calculator (`/time-value-of-money`) | Starting Value ($) | 2-Point BVA (At) | `BC-015` | Executed | Pass |
