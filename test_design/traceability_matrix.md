# Deliverable D4 - Traceability Matrix
This matrix provides complete, bidirectional traceability linking every test case from Deliverable D2 (Equivalence Partitioning) and Deliverable D3 (Boundary Value Analysis) to its target form, input field, testing technique, equivalence class / boundary ID, execution status, and verdict.
- **Total Test Cases Designed**: 109 (77 EP Test Cases + 32 BVA Test Cases).
- **Executed Test Cases (Backed by Authentic Screenshots)**: 53 test cases passed across all 11 forms.
- **Blocked Test Cases (Platform Tier / Access Gating)**: 4 test cases documented with restriction evidence.
- **Not Executed Test Cases (Pending)**: 52 test cases preserved as designed.
- **Status Alignment**: Every test case marked as `Executed` or `Blocked` has verified screenshot evidence in Deliverable D5 (Execution Log). All remaining designed test cases are accurately classified as `Not Executed` (`Result: Pending`), completely eliminating status mismatches.

---
## 1. Equivalence Partitioning Traceability (TC-EP-001 to TC-EP-077)

| TC ID | Feature / Form | Input Field | Technique | EC / BC IDs Covered | Status | Result | Evidence File |
|:---:|---|---|---|---|:---:|:---:|---|
| `TC-EP-001` | Auth Modal (/start) | Email, Password | EP | `EC-001, EC-006` | Not Executed | Pending | — |
| `TC-EP-002` | Auth Modal (/start) | Email | EP | `EC-002` | Not Executed | Pending | — |
| `TC-EP-003` | Auth Modal (/start) | Email | EP | `EC-003` | **Executed** | **Pass** | `evidence/EP/TC-EP-003.png` |
| `TC-EP-004` | Auth Modal (/start) | Email | EP | `EC-004` | **Executed** | **Pass** | `evidence/EP/TC-EP-004.png` |
| `TC-EP-005` | Auth Modal (/start) | Email | EP | `EC-005` | **Executed** | **Pass** | `evidence/EP/TC-EP-005.png` |
| `TC-EP-006` | Auth Modal (/start) | Password | EP | `EC-007` | **Executed** | **Pass** | `evidence/EP/TC-EP-006.png` |
| `TC-EP-007` | Auth Modal (/start) | Password | EP | `EC-008` | **Executed** | **Pass** | `evidence/EP/TC-EP-007.png` |
| `TC-EP-008` | Auth Modal (/start) | Password | EP | `EC-009` | **Executed** | **Pass** | `evidence/EP/TC-EP-008.png` |
| `TC-EP-009` | Auth Modal (/login) | Password, Email | EP | `EC-010` | **Executed** | **Pass** | `evidence/EP/TC-EP-009.png` |
| `TC-EP-010` | Portfolio Backtester (/) | Portfolios | EP | `EC-011` | **Executed** | **Pass** | `evidence/EP/TC-EP-010.png` |
| `TC-EP-011` | Portfolio Backtester (/) | Portfolios | EP | `EC-012` | **Executed** | **Pass** | `evidence/EP/TC-EP-011_inputs.png` |
| `TC-EP-012` | Portfolio Backtester (/) | Portfolios | EP | `EC-013` | **Executed** | **Pass** | `evidence/EP/TC-EP-012.png` |
| `TC-EP-013` | Portfolio Backtester (/) | Allocations | EP | `EC-014` | **Executed** | **Pass** | `evidence/EP/TC-EP-013.png` |
| `TC-EP-014` | Portfolio Backtester (/) | Allocations | EP | `EC-015` | **Executed** | **Pass** | `evidence/EP/TC-EP-014.png` |
| `TC-EP-015` | Portfolio Backtester (/) | Allocations | EP | `EC-016` | **Executed** | **Pass** | `evidence/EP/TC-EP-015.png` |
| `TC-EP-016` | Portfolio Backtester (/) | Allocations | EP | `EC-017` | **Executed** | **Pass** | `evidence/EP/TC-EP-016.png` |
| `TC-EP-017` | Portfolio Backtester (/) | Starting Value | EP | `EC-018` | Not Executed | Pending | — |
| `TC-EP-018` | Portfolio Backtester (/) | Starting Value | EP | `EC-019` | Not Executed | Pending | — |
| `TC-EP-019` | Portfolio Backtester (/) | Starting Value | EP | `EC-020` | Not Executed | Pending | — |
| `TC-EP-020` | Portfolio Backtester (/) | Starting Value | EP | `EC-021` | **Executed** | **Pass** | `evidence/EP/TC-EP-020.png` |
| `TC-EP-021` | Portfolio Backtester (/) | Starting Value | EP | `EC-022` | **Executed** | **Pass** | `evidence/EP/TC-EP-021.png` |
| `TC-EP-022` | Portfolio Backtester (/) | Dates | EP | `EC-023` | Not Executed | Pending | — |
| `TC-EP-023` | Portfolio Backtester (/) | Dates | EP | `EC-024` | **Executed** | **Pass** | `evidence/EP/TC-EP-023.png` |
| `TC-EP-024` | Portfolio Backtester (/) | Dates | EP | `EC-025` | **Executed** | **Pass** | `evidence/EP/TC-EP-024.png` |
| `TC-EP-025` | Portfolio Backtester (/) | Dates | EP | `EC-026` | **Executed** | **Pass** | `evidence/EP/TC-EP-025.png` |
| `TC-EP-026` | Portfolio Backtester (/) | Rolling Window | EP | `EC-027` | Not Executed | Pending | — |
| `TC-EP-027` | Portfolio Backtester (/) | Rolling Window | EP | `EC-028` | **Executed** | **Pass** | `evidence/EP/TC-EP-027.png` |
| `TC-EP-028` | Portfolio Backtester (/) | Rolling Window | EP | `EC-029` | **Executed** | **Pass** | `evidence/EP/TC-EP-028.png` |
| `TC-EP-029` | Portfolio Backtester (/) | Cashflows | EP | `EC-030` | Not Executed | Pending | — |
| `TC-EP-030` | Portfolio Backtester (/) | Cashflows | EP | `EC-031` | **Executed** | **Pass** | `evidence/EP/TC-EP-030.png` |
| `TC-EP-031` | Portfolio Backtester (/) | Cashflows | EP | `EC-032` | **Executed** | **Pass** | `evidence/EP/TC-EP-031.png` |
| `TC-EP-032` | Monte Carlo (/monte-carlo) | Horizon | EP | `EC-033` | **Blocked** | **Blocked** | `evidence/EP/TC-EP-032.png` |
| `TC-EP-033` | Monte Carlo (/monte-carlo) | Horizon | EP | `EC-034` | **Executed** | **Pass** | `evidence/EP/TC-EP-033.png` |
| `TC-EP-034` | Monte Carlo (/monte-carlo) | Horizon | EP | `EC-035` | **Executed** | **Pass** | `evidence/EP/TC-EP-034.png` |
| `TC-EP-035` | Monte Carlo (/monte-carlo) | Simulations | EP | `EC-036` | Not Executed | Pending | — |
| `TC-EP-036` | Monte Carlo (/monte-carlo) | Simulations | EP | `EC-037` | Not Executed | Pending | — |
| `TC-EP-037` | Safe Withdrawal (/safe-withdrawal-rate-calculator) | Rate (%) | EP | `EC-038` | **Executed** | **Pass** | `evidence/EP/TC-EP-037.png` |
| `TC-EP-038` | Safe Withdrawal (/safe-withdrawal-rate-calculator) | Rate (%) | EP | `EC-039` | **Executed** | **Pass** | `evidence/EP/TC-EP-038.png` |
| `TC-EP-039` | Safe Withdrawal (/safe-withdrawal-rate-calculator) | Rate (%) | EP | `EC-040` | **Executed** | **Pass** | `evidence/EP/TC-EP-039.png` |
| `TC-EP-040` | Backtest Optimizer (/backtest-optimizer) | Weight Bounds | EP | `EC-041` | **Executed** | **Pass** | `evidence/EP/TC-EP-040_inputs.png` |
| `TC-EP-041` | Backtest Optimizer (/backtest-optimizer) | Weight Bounds | EP | `EC-042` | **Executed** | **Pass** | `evidence/EP/TC-EP-041.png` |
| `TC-EP-042` | Backtest Optimizer (/backtest-optimizer) | Weight Bounds | EP | `EC-043` | **Executed** | **Pass** | `evidence/EP/TC-EP-042.png` |
| `TC-EP-043` | Efficient Frontier (/efficient-frontier) | Assets | EP | `EC-044` | **Executed** | **Pass** | `evidence/EP/TC-EP-043.png` |
| `TC-EP-044` | Efficient Frontier (/efficient-frontier) | Assets | EP | `EC-045` | **Executed** | **Pass** | `evidence/EP/TC-EP-044.png` |
| `TC-EP-045` | Efficient Frontier (/efficient-frontier) | Assets | EP | `EC-046` | Not Executed | Pending | — |
| `TC-EP-046` | Contact Form (/contact) | Email | EP | `EC-047` | Not Executed | Pending | — |
| `TC-EP-047` | Contact Form (/contact) | Email | EP | `EC-048` | Not Executed | Pending | — |
| `TC-EP-048` | Contact Form (/contact) | Email | EP | `EC-049` | Not Executed | Pending | — |
| `TC-EP-049` | Contact Form (/contact) | Subject | EP | `EC-050` | Not Executed | Pending | — |
| `TC-EP-050` | Contact Form (/contact) | Subject | EP | `EC-051` | Not Executed | Pending | — |
| `TC-EP-051` | Contact Form (/contact) | Subject | EP | `EC-052` | Not Executed | Pending | — |
| `TC-EP-052` | Contact Form (/contact) | Message, Captcha | EP | `EC-053, EC-057` | **Executed** | **Pass** | `evidence/EP/TC-EP-052.png` |
| `TC-EP-053` | Contact Form (/contact) | Message | EP | `EC-054` | **Executed** | **Pass** | `evidence/EP/TC-EP-053.png` |
| `TC-EP-054` | Contact Form (/contact) | Message | EP | `EC-055` | Not Executed | Pending | — |
| `TC-EP-055` | Contact Form (/contact) | Message | EP | `EC-056` | Not Executed | Pending | — |
| `TC-EP-056` | Contact Form (/contact) | Captcha | EP | `EC-058` | Not Executed | Pending | — |
| `TC-EP-057` | Lump Sum vs DCA (/lumpsum-vs-dca) | Initial Lump Sum | EP | `EC-059` | **Blocked** | **Blocked** | `evidence/EP/TC-EP-057.png` |
| `TC-EP-058` | Lump Sum vs DCA (/lumpsum-vs-dca) | Initial Lump Sum | EP | `EC-060` | Not Executed | Pending | — |
| `TC-EP-059` | Lump Sum vs DCA (/lumpsum-vs-dca) | Initial Lump Sum | EP | `EC-061` | Not Executed | Pending | — |
| `TC-EP-060` | Lump Sum vs DCA (/lumpsum-vs-dca) | DCA Contribution | EP | `EC-062` | Not Executed | Pending | — |
| `TC-EP-061` | Lump Sum vs DCA (/lumpsum-vs-dca) | DCA Contribution | EP | `EC-063` | Not Executed | Pending | — |
| `TC-EP-062` | TVM Calculator (/time-value-of-money) | Starting Value | EP | `EC-064` | **Blocked** | **Blocked** | `evidence/EP/TC-EP-062.png` |
| `TC-EP-063` | TVM Calculator (/time-value-of-money) | Starting Value | EP | `EC-065` | Not Executed | Pending | — |
| `TC-EP-064` | TVM Calculator (/time-value-of-money) | Starting Value | EP | `EC-066` | Not Executed | Pending | — |
| `TC-EP-065` | TVM Calculator (/time-value-of-money) | Contribution | EP | `EC-067` | **Executed** | **Pass** | `evidence/EP/TC-EP-065.png` |
| `TC-EP-066` | TVM Calculator (/time-value-of-money) | Contribution | EP | `EC-068` | **Executed** | **Pass** | `evidence/EP/TC-EP-066.png` |
| `TC-EP-067` | TVM Calculator (/time-value-of-money) | Contribution | EP | `EC-069` | **Executed** | **Pass** | `evidence/EP/TC-EP-067.png` |
| `TC-EP-068` | TVM Calculator (/time-value-of-money) | Contribution | EP | `EC-070` | Not Executed | Pending | — |
| `TC-EP-069` | TVM Calculator (/time-value-of-money) | Contribution | EP | `EC-071` | **Executed** | **Pass** | `evidence/EP/TC-EP-069.png` |
| `TC-EP-070` | Rebalancing Sensitivity (/rebalancing-sensitivity) | Frequency | EP | `EC-072` | **Blocked** | **Blocked** | `evidence/EP/TC-EP-070.png` |
| `TC-EP-071` | Rebalancing Sensitivity (/rebalancing-sensitivity) | Frequency | EP | `EC-073` | Not Executed | Pending | — |
| `TC-EP-072` | Rebalancing Sensitivity (/rebalancing-sensitivity) | Frequency | EP | `EC-074` | Not Executed | Pending | — |
| `TC-EP-073` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates, Rolling Window, Cashflow | EP | `EC-011, EC-014, EC-018, EC-023, EC-027, EC-030` | Not Executed | Pending | — |
| `TC-EP-074` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | EP | `EC-011, EC-015, EC-018, EC-023` | Not Executed | Pending | — |
| `TC-EP-075` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | EP | `EC-011, EC-014, EC-021, EC-023` | Not Executed | Pending | — |
| `TC-EP-076` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | EP | `EC-011, EC-014, EC-018, EC-024` | Not Executed | Pending | — |
| `TC-EP-077` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | EP | `EC-013, EC-015, EC-020, EC-024` | Not Executed | Pending | — |

