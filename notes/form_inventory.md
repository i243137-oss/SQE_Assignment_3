# Form & Input Field Inventory

This file inventories all 11 in-scope tools and forms on [testfol.io](https://testfol.io) along with their discovered input fields and control types.

*Note: Fields will be verified during live browser exploration to ensure 100% accuracy with the current live deployment.*

| # | Form / Tool | URL | Identified Fields / Controls | Status |
|---|---|---|---|---|
| 1 | Create Account (Sign Up) | `https://testfol.io/start` | Email, Password, Confirm Password (if present), Submit button | Discovered via Probing |
| 2 | Sign In (Login) | `https://testfol.io/login` | Email, Password, Remember Me, Submit button | Discovered via Probing |
| 3 | Portfolio Backtester (CRITICAL FORM) | `https://testfol.io/` | **Parameters**: Date range (dropdown), Start Date (`mm/dd/yyyy`), End Date (`mm/dd/yyyy`), Starting Value (`$`, default 10,000), Rolling Window (months, default 60), Pick benchmark ticker (checkbox), Adjust for inflation (checkbox), Extended withdrawal stats (checkbox).<br>**Cashflow legs**: Annual cashflow growth (`%`), Cashflow ($), Cashflow Frequency, Cashflow Offset, Inflation adjustment.<br>**Portfolios**: ADD EMPTY, ADD PRESET, Asset Tickers, Asset Allocations (%), Rebalance Frequency. | Discovered & Verified (Evidence: `PR-004_Backtester_Parameters_Top.png`, `PR-005_Backtester_Cashflow_Portfolios.png`) |
| 4 | Monte Carlo Simulator | `https://testfol.io/monte-carlo` | Initial Amount, Cashflows, Simulation Horizon/Years, Number of Simulations, Assets & Percentages | Discovered via Probing |
| 5 | Safe Withdrawal Rate Calculator | `https://testfol.io/safe-withdrawal-rate-calculator` | Initial Portfolio Value, Withdrawal Strategy/Rate, Time Horizon, Asset Allocation | Discovered via Probing |
| 6 | Backtest Optimizer | `https://testfol.io/backtest-optimizer` | Assets, Min/Max Weight bounds, Optimization Metric/Objective (Sharpe, Return, etc.) | Discovered via Probing |
| 7 | Efficient Frontier | `https://testfol.io/efficient-frontier` | Assets selection, Constraints, Return/Volatility settings | Discovered via Probing |
| 8 | Contact Form | `https://testfol.io/contact` | **Fields**: Name (text, optional), Email (email, required, validated format), What's this about (dropdown, e.g. 'Product Question'), Subject (text, character counter 0–120), Message (textarea, character counter, min 10 to max 5,000 chars), Security Check (Cloudflare Turnstile captcha), 'Send message' submit button.<br>**Responses**: Error banner *"Message must be at least 10 characters."*, Success banner *"Message sent. We will get back to you soon."* | Discovered & Verified (Evidence: `PR-015_ContactForm_MessageMin10Chars_Error.png`, `PR-016_ContactForm_MessageSent_Success.png`) |
| 9 | Lump Sum vs DCA | `https://testfol.io/lumpsum-vs-dca` | Initial Lump Sum, DCA Monthly Amount, Duration, Assets | Discovered via Probing |
| 10 | Time Value of Money Calculator | `https://testfol.io/time-value-of-money` | **Cashflow schedule**: Contribution Frequency (dropdown, default 'Monthly'), Contribution timing (dropdown, default 'End of period').<br>**Variables**: X variable (dropdown, default 'Years'), Y variable (dropdown, default 'Ending Value'), Color variable (dropdown, default 'CAGR'), Specify Years range (checkbox), Specify Ending Value range (checkbox), Specify CAGR levels (checkbox).<br>**Other Inputs**: Starting Value ($ numeric, default 10,000), Monthly contribution ($ numeric, default 1,000).<br>**Action**: CALCULATE button. | Discovered & Verified (Evidence: `PR-010_TimeValueOfMoney_FormDiscovery.png`) |
| 11 | Rebalancing Sensitivity | `https://testfol.io/rebalancing-sensitivity` | Assets & Weights, Rebalancing Frequencies, Time Range | Discovered via Probing |
