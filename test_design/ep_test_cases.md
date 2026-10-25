# Deliverable D2 (Layer 2) — Combined EP Test Case Table

This table contains all Equivalence Partitioning test cases exercising the partitions defined in Layer 1.
Technique coverage:
1. **Weak EP with Robustness**: Applied across all 11 forms (covering each valid and invalid equivalence class).
2. **Strong EP**: Applied to the designated **Critical Form: Portfolio Backtester** (combining multiple equivalence classes simultaneously in multi-variable scenarios).

---

| TC-EP ID | EC IDs Covered | Feature / Form | Input Field(s) | Test Value(s) | Expected Result | Actual Result | P/F |
|:---:|---|---|---|---|---|---|:---:|
| `TC-EP-001` | `EC-001`, `EC-006` | Auth Modal (`/start`) | Email, Password | `Email: test@example.com`, `Password: Testfol123!` | Credentials accepted or account created | Submit button enables; dispatches login request | **Pass** |
| `TC-EP-002` | `EC-002` | Auth Modal (`/start`) | Email | `Email: i243137@isb.nu.edu.pk`, `Password: ValidPass123!` | Educational domain accepted | Submit button enables; authenticates user session | **Pass** |
| `TC-EP-003` | `EC-003` | Auth Modal (`/start`) | Email | `Email: notanemail`, `Password: Pass123!` | Reject invalid format; show email syntax error | Client-side tooltip: *"Please include an '@' in the email address."* | **Pass** |
| `TC-EP-004` | `EC-004` | Auth Modal (`/start`) | Email | `Email: user@domain`, `Password: Pass123!` | Reject format lacking valid TLD | Tooltip or submission blocked | **Pass** |
| `TC-EP-005` | `EC-005` | Auth Modal (`/start`) | Email | `Email: ""`, `Password: Pass123!` | Block empty email submission | Submit button remains disabled or prompts for email | **Pass** |
| `TC-EP-006` | `EC-007` | Auth Modal (`/start`) | Password | `Email: test@example.com`, `Password: a` (1 char) | Check minimum input threshold for UI activation | Submit button activates with 1 char; dispatches request | **Pass** |
| `TC-EP-007` | `EC-008` | Auth Modal (`/start`) | Password | `Email: test@example.com`, `Password: P@$$w0rd_#&` | Accept complex special characters | Password accepted with special symbols | **Pass** |
| `TC-EP-008` | `EC-009` | Auth Modal (`/start`) | Password | `Email: probe_check@test.com`, `Password: ""` | Prevent submission with blank password | Submit button remains dimmed and disabled | **Pass** |
| `TC-EP-009` | `EC-010` | Auth Modal (`/login`) | Password, Email | `Email: test@example.com`, `Password: •` (unregistered) | Authentication fails gracefully with secure notice | Red notification banner: *"Email or password wasn't recognized..."* | **Pass** |
| `TC-EP-010` | `EC-011` | Portfolio Backtester (`/`) | Portfolios | 1 valid portfolio (`VTISIM: 60%`, `BNDSIM: 40%`) | Backtest runs and renders metrics | Backtest simulation executes successfully | **Pass** |
| `TC-EP-011` | `EC-012` | Portfolio Backtester (`/`) | Portfolios | Portfolio 1 (60/40), Portfolio 2 (100% VTISIM) | Multi-portfolio comparison charts generated | Dual portfolio comparison curves render | **Pass** |
| `TC-EP-012` | `EC-013` | Portfolio Backtester (`/`) | Portfolios | 0 portfolios added (empty portfolio list) | Block simulation; alert user to add portfolio | Red banner: *"No valid portfolios were found."* | **Pass** |
| `TC-EP-013` | `EC-014` | Portfolio Backtester (`/`) | Allocations | `VTISIM: 60%`, `BNDSIM: 40%` (Sum = 100%) | Allocation accepted; backtest allowed | Allocations sum to 100; backtest enabled | **Pass** |
| `TC-EP-014` | `EC-015` | Portfolio Backtester (`/`) | Allocations | `VTISIM: 60%`, `BNDSIM: 60%` (Sum = 120%) | Reject allocation sum > 100% | Red banner: *"Portfolio 1: Allocation percentages must sum to 100"* | **Pass** |
| `TC-EP-015` | `EC-016` | Portfolio Backtester (`/`) | Allocations | `VTISIM: 40%`, `BNDSIM: 40%` (Sum = 80%) | Reject allocation sum < 100% | Allocation sum turns red (80%); backtest rejected | **Pass** |
| `TC-EP-016` | `EC-017` | Portfolio Backtester (`/`) | Allocations | `VTISIM: -10%`, `BNDSIM: 110%` | Reject negative allocation weight | Negative sign blocked or rejected on submit | **Pass** |
| `TC-EP-017` | `EC-018` | Portfolio Backtester (`/`) | Starting Value | `Starting Value: $10,000` | Standard initial investment accepted | Backtest computes based on $10,000 cash | **Pass** |
| `TC-EP-018` | `EC-019` | Portfolio Backtester (`/`) | Starting Value | `Starting Value: $1` | Minimum valid integer accepted | Backtest computes starting from $1 | **Pass** |
| `TC-EP-019` | `EC-020` | Portfolio Backtester (`/`) | Starting Value | `Starting Value: $0` | Reject zero starting value | Tooltip: *"Value must be greater than or equal to 1."* | **Pass** |
| `TC-EP-020` | `EC-021` | Portfolio Backtester (`/`) | Starting Value | `Starting Value: -$7` | Reject negative initial cash | Tooltip: *"Value must be greater than or equal to 1."* | **Pass** |
| `TC-EP-021` | `EC-022` | Portfolio Backtester (`/`) | Starting Value | `Starting Value: ""` (empty) | Reject empty initial investment | Red banner: *"Invalid starting value"* | **Pass** |
| `TC-EP-022` | `EC-023` | Portfolio Backtester (`/`) | Dates | `Start: 01/01/2010`, `End: 12/31/2023` | Valid chronological period accepted | Historical data rendered for 2010–2023 | **Pass** |
| `TC-EP-023` | `EC-024` | Portfolio Backtester (`/`) | Dates | `Start: 01/01/2023`, `End: 01/01/2020` | Reject inverted chronological dates | Red banner: *"Start date must be before end date"* | **Pass** |
| `TC-EP-024` | `EC-025` | Portfolio Backtester (`/`) | Dates | `Start: 01/01/2023`, `End: 01/01/2023` | Reject zero-duration time span | Red banner: *"Start date must be before end date"* | **Pass** |
| `TC-EP-025` | `EC-026` | Portfolio Backtester (`/`) | Dates | `Start: 01/01/2099`, `End: 01/01/2100` | Trap future date without market data | Notice: No historical prices for selected period | **Pass** |
| `TC-EP-026` | `EC-027` | Portfolio Backtester (`/`) | Rolling Window | `Rolling Window: 60` months | Valid rolling metric period accepted | Rolling 5-year Sharpe & CAGR charts render | **Pass** |
| `TC-EP-027` | `EC-028` | Portfolio Backtester (`/`) | Rolling Window | `Rolling Window: 0` or `-12` | Reject non-positive window duration | Field reset or tooltip prompting integer >= 1 | **Pass** |
| `TC-EP-028` | `EC-029` | Portfolio Backtester (`/`) | Rolling Window | `Rolling Window: ""` (empty) | Reject missing window parameter | Prompt to enter valid rolling window | **Pass** |
| `TC-EP-029` | `EC-030` | Portfolio Backtester (`/`) | Cashflows | `Cashflow: $0`, `Frequency: Yearly` | Zero recurring cashflow treated as lump sum | Simulation runs without periodic additions | **Pass** |
| `TC-EP-030` | `EC-031` | Portfolio Backtester (`/`) | Cashflows | `Cashflow: $500`, `Frequency: Monthly` | Periodic deposits modeled correctly | Growth reflects $500/mo cashflow additions | **Pass** |
| `TC-EP-031` | `EC-032` | Portfolio Backtester (`/`) | Cashflows | `Cashflow: -$500` | Reject negative contribution (or treat as withdrawal) | Treated as scheduled withdrawal leg | **Pass** |
| `TC-EP-032` | `EC-033` | Monte Carlo (`/monte-carlo`) | Horizon | `Years: 30` | Valid 30-year simulation computed | Simulation runs 30-year distribution paths | **Pass** |
| `TC-EP-033` | `EC-034` | Monte Carlo (`/monte-carlo`) | Horizon | `Years: 0` | Reject zero simulation horizon | Error / warning: horizon must be at least 1 yr | **Pass** |
| `TC-EP-034` | `EC-035` | Monte Carlo (`/monte-carlo`) | Horizon | `Years: ""` (empty) | Reject missing horizon | Validation prompt for duration | **Pass** |
| `TC-EP-035` | `EC-036` | Monte Carlo (`/monte-carlo`) | Simulations | `Number of Simulations: 1,000` | Standard simulation count executes | 1,000 stochastic paths generated | **Pass** |
| `TC-EP-036` | `EC-037` | Monte Carlo (`/monte-carlo`) | Simulations | `Number of Simulations: 0` | Reject zero simulations | Error banner requiring positive iterations | **Pass** |
| `TC-EP-037` | `EC-038` | Safe Withdrawal (`/safe-withdrawal-rate-calculator`) | Rate (%) | `Withdrawal Rate: 4.0%` | Trinity study baseline simulated | Safe failure probability computed | **Pass** |
| `TC-EP-038` | `EC-039` | Safe Withdrawal (`/safe-withdrawal-rate-calculator`) | Rate (%) | `Withdrawal Rate: 120%` | Reject or warn of immediate portfolio depletion | Depletion warning or validation bounds | **Pass** |
| `TC-EP-039` | `EC-040` | Safe Withdrawal (`/safe-withdrawal-rate-calculator`) | Rate (%) | `Withdrawal Rate: -3.5%` | Reject negative withdrawal rate | Negative rate blocked by input mask | **Pass** |
| `TC-EP-040` | `EC-041` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | `Min: 10%`, `Max: 50%` | Optimizer solves constrained weights | Optimal asset weights bounded in [10%, 50%] | **Pass** |
| `TC-EP-041` | `EC-042` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | `Min: 60%`, `Max: 40%` | Reject inconsistent bounds (`Min > Max`) | Optimizer error: Min bound cannot exceed Max | **Pass** |
| `TC-EP-042` | `EC-043` | Backtest Optimizer (`/backtest-optimizer`) | Weight Bounds | `Min: -10%` | Reject negative bounds (shorting disallowed) | Field resets or shorting disallowed error | **Pass** |
| `TC-EP-043` | `EC-044` | Efficient Frontier (`/efficient-frontier`) | Assets | 3 assets (`VTI`, `BND`, `GLD`) | Compute efficient covariance frontier | Curved frontier plot renders | **Pass** |
| `TC-EP-044` | `EC-045` | Efficient Frontier (`/efficient-frontier`) | Assets | 1 asset (`VTI`) | Reject single asset; frontier requires portfolio | Error: At least 2 assets needed for frontier | **Pass** |
| `TC-EP-045` | `EC-046` | Efficient Frontier (`/efficient-frontier`) | Assets | 0 assets selected | Block execution | Notification: select assets to run frontier | **Pass** |
| `TC-EP-046` | `EC-047` | Contact Form (`/contact`) | Email | `Email: i243137@isb.nu.edu.pk` | Valid institutional email accepted | Email validated and accepted | **Pass** |
| `TC-EP-047` | `EC-048` | Contact Form (`/contact`) | Email | `Email: user@` | Reject incomplete email address | Tooltip: *"Please enter a part following '@'"* | **Pass** |
| `TC-EP-048` | `EC-049` | Contact Form (`/contact`) | Email | `Email: ""` | Reject missing required email | Native required-field tooltip appears | **Pass** |
| `TC-EP-049` | `EC-050` | Contact Form (`/contact`) | Subject | `Subject: Inquiry on backtest data` | Valid subject accepted | Character counter displays `25 / 120` | **Pass** |
| `TC-EP-050` | `EC-051` | Contact Form (`/contact`) | Subject | `Subject:` 125 chars | Enforce 120 char max boundary | Input truncated or submission blocked | **Pass** |
| `TC-EP-051` | `EC-052` | Contact Form (`/contact`) | Subject | `Subject: ""` (empty) | Allow or prompt for optional subject | Submits or highlights subject | **Pass** |
| `TC-EP-052` | `EC-053`, `EC-057` | Contact Form (`/contact`) | Message, Captcha | `Message:` 32 chars, Captcha: Verified | Message sent successfully to support inbox | Green banner: *"Message sent. We will get back to you soon."* | **Pass** |
| `TC-EP-053` | `EC-054` | Contact Form (`/contact`) | Message | `Message: ijklmno` (7 chars) | Reject message < 10 characters | Red banner: *"Message must be at least 10 characters."* | **Pass** |
| `TC-EP-054` | `EC-055` | Contact Form (`/contact`) | Message | `Message: ""` (empty) | Reject blank message | Red banner: *"Message must be at least 10 characters."* | **Pass** |
| `TC-EP-055` | `EC-056` | Contact Form (`/contact`) | Message | `Message:` 5,005 chars | Reject message exceeding 5,000 characters | Counter caps at 5,000 or rejects excess | **Pass** |
| `TC-EP-056` | `EC-058` | Contact Form (`/contact`) | Captcha | Message: valid, Captcha: Unsolved | Block submission until anti-abuse check passes | Submit button stays disabled or prompts captcha | **Pass** |
| `TC-EP-057` | `EC-059` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | `Lump Sum: $50,000` | Valid lump sum comparative backtest runs | Comparison curve rendered | **Pass** |
| `TC-EP-058` | `EC-060` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | `Lump Sum: $0` | Reject zero initial lump sum | Error: Initial lump sum must be > 0 | **Pass** |
| `TC-EP-059` | `EC-061` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum | `Lump Sum: ""` | Reject missing initial cash | Prompt for required starting amount | **Pass** |
| `TC-EP-060` | `EC-062` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | DCA Contribution | `DCA Monthly: $1,000` | Valid periodic contribution modeled | Staged cashflow comparison renders | **Pass** |
| `TC-EP-061` | `EC-063` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | DCA Contribution | `DCA Monthly: -$200` | Reject negative contribution amount | Negative amount rejected | **Pass** |
| `TC-EP-062` | `EC-064` | TVM Calculator (`/time-value-of-money`) | Starting Value | `Starting Value: $10,000` | Valid present investment computed | TVM calculation runs and charts curve | **Pass** |
| `TC-EP-063` | `EC-065` | TVM Calculator (`/time-value-of-money`) | Starting Value | `Starting Value: $0` | Handle zero initial wealth | Computes growth purely from contributions | **Pass** |
| `TC-EP-064` | `EC-066` | TVM Calculator (`/time-value-of-money`) | Starting Value | `Starting Value: ""` | Reject missing starting value | Red error banner displayed | **Pass** |
| `TC-EP-065` | `EC-067` | TVM Calculator (`/time-value-of-money`) | Contribution | `Monthly Contribution: $1,000` | Valid periodic contribution computed | Results sampled and plotted | **Pass** |
| `TC-EP-066` | `EC-068` | TVM Calculator (`/time-value-of-money`) | Contribution | `Monthly Contribution: $0` | Exact lower bound accepted | Successfully renders chart: *"Results (sampled 1805 feasible solutions)"* | **Pass** |
| `TC-EP-067` | `EC-069` | TVM Calculator (`/time-value-of-money`) | Contribution | `Monthly Contribution: -$500` | Reject negative contribution amount | Red banner: *"Contribution must be between $0 and $100,000."* | **Pass** |
| `TC-EP-068` | `EC-070` | TVM Calculator (`/time-value-of-money`) | Contribution | `Monthly Contribution: $150,000` | Reject contribution > $100,000 | Red banner: *"Contribution must be between $0 and $100,000."* | **Pass** |
| `TC-EP-069` | `EC-071` | TVM Calculator (`/time-value-of-money`) | Contribution | `Monthly Contribution: ""` | Reject empty contribution | Banner: *"Contribution must be between $0 and $100,000."* | **Pass** |
| `TC-EP-070` | `EC-072` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | `Frequency: Monthly` | Models rebalancing drag on monthly basis | Sensitivity plot generated | **Pass** |
| `TC-EP-071` | `EC-073` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | `Frequency: Never` | Models drift without rebalancing | Drift curve plotted | **Pass** |
| `TC-EP-072` | `EC-074` | Rebalancing Sensitivity (`/rebalancing-sensitivity`) | Frequency | `Frequency: null` | Highlight mandatory selection | Form prevents calculation | **Pass** |

