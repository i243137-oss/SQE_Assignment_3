# Deliverable D3 (Layer 1) — Boundary Value Analysis (BVA) Tables

This document defines all meaningful input boundaries identified across the 11 in-scope tools on [testfol.io](https://testfol.io).
Each boundary is assigned a unique sequential `BC-xxx` ID and cross-referenced with its corresponding Equivalence Class (`EC ID`) from Deliverable D2.

---

## 1. Boundary Table (All Applicable Input Fields)

| BC ID | Feature / Form | Input Field | EC ID | Boundary Description | Boundary Value (Inferred from Probing) |
|:---:|---|---|:---:|---|---|
| `BC-001` | Auth Modal (`/start`, `/login`) | Password | `EC-007` | Minimum password length required to activate submit button client-side (lower bound) | `1 character` |
| `BC-002` | Portfolio Backtester (`/`) | Asset Allocation Sum | `EC-014` | Lower exact bound for total portfolio asset allocation percentage | `100%` |
| `BC-003` | Portfolio Backtester (`/`) | Asset Allocation Sum | `EC-014` | Upper exact bound for total portfolio asset allocation percentage | `100%` |
| `BC-004` | Portfolio Backtester (`/`) | Starting Value ($) | `EC-019` | Absolute minimum allowable initial starting capital (lower bound) | `$1` |
| `BC-005` | Portfolio Backtester (`/`) | Start Date vs End Date | `EC-023` | Relational chronological threshold: Start Date must be strictly prior to End Date | `Start Date = End Date - 1 day` |
| `BC-006` | Portfolio Backtester (`/`) | Rolling Window (months) | `EC-027` | Minimum duration for calculating rolling performance metrics (lower bound) | `1 month` |
| `BC-007` | Monte Carlo Simulator (`/monte-carlo`) | Simulation Horizon (Years) | `EC-033` | Minimum time horizon for stochastic multi-year path modeling (lower bound) | `1 year` |
| `BC-008` | Safe Withdrawal Rate (`/safe-withdrawal`) | Withdrawal Rate (%) | `EC-038` | Minimum allowable non-negative withdrawal percentage (lower bound) | `0.0%` |
| `BC-009` | Contact Form (`/contact`) | Message Body Length | `EC-054` | Minimum required character length for message inquiry body (lower bound) | `10 characters` |
| `BC-010` | Contact Form (`/contact`) | Message Body Length | `EC-056` | Maximum allowable character length for message inquiry body (upper bound) | `5,000 characters` |
| `BC-011` | Contact Form (`/contact`) | Subject Length | `EC-051` | Maximum allowable character length for inquiry subject line (upper bound) | `120 characters` |
| `BC-012` | Lump Sum vs DCA (`/lumpsum-vs-dca`) | Initial Lump Sum ($) | `EC-059` | Minimum initial lump sum amount for comparative strategy analysis (lower bound) | `$1` |
| `BC-013` | Time Value of Money (`/time-value-of-money`) | Monthly Contribution ($) | `EC-068` | Minimum allowable periodic contribution amount (lower bound) | `$0` |
| `BC-014` | Time Value of Money (`/time-value-of-money`) | Monthly Contribution ($) | `EC-070` | Maximum allowable periodic contribution amount (upper bound) | `$100,000` |
| `BC-015` | Time Value of Money (`/time-value-of-money`) | Starting Value ($) | `EC-064` | Minimum initial present capital for TVM calculation (lower bound) | `$1` |

---

## 2. Professional Engineering Justification for Excluded Fields

In accordance with Software Quality Engineering principles, BVA applies specifically to ordered, continuous, or countable domains (numeric amounts, dates, string lengths, and percentages). The following fields are intentionally **excluded** from BVA:

1. **Rebalancing Frequency (Dropdown)**: A discrete, unordered nominal enumeration (`None`, `Monthly`, `Quarterly`, `Yearly`). There is no arithmetic ordering or numeric boundary between "Monthly" and "Yearly".
2. **Contribution Timing (Dropdown)**: A binary discrete state (`Beginning of period` vs `End of period`).
3. **Email Address Content**: String formatting is governed by regular expression syntax and domain structure rather than length thresholds.
4. **Cloudflare Turnstile Captcha**: A cryptographic token verification representing a discrete state (`Verified` vs `Unverified`), with no numeric boundary.
5. **Checkbox Toggles (e.g., Adjust for inflation, Total return)**: Discrete boolean flags (`true` / `false`) which are exhaustively tested under EP.
