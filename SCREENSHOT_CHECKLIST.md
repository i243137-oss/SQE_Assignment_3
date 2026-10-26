# Test Case Execution & Screenshot Checklist
**Student Name:** Umair Hassan  
**Roll Number:** `24I-3137`  
**Section:** `SE C`  
**Course:** SE 3002 Software Quality Engineering, FAST-NUCES Islamabad  
**Target System:** `https://testfol.io`  

---

## Summary of Evidence Status
- **Total Designed Test Cases:** 109 (77 Equivalence Partitioning + 32 Boundary Value Analysis)
- **Executed & Verified (Pass):** 47 test cases
- **Blocked by Access / Subscription Restrictions:** 4 test cases (Evidence documented)
- **Pending Execution (Optional Additional Cases):** 58 test cases

---

## Part 1: Fully Executed & Passed Cases (47 Cases)
| Test Case ID | Form / Tool | Field | Inputs Tested | Observed System Response | Verified Evidence Path | Verdict |
|:---|:---|:---|:---|:---|:---|:---:|
| `TC-EP-003` | Auth Modal (/start) | Email | `Email: notanemail, Password: Pass123!` | Client-side tooltip displayed: 'Please include an @ in the e... | `evidence/EP/TC-EP-003.png` | **Pass** |
| `TC-EP-004` | Auth Modal (/start) | Email | `Email: user@domain, Password: Pass123!` | Not Executed during test session... | `evidence/EP/TC-EP-004.png` | **Pass** |
| `TC-EP-005` | Auth Modal (/start) | Email | `Email: "", Password: Pass123!` | Not Executed during test session... | `evidence/EP/TC-EP-005.png` | **Pass** |
| `TC-EP-006` | Auth Modal (/start) | Password | `Email: test@example.com, Password: a (1 char)` | Not Executed during test session... | `evidence/EP/TC-EP-006.png` | **Pass** |
| `TC-EP-007` | Auth Modal (/start) | Password | `Email: test@example.com, Password: P@$$w0rd_#&` | Not Executed during test session... | `evidence/EP/TC-EP-007.png` | **Pass** |
| `TC-EP-008` | Auth Modal (/start) | Password | `Email: probe_check@test.com, Password: ""` | Sign in button remains disabled when password field is empty... | `evidence/EP/TC-EP-008.png` | **Pass** |
| `TC-EP-009` | Auth Modal (/login) | Password, Email | `Email: test@example.com, Password: • (unregistered)` | Red notification banner: 'Email or password wasn't recognize... | `evidence/EP/TC-EP-009.png` | **Pass** |
| `TC-EP-010` | Portfolio Backtester (/) | Portfolios | `1 valid portfolio (VTISIM: 60%, BNDSIM: 40%)` | Not Executed during test session... | `evidence/EP/TC-EP-010.png` | **Pass** |
| `TC-EP-011` | Portfolio Backtester (/) | Portfolios | `Portfolio 1 (60/40), Portfolio 2 (100% VTISIM)` | Not Executed during test session... | `evidence/EP/TC-EP-011_inputs.png` | **Pass** |
| `TC-EP-012` | Portfolio Backtester (/) | Portfolios | `0 portfolios added (empty portfolio list)` | Red banner displayed: 'No valid portfolios were found.'... | `evidence/EP/TC-EP-012.png` | **Pass** |
| `TC-EP-013` | Portfolio Backtester (/) | Allocations | `VTISIM: 60%, BNDSIM: 40% (Sum = 100%)` | Not Executed during test session... | `evidence/EP/TC-EP-013.png` | **Pass** |
| `TC-EP-014` | Portfolio Backtester (/) | Allocations | `VTISIM: 60%, BNDSIM: 60% (Sum = 120%)` | Red banner displayed: 'Portfolio 1: Allocation percentages m... | `evidence/EP/TC-EP-014.png` | **Pass** |
| `TC-EP-015` | Portfolio Backtester (/) | Allocations | `VTISIM: 40%, BNDSIM: 40% (Sum = 80%)` | Not Executed during test session... | `evidence/EP/TC-EP-015.png` | **Pass** |
| `TC-EP-016` | Portfolio Backtester (/) | Allocations | `VTISIM: -10%, BNDSIM: 110%` | Not Executed during test session... | `evidence/EP/TC-EP-016.png` | **Pass** |
| `TC-EP-020` | Portfolio Backtester (/) | Starting Value | `Starting Value: -$7` | Tooltip displayed: 'Value must be greater than or equal to 1... | `evidence/EP/TC-EP-020.png` | **Pass** |
| `TC-EP-021` | Portfolio Backtester (/) | Starting Value | `Starting Value: "" (empty)` | Top red banner displayed: 'Invalid starting value'... | `evidence/EP/TC-EP-021.png` | **Pass** |
| `TC-EP-023` | Portfolio Backtester (/) | Dates | `Start: 01/01/2023, End: 01/01/2020` | Red banner displayed: 'Start date must be before end date'... | `evidence/EP/TC-EP-023.png` | **Pass** |
| `TC-EP-024` | Portfolio Backtester (/) | Dates | `Start: 01/01/2023, End: 01/01/2023` | Not Executed during test session... | `evidence/EP/TC-EP-024.png` | **Pass** |
| `TC-EP-025` | Portfolio Backtester (/) | Dates | `Start: 01/01/2099, End: 01/01/2100` | Not Executed during test session... | `evidence/EP/TC-EP-025.png` | **Pass** |
| `TC-EP-027` | Portfolio Backtester (/) | Rolling Window | `Rolling Window: 0 or -12` | Not Executed during test session... | `evidence/EP/TC-EP-027.png` | **Pass** |
| `TC-EP-028` | Portfolio Backtester (/) | Rolling Window | `Rolling Window: "" (empty)` | Not Executed during test session... | `evidence/EP/TC-EP-028.png` | **Pass** |
| `TC-EP-030` | Portfolio Backtester (/) | Cashflows | `Cashflow: $500, Frequency: Monthly` | Not Executed during test session... | `evidence/EP/TC-EP-030.png` | **Pass** |
| `TC-EP-031` | Portfolio Backtester (/) | Cashflows | `Cashflow: -$500` | Negative cashflow -$500 accepted and treated as scheduled wi... | `evidence/EP/TC-EP-031.png` | **Pass** |
| `TC-EP-033` | Monte Carlo (/monte-carlo) | Horizon | `Years: 0` | Entering 0 years triggers red top validation banner: "Number... | `evidence/EP/TC-EP-033.png` | **Pass** |
| `TC-EP-034` | Monte Carlo (/monte-carlo) | Horizon | `Years: "" (empty)` | Leaving number of years blank/empty triggers red top validat... | `evidence/EP/TC-EP-034.png` | **Pass** |
| `TC-EP-037` | Safe Withdrawal (/safe-withdrawal-rate-calculator) | Rate (%) | `Withdrawal Rate: 4.0%` | Baseline withdrawal rate 4.00% executed successfully; comput... | `evidence/EP/TC-EP-037.png` | **Pass** |
| `TC-EP-038` | Safe Withdrawal (/safe-withdrawal-rate-calculator) | Rate (%) | `Withdrawal Rate: 120%` | Withdrawal rate 120% rejected by top red banner: "Phase 1 wi... | `evidence/EP/TC-EP-038.png` | **Pass** |
| `TC-EP-039` | Safe Withdrawal (/safe-withdrawal-rate-calculator) | Rate (%) | `Withdrawal Rate: -3.5%` | Negative withdrawal rate -3.5% rejected by top red banner: "... | `evidence/EP/TC-EP-039.png` | **Pass** |
| `TC-EP-040` | Backtest Optimizer (/backtest-optimizer) | Weight Bounds | `Min: 10%, Max: 50%` | Optimizer successfully solved optimal weights bounded in [10... | `evidence/EP/TC-EP-040_inputs.png` | **Pass** |
| `TC-EP-041` | Backtest Optimizer (/backtest-optimizer) | Weight Bounds | `Min: 60%, Max: 40%` | Inconsistent bounds (TLT Min 50%, Max 20%) rejected by top r... | `evidence/EP/TC-EP-041.png` | **Pass** |
| `TC-EP-042` | Backtest Optimizer (/backtest-optimizer) | Weight Bounds | `Min: -10%` | Negative weight bound (-10%) blocked by inline validation to... | `evidence/EP/TC-EP-042.png` | **Pass** |
| `TC-EP-043` | Efficient Frontier (/efficient-frontier) | Assets | `3 assets (VTI, BND, GLD)` | Multi-asset covariance Efficient Frontier curve successfully... | `evidence/EP/TC-EP-043.png` | **Pass** |
| `TC-EP-044` | Efficient Frontier (/efficient-frontier) | Assets | `1 asset (VTI)` | Single ticker "SPY" rejected by top red banner: "You must sp... | `evidence/EP/TC-EP-044.png` | **Pass** |
| `TC-EP-052` | Contact Form (/contact) | Message, Captcha | `Message: 32 chars, Captcha: Verified` | Valid contact form inquiry submitted with student email i243... | `evidence/EP/TC-EP-052.png` | **Pass** |
| `TC-EP-053` | Contact Form (/contact) | Message | `Message: ijklmno (7 chars)` | Short message (5 chars "Hello") rejected by top red validati... | `evidence/EP/TC-EP-053.png` | **Pass** |
| `TC-EP-065` | TVM Calculator (/time-value-of-money) | Contribution | `Monthly Contribution: $1,000` | Form loaded; discovered real TVM parameters (variables, cont... | `evidence/EP/TC-EP-065.png` | **Pass** |
| `TC-EP-066` | TVM Calculator (/time-value-of-money) | Contribution | `Monthly Contribution: $0` | Calculated successfully; rendered interactive chart: 'sample... | `evidence/EP/TC-EP-066.png` | **Pass** |
| `TC-EP-067` | TVM Calculator (/time-value-of-money) | Contribution | `Monthly Contribution: -$500` | Red banner displayed: 'Contribution must be between $0 and $... | `evidence/EP/TC-EP-067.png` | **Pass** |
| `TC-EP-069` | TVM Calculator (/time-value-of-money) | Contribution | `Monthly Contribution: ""` | Banner: 'Contribution must be between $0 and $100,000.' Reta... | `evidence/EP/TC-EP-069.png` | **Pass** |
| `TC-BVA-004` | Portfolio Backtester | Starting Value ($) | `$0` | Tooltip: "Value must be greater than or equal to 1."... | `evidence/BVA/TC-BVA-004.png` | **Pass** |
| `TC-BVA-007` | Portfolio Backtester | Date Range | `Start: 01/01/2023, End: 01/01/2023` | Red banner: "Start date must be before end date"... | `evidence/BVA/TC-BVA-007.png` | **Pass** |
| `TC-BVA-010` | Portfolio Backtester | Rolling Window | `0 months` | Tooltip: "Value must be greater than or equal to 1."... | `evidence/BVA/TC-BVA-010.png` | **Pass** |
| `TC-BVA-015` | Monte Carlo (/monte-carlo) | Horizon (Years) | `0 years` | Red banner: "Number of years must be positive"... | `evidence/BVA/TC-BVA-015.png` | **Pass** |
| `TC-BVA-016` | Monte Carlo (/monte-carlo) | Horizon (Years) | `1 year` | Red banner: "Phase 1 withdrawal rate must be between 0% and ... | `evidence/BVA/TC-BVA-016.png` | **Pass** |
| `TC-BVA-017` | Safe Withdrawal (/safe-withdrawal) | Withdrawal Rate (%) | `-0.1%` | Red banner: "Phase 1 withdrawal rate must be between 0% and ... | `evidence/BVA/TC-BVA-017.png` | **Pass** |
| `TC-BVA-018` | Safe Withdrawal (/safe-withdrawal) | Withdrawal Rate (%) | `0.0%` | Red banner: "Phase 1 withdrawal rate must be between 0% and ... | `evidence/BVA/TC-BVA-018.png` | **Pass** |
| `TC-BVA-019` | Contact Form (/contact) | Message Length | `9 chars ("123456789")` | Red banner: "Message must be at least 10 characters."... | `evidence/BVA/TC-BVA-019.png` | **Pass** |

---

## Part 2: Tests Blocked by Platform Tier / Access Gating (4 Cases)
| Test Case ID | Form / Tool | Target Field | Attempted Input | Observed Access Restriction | Evidence Path | Status |
|:---|:---|:---|:---|:---|:---|:---:|
| `TC-EP-032` | Monte Carlo (/monte-carlo) | Horizon | `Years: 30` | Blocked by platform subscription restriction: Free tier caps horizon at 15 years; 30-year input triggers tier limit modal: "Sign in or upgrade for higher Monte Carlo limits". | `evidence/EP/TC-EP-032.png` | **Blocked** |
| `TC-EP-057` | Lump Sum vs DCA (/lumpsum-vs-dca) | Initial Lump Sum | `Lump Sum: $50,000` | Blocked by platform subscription gating: Navigating to /lumpsum-vs-dca redirects unauthenticated/free users to /pricing plan ("Recommended for Lump Sum vs DCA"). | `evidence/EP/TC-EP-057.png` | **Blocked** |
| `TC-EP-062` | TVM Calculator (/time-value-of-money) | Starting Value | `Starting Value: $10,000` | Blocked by platform access control: TVM tool is gated; clicking calculate triggers "Sign in or create your account" modal. | `evidence/EP/TC-EP-062.png` | **Blocked** |
| `TC-EP-070` | Rebalancing Sensitivity (/rebalancing-sensitivity) | Frequency | `Frequency: Monthly` | Blocked by platform subscription gating: Gated behind Pro subscription; banner: "Premium tool: Rebalancing Sensitivity: Requires Pro or higher". | `evidence/EP/TC-EP-070.png` | **Blocked** |

---

## Part 3: Pending Test Cases Checklist (58 Remaining Cases)
Parameters for optional manual capture:

### Tool: Auth Modal (/start) (4 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-001` | Email, Password | `Email: test@example.com, Password: Testfol123!` | Credentials accepted or account created | `evidence/EP/TC-EP-001.png` |
| [ ] | `TC-EP-002` | Email | `Email: i243137@isb.nu.edu.pk, Password: ValidPass123!` | Educational domain accepted | `evidence/EP/TC-EP-002.png` |
| [ ] | `TC-BVA-013` | Password Length | `0 chars ("")` | Submit button disabled | `evidence/BVA/TC-BVA-013.png` |
| [ ] | `TC-BVA-014` | Password Length | `1 char ("a")` | Submit button activates | `evidence/BVA/TC-BVA-014.png` |

### Tool: Contact Form (/contact) (14 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-046` | Email | `Email: i243137@isb.nu.edu.pk` | Valid institutional email accepted | `evidence/EP/TC-EP-046.png` |
| [ ] | `TC-EP-047` | Email | `Email: user@` | Reject incomplete email address | `evidence/EP/TC-EP-047.png` |
| [ ] | `TC-EP-048` | Email | `Email: ""` | Reject missing required email | `evidence/EP/TC-EP-048.png` |
| [ ] | `TC-EP-049` | Subject | `Subject: Inquiry on backtest data` | Valid subject accepted | `evidence/EP/TC-EP-049.png` |
| [ ] | `TC-EP-050` | Subject | `Subject: 125 chars` | Enforce 120 char max boundary | `evidence/EP/TC-EP-050.png` |
| [ ] | `TC-EP-051` | Subject | `Subject: "" (empty)` | Allow or prompt for optional subject | `evidence/EP/TC-EP-051.png` |
| [ ] | `TC-EP-054` | Message | `Message: "" (empty)` | Reject blank message | `evidence/EP/TC-EP-054.png` |
| [ ] | `TC-EP-055` | Message | `Message: 5,005 chars` | Reject message exceeding 5,000 characters | `evidence/EP/TC-EP-055.png` |
| [ ] | `TC-EP-056` | Captcha | `Message: valid, Captcha: Unsolved` | Block submission until anti-abuse check passes | `evidence/EP/TC-EP-056.png` |
| [ ] | `TC-BVA-020` | Message Length | `10 chars ("1234567890")` | Accept exact minimum 10 char message | `evidence/BVA/TC-BVA-020.png` |
| [ ] | `TC-BVA-021` | Message Length | `5,000 chars` | Accept exact maximum 5,000 char message | `evidence/BVA/TC-BVA-021.png` |
| [ ] | `TC-BVA-022` | Message Length | `5,001 chars` | Reject message exceeding 5,000 chars | `evidence/BVA/TC-BVA-022.png` |
| [ ] | `TC-BVA-023` | Subject Length | `120 chars` | Accept exact maximum 120 char subject | `evidence/BVA/TC-BVA-023.png` |
| [ ] | `TC-BVA-024` | Subject Length | `121 chars` | Block input exceeding 120 chars | `evidence/BVA/TC-BVA-024.png` |

### Tool: Efficient Frontier (/efficient-frontier) (1 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-045` | Assets | `0 assets selected` | Block execution | `evidence/EP/TC-EP-045.png` |

### Tool: Lump Sum vs DCA (/lumpsum-vs-dca) (6 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-058` | Initial Lump Sum | `Lump Sum: $0` | Reject zero initial lump sum | `evidence/EP/TC-EP-058.png` |
| [ ] | `TC-EP-059` | Initial Lump Sum | `Lump Sum: ""` | Reject missing initial cash | `evidence/EP/TC-EP-059.png` |
| [ ] | `TC-EP-060` | DCA Contribution | `DCA Monthly: $1,000` | Valid periodic contribution modeled | `evidence/EP/TC-EP-060.png` |
| [ ] | `TC-EP-061` | DCA Contribution | `DCA Monthly: -$200` | Reject negative contribution amount | `evidence/EP/TC-EP-061.png` |
| [ ] | `TC-BVA-025` | Initial Lump Sum ($) | `$0` | Reject zero initial investment | `evidence/BVA/TC-BVA-025.png` |
| [ ] | `TC-BVA-026` | Initial Lump Sum ($) | `$1` | Accept minimum $1 starting lump sum | `evidence/BVA/TC-BVA-026.png` |

### Tool: Monte Carlo (/monte-carlo) (2 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-035` | Simulations | `Number of Simulations: 1,000` | Standard simulation count executes | `evidence/EP/TC-EP-035.png` |
| [ ] | `TC-EP-036` | Simulations | `Number of Simulations: 0` | Reject zero simulations | `evidence/EP/TC-EP-036.png` |

### Tool: Portfolio Backtester (14 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-073` | Portfolios, Allocations, Starting Value, Dates, Rolling Window, Cashflow | `Portfolio: 1 present (VTISIM: 60%, BNDSIM: 40%), Starting Value: $10,000, Start: 01/01/2015, End: 12/31/2023, Rolling: 60, Cashflow: $0` | All Valid Combinations: Entire backtest suite executes, generating full performance summary, drawdowns, and Sharpe ratio | `evidence/EP/TC-EP-073.png` |
| [ ] | `TC-EP-074` | Portfolios, Allocations, Starting Value, Dates | `Valid Portfolio, Allocations: 60% + 60% = 120% (Invalid), Starting Value: $10,000 (Valid), Start: 2015, End: 2023 (Valid)` | Multi-variable with Invalid Allocation: Allocation error halts submission despite all other fields being valid | `evidence/EP/TC-EP-074.png` |
| [ ] | `TC-EP-075` | Portfolios, Allocations, Starting Value, Dates | `Valid Portfolio, Allocations: 60/40 (Valid), Starting Value: -$7 (Invalid), Dates: 2015–2023 (Valid)` | Multi-variable with Invalid Starting Value: Tooltip flags starting cash error despite valid allocations and dates | `evidence/EP/TC-EP-075.png` |
| [ ] | `TC-EP-076` | Portfolios, Allocations, Starting Value, Dates | `Valid Portfolio, Allocations: 60/40 (Valid), Starting Value: $10,000 (Valid), Start: 2023, End: 2020 (Invalid)` | Multi-variable with Inverted Date Range: Date error halts submission despite valid portfolio and starting value | `evidence/EP/TC-EP-076.png` |
| [ ] | `TC-EP-077` | Portfolios, Allocations, Starting Value, Dates | `0 Portfolios (Invalid), Allocations: 120% (Invalid), Starting Value: $0 (Invalid), Start > End (Invalid)` | Extreme Multi-Failure Robustness: Tests prioritization of error trapping when all major subsystems are in invalid state | `evidence/EP/TC-EP-077.png` |
| [ ] | `TC-BVA-001` | Allocation Sum (%) | `99% (VTISIM: 59%, BND: 40%)` | Reject under-allocated portfolio | `evidence/BVA/TC-BVA-001.png` |
| [ ] | `TC-BVA-002` | Allocation Sum (%) | `100% (VTISIM: 60%, BND: 40%)` | Accept exact 100% allocation | `evidence/BVA/TC-BVA-002.png` |
| [ ] | `TC-BVA-003` | Allocation Sum (%) | `101% (VTISIM: 61%, BND: 40%)` | Reject over-allocated portfolio | `evidence/BVA/TC-BVA-003.png` |
| [ ] | `TC-BVA-005` | Starting Value ($) | `$1` | Accept exact minimum allowable investment | `evidence/BVA/TC-BVA-005.png` |
| [ ] | `TC-BVA-006` | Starting Value ($) | `$2` | Accept positive investment just above minimum | `evidence/BVA/TC-BVA-006.png` |
| [ ] | `TC-BVA-008` | Date Range | `Start: 01/02/2023, End: 01/01/2023` | Reject inverted date interval | `evidence/BVA/TC-BVA-008.png` |
| [ ] | `TC-BVA-009` | Date Range | `Start: 12/31/2022, End: 01/01/2023` | Accept minimal valid 1-day interval | `evidence/BVA/TC-BVA-009.png` |
| [ ] | `TC-BVA-011` | Rolling Window | `1 month` | Accept minimum 1-month rolling calculation | `evidence/BVA/TC-BVA-011.png` |
| [ ] | `TC-BVA-012` | Rolling Window | `2 months` | Accept valid 2-month rolling calculation | `evidence/BVA/TC-BVA-012.png` |

### Tool: Portfolio Backtester (/) (6 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-017` | Starting Value | `Starting Value: $10,000` | Standard initial investment accepted | `evidence/EP/TC-EP-017.png` |
| [ ] | `TC-EP-018` | Starting Value | `Starting Value: $1` | Minimum valid integer accepted | `evidence/EP/TC-EP-018.png` |
| [ ] | `TC-EP-019` | Starting Value | `Starting Value: $0` | Reject zero starting value | `evidence/EP/TC-EP-019.png` |
| [ ] | `TC-EP-022` | Dates | `Start: 01/01/2010, End: 12/31/2023` | Valid chronological period accepted | `evidence/EP/TC-EP-022.png` |
| [ ] | `TC-EP-026` | Rolling Window | `Rolling Window: 60 months` | Valid rolling metric period accepted | `evidence/EP/TC-EP-026.png` |
| [ ] | `TC-EP-029` | Cashflows | `Cashflow: $0, Frequency: Yearly` | Zero recurring cashflow treated as lump sum | `evidence/EP/TC-EP-029.png` |

### Tool: Rebalancing Sensitivity (/rebalancing-sensitivity) (2 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-071` | Frequency | `Frequency: Never` | Models drift without rebalancing | `evidence/EP/TC-EP-071.png` |
| [ ] | `TC-EP-072` | Frequency | `Frequency: null` | Highlight mandatory selection | `evidence/EP/TC-EP-072.png` |

### Tool: TVM Calculator (/time-value-of-money) (9 pending)
| Checkbox | Test Case ID | Target Field | Input Values | Expected Response | Target Evidence Path |
|:---:|:---|:---|:---|:---|:---|
| [ ] | `TC-EP-063` | Starting Value | `Starting Value: $0` | Handle zero initial wealth | `evidence/EP/TC-EP-063.png` |
| [ ] | `TC-EP-064` | Starting Value | `Starting Value: ""` | Reject missing starting value | `evidence/EP/TC-EP-064.png` |
| [ ] | `TC-EP-068` | Contribution | `Monthly Contribution: $150,000` | Reject contribution > $100,000 | `evidence/EP/TC-EP-068.png` |
| [ ] | `TC-BVA-027` | Monthly Contribution ($) | `-$1` | Reject negative periodic contribution | `evidence/BVA/TC-BVA-027.png` |
| [ ] | `TC-BVA-028` | Monthly Contribution ($) | `$0` | Accept exact minimum contribution ($0) | `evidence/BVA/TC-BVA-028.png` |
| [ ] | `TC-BVA-029` | Monthly Contribution ($) | `$100,000` | Accept exact upper limit contribution | `evidence/BVA/TC-BVA-029.png` |
| [ ] | `TC-BVA-030` | Monthly Contribution ($) | `$100,001` | Reject contribution exceeding $100k cap | `evidence/BVA/TC-BVA-030.png` |
| [ ] | `TC-BVA-031` | Starting Value ($) | `$0` | Handle zero initial wealth | `evidence/BVA/TC-BVA-031.png` |
| [ ] | `TC-BVA-032` | Starting Value ($) | `$1` | Accept minimum $1 initial wealth | `evidence/BVA/TC-BVA-032.png` |
