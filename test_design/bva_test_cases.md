# Deliverable D3 (Layer 2) — Combined BVA Test Case Table

This table contains all Boundary Value Analysis test cases exercising the boundaries defined in Layer 1.
Technique coverage:
1. **All Forms (2-Point BVA)**: Evaluates two values per boundary (e.g. Below/At or At/Above).
2. **Critical Form: Portfolio Backtester (3-Point BVA)**: Evaluates three values per boundary (**Below**, **At**, and **Above**).

---

| TC-BVA ID | BC IDs | Feature / Form | Input Field | Test Value | Position | Expected Result | Actual Result | P/F |
|:---:|---|---|---|---|:---:|---|---|:---:|
| **3-POINT BVA ON CRITICAL FORM: PORTFOLIO BACKTESTER** | | | | | | | | |
| `TC-BVA-001` | `BC-002`, `BC-003` | Portfolio Backtester | Allocation Sum (%) | `80%` (`VTISIM: 40%`, `BNDSIM: 40%`) | **Below** | Reject under-allocated portfolio | Allocation sum highlights red (80%); red banner: *"Allocations must sum to 100"* | **Pass** |
| `TC-BVA-002` | `BC-002`, `BC-003` | Portfolio Backtester | Allocation Sum (%) | `100%` (`VTISIM: 60%`, `BNDSIM: 40%`) | **At** | Accept exact 100% allocation | Backtest executes simulation successfully | **Pass** |
| `TC-BVA-003` | `BC-002`, `BC-003` | Portfolio Backtester | Allocation Sum (%) | `120%` (`VTISIM: 60%`, `BNDSIM: 60%`) | **Above** | Reject over-allocated portfolio | Red banner: *"Portfolio 1: Allocation percentages must sum to 100"* | **Pass** |
| `TC-BVA-004` | `BC-004` | Portfolio Backtester | Starting Value ($) | `$0` | **Below** | Reject non-positive starting cash | Tooltip: "Value must be greater than or equal to 1." | **Pass** |
| `TC-BVA-005` | `BC-004` | Portfolio Backtester | Starting Value ($) | `$1` | **At** | Accept exact minimum allowable investment | Pending Execution | Not Executed |
| `TC-BVA-006` | `BC-004` | Portfolio Backtester | Starting Value ($) | `$10,000` | **Above** | Accept positive investment above minimum | Backtest executes simulation successfully ("Backtest complete") | **Pass** |
| `TC-BVA-007` | `BC-005` | Portfolio Backtester | Date Range | `Start: 01/01/2023`, `End: 01/01/2023` | **At** (Diff = 0) | Reject zero duration interval | Red banner: "Start date must be before end date" | **Pass** |
| `TC-BVA-008` | `BC-005` | Portfolio Backtester | Date Range | `Start: 01/01/2023`, `End: 01/01/2020` | **Below** (Start > End) | Reject inverted date interval | Red banner: *"Start date must be before end date"* | **Pass** |
| `TC-BVA-009` | `BC-005` | Portfolio Backtester | Date Range | `Start: 01/01/2025`, `End: 10/26/2026` | **Above** (Start < End) | Accept valid chronological date interval | Backtest accepts range and computes successfully | **Pass** |
| `TC-BVA-010` | `BC-006` | Portfolio Backtester | Rolling Window | `0 months` | **Below** | Reject zero rolling window | Tooltip: "Value must be greater than or equal to 1." | **Pass** |
| `TC-BVA-011` | `BC-006` | Portfolio Backtester | Rolling Window | `1 month` | **At** | Accept minimum 1-month rolling calculation | Pending Execution | Not Executed |
| `TC-BVA-012` | `BC-006` | Portfolio Backtester | Rolling Window | `60 months` | **Above** | Accept valid rolling calculation above minimum | Backtest executes simulation successfully | **Pass** |
| **2-POINT BVA ON REMAINING IN-SCOPE FORMS** | | | | | | | | |
| `TC-BVA-013` | `BC-001` | Auth Modal (`/start`) | Password Length | `0 chars` (`""`) | **Below** | Submit button disabled | Submit button dimmed / disabled client-side | **Pass** |
| `TC-BVA-014` | `BC-001` | Auth Modal (`/start`) | Password Length | `1 char` (`"a"`) | **At** | Submit button activates | Submit button enabled client-side | **Pass** |
| `TC-BVA-015` | `BC-007` | Monte Carlo (`/monte-carlo`) | Horizon (Years) | `0 years` | **Below** | Reject zero horizon | Red banner: "Number of years must be positive" | **Pass** |
| `TC-BVA-016` | `BC-007` | Monte Carlo (`/monte-carlo`) | Horizon (Years) | `1 year` | **At** | Accept minimum 1-year stochastic run | Red banner: "Phase 1 withdrawal rate must be between 0% and 100%" | **Pass** |
| `TC-BVA-017` | `BC-008` | Safe Withdrawal (`/safe-withdrawal`) | Withdrawal Rate (%) | `-0.1%` | **Below** | Reject negative withdrawal percentage | Red banner: "Phase 1 withdrawal rate must be between 0% and 100%" | **Pass** |
| `TC-BVA-018` | `BC-008` | Safe Withdrawal (`/safe-withdrawal`) | Withdrawal Rate (%) | `0.0%` | **At** | Accept zero withdrawal rate (capital preservation) | Red banner: "Phase 1 withdrawal rate must be between 0% and 100%" | **Pass** |
| `TC-BVA-019` | `BC-009` | Contact Form (`/contact`) | Message Length | `9 chars` (`"123456789"`) | **Below** | Reject message under 10 chars | Red banner: "Message must be at least 10 characters." | **Pass** |
| `TC-BVA-020` | `BC-009` | Contact Form (`/contact`) | Message Length | `10 chars` (`"1234567890"`) | **At** | Accept exact minimum 10 char message | Pending Execution | Not Executed |
| `TC-BVA-021` | `BC-010` | Contact Form (`/contact`) | Message Length | `5,000 chars` | **At** | Accept exact maximum 5,000 char message | Pending Execution | Not Executed |
| `TC-BVA-022` | `BC-010` | Contact Form (`/contact`) | Message Length | `5,001 chars` | **Above** | Reject message exceeding 5,000 chars | Pending Execution | Not Executed |
| `TC-BVA-023` | `BC-011` | Contact Form (`/contact`) | Subject Length | `120 chars` | **At** | Accept exact maximum 120 char subject | Pending Execution | Not Executed |
| `TC-BVA-024` | `BC-011` | Contact Form (`/contact`) | Subject Length | `121 chars` | **Above** | Block input exceeding 120 chars | Pending Execution | Not Executed |
| `TC-BVA-025` | `BC-012` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | `$0` | **Below** | Reject zero initial investment | Pending Execution | Not Executed |
| `TC-BVA-026` | `BC-012` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | `$1` | **At** | Accept minimum $1 starting lump sum | Pending Execution | Not Executed |
| `TC-BVA-027` | `BC-013` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | `-$1` | **Below** | Reject negative periodic contribution | Pending Execution | Not Executed |
| `TC-BVA-028` | `BC-013` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | `$0` | **At** | Accept exact minimum contribution ($0) | Pending Execution | Not Executed |
| `TC-BVA-029` | `BC-014` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | `$100,000` | **At** | Accept exact upper limit contribution | Pending Execution | Not Executed |
| `TC-BVA-030` | `BC-014` | TVM Calculator (`/time-value-of-money`) | Monthly Contribution ($) | `$100,001` | **Above** | Reject contribution exceeding $100k cap | Pending Execution | Not Executed |
| `TC-BVA-031` | `BC-015` | TVM Calculator (`/time-value-of-money`) | Starting Value ($) | `$0` | **Below** | Handle zero initial wealth | Pending Execution | Not Executed |
| `TC-BVA-032` | `BC-015` | TVM Calculator (`/time-value-of-money`) | Starting Value ($) | `$1` | **At** | Accept minimum $1 initial wealth | Pending Execution | Not Executed |