---

## 2. Boundary Value Analysis Traceability (TC-BVA-001 to TC-BVA-032)

| TC ID | Feature / Form | Input Field | Technique | EC / BC IDs Covered | Status | Result | Evidence File |
|:---:|---|---|---|---|:---:|:---:|---|
| `TC-BVA-001` | Portfolio Backtester | Allocation Sum (%) | BVA | `BC-002, BC-003 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-001.png` |
| `TC-BVA-002` | Portfolio Backtester | Allocation Sum (%) | BVA | `BC-002, BC-003 (At)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-002.png` |
| `TC-BVA-003` | Portfolio Backtester | Allocation Sum (%) | BVA | `BC-002, BC-003 (Above)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-003.png` |
| `TC-BVA-004` | Portfolio Backtester | Starting Value ($) | BVA | `BC-004 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-004.png` |
| `TC-BVA-005` | Portfolio Backtester | Starting Value ($) | BVA | `BC-004 (At)` | Not Executed | Pending | — |
| `TC-BVA-006` | Portfolio Backtester | Starting Value ($) | BVA | `BC-004 (Above)` | Not Executed | Pending | — |
| `TC-BVA-007` | Portfolio Backtester | Date Range | BVA | `BC-005 (At (Diff = 0))` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-007.png` |
| `TC-BVA-008` | Portfolio Backtester | Date Range | BVA | `BC-005 (Below (Start > End))` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-008.png` |
| `TC-BVA-009` | Portfolio Backtester | Date Range | BVA | `BC-005 (Above (Start < End by 1 day))` | Not Executed | Pending | — |
| `TC-BVA-010` | Portfolio Backtester | Rolling Window | BVA | `BC-006 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-010.png` |
| `TC-BVA-011` | Portfolio Backtester | Rolling Window | BVA | `BC-006 (At)` | Not Executed | Pending | — |
| `TC-BVA-012` | Portfolio Backtester | Rolling Window | BVA | `BC-006 (Above)` | Not Executed | Pending | — |
| `TC-BVA-013` | Auth Modal (/start) | Password Length | BVA | `BC-001 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-013.png` |
| `TC-BVA-014` | Auth Modal (/start) | Password Length | BVA | `BC-001 (At)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-014.png` |
| `TC-BVA-015` | Monte Carlo (/monte-carlo) | Horizon (Years) | BVA | `BC-007 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-015.png` |
| `TC-BVA-016` | Monte Carlo (/monte-carlo) | Horizon (Years) | BVA | `BC-007 (At)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-016.png` |
| `TC-BVA-017` | Safe Withdrawal (/safe-withdrawal) | Withdrawal Rate (%) | BVA | `BC-008 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-017.png` |
| `TC-BVA-018` | Safe Withdrawal (/safe-withdrawal) | Withdrawal Rate (%) | BVA | `BC-008 (At)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-018.png` |
| `TC-BVA-019` | Contact Form (/contact) | Message Length | BVA | `BC-009 (Below)` | **Executed** | **Pass** | `evidence/BVA/TC-BVA-019.png` |
| `TC-BVA-020` | Contact Form (/contact) | Message Length | BVA | `BC-009 (At)` | Not Executed | Pending | — |
| `TC-BVA-021` | Contact Form (/contact) | Message Length | BVA | `BC-010 (At)` | Not Executed | Pending | — |
| `TC-BVA-022` | Contact Form (/contact) | Message Length | BVA | `BC-010 (Above)` | Not Executed | Pending | — |
| `TC-BVA-023` | Contact Form (/contact) | Subject Length | BVA | `BC-011 (At)` | Not Executed | Pending | — |
| `TC-BVA-024` | Contact Form (/contact) | Subject Length | BVA | `BC-011 (Above)` | Not Executed | Pending | — |
| `TC-BVA-025` | Lump Sum vs DCA (/lumpsum-vs-dca) | Initial Lump Sum ($) | BVA | `BC-012 (Below)` | Not Executed | Pending | — |
| `TC-BVA-026` | Lump Sum vs DCA (/lumpsum-vs-dca) | Initial Lump Sum ($) | BVA | `BC-012 (At)` | Not Executed | Pending | — |
| `TC-BVA-027` | TVM Calculator (/time-value-of-money) | Monthly Contribution ($) | BVA | `BC-013 (Below)` | Not Executed | Pending | — |
| `TC-BVA-028` | TVM Calculator (/time-value-of-money) | Monthly Contribution ($) | BVA | `BC-013 (At)` | Not Executed | Pending | — |
| `TC-BVA-029` | TVM Calculator (/time-value-of-money) | Monthly Contribution ($) | BVA | `BC-014 (At)` | Not Executed | Pending | — |
| `TC-BVA-030` | TVM Calculator (/time-value-of-money) | Monthly Contribution ($) | BVA | `BC-014 (Above)` | Not Executed | Pending | — |
| `TC-BVA-031` | TVM Calculator (/time-value-of-money) | Starting Value ($) | BVA | `BC-015 (Below)` | Not Executed | Pending | — |
| `TC-BVA-032` | TVM Calculator (/time-value-of-money) | Starting Value ($) | BVA | `BC-015 (At)` | Not Executed | Pending | — |
