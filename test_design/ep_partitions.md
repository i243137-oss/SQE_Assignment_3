# Deliverable D2 (Layer 1) — Equivalence Partition Tables

This document contains the complete Equivalence Partition (EP) Analysis Tables for all in-scope forms and input fields across [testfol.io](https://testfol.io).
Each partition is assigned a unique, sequential `EC-xxx` ID and classified as either a Valid Equivalence Class (`VEC`) or an Invalid Equivalence Class (`IEC`).

---

## Form 1 & 2: Authentication Modal (Sign Up & Login — `/start`, `/login`)

### EP-01: Feature: Authentication Modal | Input Field: `Email address`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-001` | Valid standard email format (contains local-part, `@`, domain, and TLD) | `test@example.com` | **VEC** |
| `EC-002` | Registered student FAST university email format | `i243137@isb.nu.edu.pk` | **VEC** |
| `EC-003` | Malformed email string missing `@` symbol | `notanemail` | **IEC** |
| `EC-004` | Malformed email missing top-level domain (TLD) | `user@domain` | **IEC** |
| `EC-005` | Completely empty / blank email address | `""` (empty) | **IEC** |

### EP-02: Feature: Authentication Modal | Input Field: `Password`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-006` | Valid standard alphanumeric password (length ≥ 8) | `Testfol123!` | **VEC** |
| `EC-007` | Single-character input (activates submit button client-side) | `a` | **VEC** |
| `EC-008` | Password with special characters and symbols | `P@$$w0rd_#&` | **VEC** |
| `EC-009` | Completely empty / blank password | `""` (empty) | **IEC** |
| `EC-010` | Non-existent / unrecognized credentials for authentication | `DummyUnregistered99!` | **IEC** |

---

## Form 3: Portfolio Backtester (`/`) — DESIGNATED CRITICAL FORM

### EP-03: Feature: Portfolio Backtester | Input Field: `Portfolio Configuration`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-011` | At least one valid, configured portfolio present | 1 portfolio (`VTISIM: 60%`, `BNDSIM: 40%`) | **VEC** |
| `EC-012` | Multiple configured comparison portfolios present | Portfolio 1 (60/40), Portfolio 2 (100% VTISIM) | **VEC** |
| `EC-013` | No portfolios configured (0 portfolios present) | `0 portfolios` (empty list) | **IEC** |

### EP-04: Feature: Portfolio Backtester | Input Field: `Asset Allocation Percentage (%)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-014` | Total portfolio asset allocations sum to exactly 100% | `VTISIM: 60%`, `BNDSIM: 40%` (Sum = 100%) | **VEC** |
| `EC-015` | Total portfolio asset allocations exceed 100% | `VTISIM: 60%`, `BNDSIM: 60%` (Sum = 120%) | **IEC** |
| `EC-016` | Total portfolio asset allocations sum to less than 100% | `VTISIM: 40%`, `BNDSIM: 40%` (Sum = 80%) | **IEC** |
| `EC-017` | Negative asset allocation percentage entered | `VTISIM: -10%`, `BNDSIM: 110%` | **IEC** |

### EP-05: Feature: Portfolio Backtester | Input Field: `Starting Value ($)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-018` | Standard positive integer initial investment (≥ 1) | `$10,000` | **VEC** |
| `EC-019` | Minimum allowable boundary starting value (exact lower bound) | `$1` | **VEC** |
| `EC-020` | Zero starting value (strictly < 1) | `$0` | **IEC** |
| `EC-021` | Negative starting value | `-$7` | **IEC** |
| `EC-022` | Completely empty / blank starting value | `""` (empty) | **IEC** |

### EP-06: Feature: Portfolio Backtester | Input Field: `Date Range (Start Date vs End Date)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-023` | Valid chronological date range (`Start Date < End Date`) | `Start: 01/01/2010`, `End: 12/31/2023` | **VEC** |
| `EC-024` | Inverted chronological date range (`Start Date > End Date`) | `Start: 01/01/2023`, `End: 01/01/2020` | **IEC** |
| `EC-025` | Identical start and end dates (`Start Date == End Date`) | `Start: 01/01/2023`, `End: 01/01/2023` | **IEC** |
| `EC-026` | Start date far in future beyond market dataset | `Start: 01/01/2099`, `End: 01/01/2100` | **IEC** |

### EP-07: Feature: Portfolio Backtester | Input Field: `Rolling Window (months)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-027` | Standard positive integer duration in months | `60` months | **VEC** |
| `EC-028` | Zero or negative rolling window duration | `0` months / `-12` months | **IEC** |
| `EC-029` | Empty / blank rolling window | `""` (empty) | **IEC** |

### EP-08: Feature: Portfolio Backtester | Input Field: `Cashflows & Rebalancing Frequency`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-030` | Valid non-negative annual cashflow and standard rebalancing | Cashflow: `$0`, Frequency: `Yearly` | **VEC** |
| `EC-031` | Valid positive recurring contribution | Cashflow: `$500`, Frequency: `Monthly` | **VEC** |
| `EC-032` | Negative recurring cashflow amount | Cashflow: `-$500` | **IEC** |

---

## Form 4: Monte Carlo Simulator (`/monte-carlo`)

### EP-09: Feature: Monte Carlo Simulator | Input Field: `Simulation Horizon / Years`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-033` | Valid positive simulation duration in years (e.g. 1 to 50) | `30` years | **VEC** |
| `EC-034` | Zero or negative simulation horizon | `0` years / `-5` years | **IEC** |
| `EC-035` | Empty / blank simulation duration | `""` (empty) | **IEC** |

### EP-10: Feature: Monte Carlo Simulator | Input Field: `Number of Simulations`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-036` | Standard positive iteration count (e.g. 100 to 10,000) | `1,000` | **VEC** |
| `EC-037` | Zero or negative iteration count | `0` / `-100` | **IEC** |

---

## Form 5: Safe Withdrawal Rate Calculator (`/safe-withdrawal-rate-calculator`)

### EP-11: Feature: Safe Withdrawal Rate | Input Field: `Withdrawal Rate (%)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-038` | Standard sustainable withdrawal rate percentage (e.g. 1% to 10%) | `4.0%` | **VEC** |
| `EC-039` | Extreme unrealistic withdrawal percentage (> 100%) | `120%` | **IEC** |
| `EC-040` | Negative withdrawal percentage | `-3.5%` | **IEC** |

---

## Form 6: Backtest Optimizer (`/backtest-optimizer`)

### EP-12: Feature: Backtest Optimizer | Input Field: `Weight Constraints (Min / Max %)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-041` | Valid consistent bounds (`0% ≤ Min ≤ Max ≤ 100%`) | `Min: 10%`, `Max: 50%` | **VEC** |
| `EC-042` | Inconsistent bounds (`Min > Max`) | `Min: 60%`, `Max: 40%` | **IEC** |
| `EC-043` | Negative weight bound | `Min: -10%`, `Max: 50%` | **IEC** |

---

## Form 7: Efficient Frontier (`/efficient-frontier`)

### EP-13: Feature: Efficient Frontier | Input Field: `Asset Selection Count`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-044` | Multi-asset selection capable of forming a curve (≥ 2 assets) | 3 assets (`VTI`, `BND`, `GLD`) | **VEC** |
| `EC-045` | Single asset selection (cannot calculate variance curve) | 1 asset (`VTI`) | **IEC** |
| `EC-046` | Zero assets selected | 0 assets | **IEC** |

---

## Form 8: Contact Form (`/contact`)

### EP-14: Feature: Contact Form | Input Field: `Email`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-047` | Valid academic / institutional email address | `i243137@isb.nu.edu.pk` | **VEC** |
| `EC-048` | Invalid email format lacking domain structure | `user@` | **IEC** |
| `EC-049` | Empty mandatory email field | `""` (empty) | **IEC** |

### EP-15: Feature: Contact Form | Input Field: `Subject`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-050` | Valid non-empty subject within length bound (1 to 120 chars) | `Inquiry on backtest data` (25 chars) | **VEC** |
| `EC-051` | Excessively long subject exceeding max character limit (> 120 chars) | `A` × 125 chars | **IEC** |
| `EC-052` | Empty subject string | `""` (empty) | **IEC** |

### EP-16: Feature: Contact Form | Input Field: `Message Body`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-053` | Valid message body within permitted range (10 to 5,000 chars) | `This is a verified test inquiry.` (32 chars) | **VEC** |
| `EC-054` | Message body below minimum required length (< 10 chars) | `ijklmno` (7 chars) | **IEC** |
| `EC-055` | Completely empty / blank message body | `""` (empty) | **IEC** |
| `EC-056` | Message body exceeding maximum boundary (> 5,000 chars) | `X` × 5,005 chars | **IEC** |

### EP-17: Feature: Contact Form | Input Field: `Security Verification (Cloudflare Turnstile)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-057` | Cloudflare verification token completed successfully | Captcha token verified (`Success!`) | **VEC** |
| `EC-058` | Unverified / pending / expired captcha token | Captcha token missing / unsolved | **IEC** |

---

## Form 9: Lump Sum vs DCA (`/lumpsum-vs-dca`)

### EP-18: Feature: Lump Sum vs DCA | Input Field: `Initial Lump Sum ($)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-059` | Standard positive initial lump sum amount (≥ 1) | `$50,000` | **VEC** |
| `EC-060` | Zero or negative initial investment amount | `$0` / `-$1,000` | **IEC** |
| `EC-061` | Empty / blank initial amount | `""` (empty) | **IEC** |

### EP-19: Feature: Lump Sum vs DCA | Input Field: `DCA Monthly Contribution ($)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-062` | Standard positive periodic DCA contribution amount | `$1,000` | **VEC** |
| `EC-063` | Negative DCA contribution amount | `-$200` | **IEC** |

---

## Form 10: Time Value of Money Calculator (`/time-value-of-money`)

### EP-20: Feature: TVM Calculator | Input Field: `Starting Value ($)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-064` | Standard positive initial principal amount (≥ 1) | `$10,000` | **VEC** |
| `EC-065` | Zero or negative initial principal | `$0` / `-$500` | **IEC** |
| `EC-066` | Empty / blank starting value | `""` (empty) | **IEC** |

### EP-21: Feature: TVM Calculator | Input Field: `Monthly Contribution ($)`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-067` | Valid monthly contribution within verified range ($0 to $100,000) | `$1,000` | **VEC** |
| `EC-068` | Exact lower boundary contribution ($0) | `$0` | **VEC** |
| `EC-069` | Negative monthly contribution (< $0) | `-$500` | **IEC** |
| `EC-070` | Excessively high monthly contribution (> $100,000) | `$150,000` | **IEC** |
| `EC-071` | Completely empty / blank contribution field | `""` (empty) | **IEC** |

---

## Form 11: Rebalancing Sensitivity (`/rebalancing-sensitivity`)

### EP-22: Feature: Rebalancing Sensitivity | Input Field: `Rebalance Frequency Selection`
| EC ID | Equivalence Class Description | Representative Value | Type |
|:---:|---|---|:---:|
| `EC-072` | Standard recognized rebalancing frequency | `Yearly` / `Monthly` | **VEC** |
| `EC-073` | No rebalancing (buy and hold) strategy | `Never` | **VEC** |
| `EC-074` | Unselected / invalid rebalance configuration | `null` / unselected | **IEC** |