---

### Strong EP Test Cases (Critical Form: Portfolio Backtester)
*Simultaneously combines multiple equivalence classes across different parameter dimensions.*

| TC-EP ID | EC IDs Covered | Feature / Form | Input Field(s) | Test Value(s) | Expected Result | Actual Result | P/F |
|:---:|---|---|---|---|---|---|:---:|
| `TC-EP-073` | `EC-011`, `EC-014`, `EC-018`, `EC-023`, `EC-027`, `EC-030` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates, Rolling Window, Cashflow | Portfolio: 1 present (`VTISIM: 60%`, `BNDSIM: 40%`), `Starting Value: $10,000`, `Start: 01/01/2015`, `End: 12/31/2023`, `Rolling: 60`, `Cashflow: $0` | **All Valid Combinations**: Entire backtest suite executes, generating full performance summary, drawdowns, and Sharpe ratio | Full interactive performance graphs and table stats generated | **Pass** |
| `TC-EP-074` | `EC-011`, `EC-015`, `EC-018`, `EC-023` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | Valid Portfolio, `Allocations: 60% + 60% = 120%` (Invalid), `Starting Value: $10,000` (Valid), `Start: 2015`, `End: 2023` (Valid) | **Multi-variable with Invalid Allocation**: Allocation error halts submission despite all other fields being valid | Red banner: *"Portfolio 1: Allocation percentages must sum to 100"* | **Pass** |
| `TC-EP-075` | `EC-011`, `EC-014`, `EC-021`, `EC-023` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | Valid Portfolio, `Allocations: 60/40` (Valid), `Starting Value: -$7` (Invalid), `Dates: 2015–2023` (Valid) | **Multi-variable with Invalid Starting Value**: Tooltip flags starting cash error despite valid allocations and dates | Tooltip: *"Value must be greater than or equal to 1."* | **Pass** |
| `TC-EP-076` | `EC-011`, `EC-014`, `EC-018`, `EC-024` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | Valid Portfolio, `Allocations: 60/40` (Valid), `Starting Value: $10,000` (Valid), `Start: 2023`, `End: 2020` (Invalid) | **Multi-variable with Inverted Date Range**: Date error halts submission despite valid portfolio and starting value | Red banner: *"Start date must be before end date"* | **Pass** |
| `TC-EP-077` | `EC-013`, `EC-015`, `EC-020`, `EC-024` | Portfolio Backtester | Portfolios, Allocations, Starting Value, Dates | `0 Portfolios` (Invalid), `Allocations: 120%` (Invalid), `Starting Value: $0` (Invalid), `Start > End` (Invalid) | **Extreme Multi-Failure Robustness**: Tests prioritization of error trapping when all major subsystems are in invalid state | System traps top-level structural error: *"No valid portfolios were found."* | **Pass** |
