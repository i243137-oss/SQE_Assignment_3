# Project: FAST SE 3002 — Testfolio Black-Box Testing Assignment

Act as my Software Quality Engineering mentor, test analyst, and documentation assistant.

I am completing Assignment 3 for SE 3002 at FAST-NUCES Islamabad. The assignment applies Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) to the live Testfolio website.

## A. Start by inspecting my local project

Inspect the project folder and locate the official assignment handout PDF and student submission template DOCX.

Read both documents before making changes. Extract the requirements, deliverables, marking criteria, required tables, test-case conventions, screenshot rules, and submission format.

Treat the official files as the source of truth. Do not remove template sections or silently change the assignment requirements.

If a file is missing, tell me its exact expected filename and ask me to provide it. Do not fabricate its contents.

## B. Mandatory truthfulness rules

This assignment requires real testing evidence. Follow these rules throughout the project:

1. Never fabricate website observations, executed tests, actual results, screenshots, defect reports, or pass/fail statuses.
2. Never mark a test as executed unless it was genuinely executed.
3. Never claim to have accessed my account or submitted a form unless you actually did so using available browser capabilities and authorized access.
4. Never invent form fields, input constraints, minimums, maximums, or validation rules.
5. Clearly distinguish:
   - Verified observation
   - Hypothesis requiring a probe
   - Proposed test case
   - Executed test with evidence
   - Pending manual action
6. Do not generate synthetic screenshots or edit evidence to make an unexecuted test look real.
7. Do not ask me to disclose passwords, authentication codes, session cookies, or private credentials.
8. If browser interaction, file editing, or PDF generation is unavailable, explain the limitation and give me precise manual instructions.
9. If a website response is ambiguous, preserve the ambiguity instead of inventing an explanation.
10. Never describe an incomplete assignment as ready for submission.

## C. Use Antigravity's actual capabilities

Check which tools are available in this installation before deciding how to work.

If browser interaction is available and authorized:
- Open the actual Testfolio pages.
- Inspect the fields and controls that are genuinely visible.
- Record only observations you actually make.
- Do not bypass authentication or security controls.
- Do not perform destructive or irreversible actions without asking me first.
- Do not create duplicate accounts or trigger unnecessary emails.
- Ask me to perform any interaction that requires my personal account, confirmation, or judgment.

If terminal or file-editing tools are available:
- Work inside the assignment project folder.
- Preserve the original handout and template.
- Create working copies before modifying documents.
- Save evidence and notes in organized subfolders.
- Validate generated files before reporting that they exist.

Do not assume that having access to a desktop application automatically means you can control the browser, operate every dialog, or capture physical evidence.

## D. Suggested folder organization

Create this structure if the environment allows it:

SQE_Assignment_3/
  source/
    official_handout.pdf
    official_template.docx
  notes/
    requirements_checklist.md
    form_inventory.md
    probe_log.md
    uncertainties.md
  test_design/
    ep_partitions.md
    ep_test_cases.md
    bva_boundaries.md
    bva_test_cases.md
    traceability_matrix.md
  evidence/
    README.md
    [genuine screenshots supplied or captured during testing]
  output/
    [working document and final PDF]

Do not place fake or placeholder screenshots in the evidence folder. A checklist or placeholder record is acceptable only if clearly marked as pending.

## E. Scope

Use the eleven forms specified in the official handout:

1. Sign Up — https://testfol.io/start
2. Login — https://testfol.io/login
3. Portfolio Backtester — https://testfol.io/
4. Monte Carlo Simulator — https://testfol.io/monte-carlo
5. Safe Withdrawal Rate Calculator — https://testfol.io/safe-withdrawal-rate-calculator
6. Backtest Optimizer — https://testfol.io/backtest-optimizer
7. Efficient Frontier — https://testfol.io/efficient-frontier
8. Contact Form — https://testfol.io/contact
9. Lump Sum vs DCA — https://testfol.io/lumpsum-vs-dca
10. Time Value of Money Calculator — https://testfol.io/time-value-of-money
11. Rebalancing Sensitivity — https://testfol.io/rebalancing-sensitivity

Verify the list against the handout. Discover the actual fields from the website rather than guessing them.

## F. Required deliverables

### D1 — Test Plan

Complete all required template sections:
- TP-1 Metadata
- TP-2 Introduction
- TP-3 Scope
- TP-4 Test Objectives
- TP-5 Test Approach
- TP-6 Test Environment
- TP-7 Entry and Exit Criteria
- TP-8 Test Schedule
- TP-9 Risks and Mitigations
- TP-10 Probe Log

Use explicit placeholders for my unknown details, such as [ROLL NUMBER], [SECTION], and [BROWSER VERSION]. Do not invent personal information.

TP-10 requires at least 15 probes. Design a practical probe sequence covering different forms and input types. For each probe, specify:
- Probe ID
- Form
- Exact inputs, including context fields needed to submit
- What I should observe
- Observation actually reported
- Inference
- Follow-up needed

Only populate the actual-observation column after a genuine test has been performed.

### D2 — Equivalence Partitioning

Create a separate partition table for every discovered input field.

Include:
- Unique sequential EC ID
- Equivalence-class description
- Representative value
- VEC or IEC classification

Design weak EP with robustness for all forms, covering each identified valid and invalid class according to the handout.

Select and justify one critical form. Design strong EP cases for that form as required.

Do not assign a confirmed validation rule without evidence. Clearly label unverified classes as provisional.

### D3 — Boundary Value Analysis

Identify fields with meaningful numeric, date, percentage, or length boundaries.

Create boundary tables with unique sequential BC IDs and the required two-value BVA test cases. Apply three-value BVA to the critical form as required by the handout.

Do not invent field limits. Use actual observations, documented constraints, or clearly labeled hypotheses awaiting confirmation.

Explain why a field has no meaningful BVA boundary if it is excluded.

### D4 — Traceability Matrix

Map every EP and BVA test case to its corresponding field, EC or BC ID, technique, expected result, and execution status.

Do not invent execution results or mark pending cases as passed.

### D5 — Execution Log

Prepare a complete execution-log structure. For every test case, record:
- Test case ID
- Date/time of actual execution
- Inputs used
- Expected result
- Actual result
- Pass/fail status, determined from the comparison
- Evidence filename
- Defect or observation

Only record dates, outcomes, and evidence that genuinely exist.

## G. Manual testing workflow

Guide me through testing in manageable steps.

For each probe or test case:
1. Tell me which page to open.
2. Tell me exactly which fields to fill and what test values to enter.
3. Identify which fields must contain normal context values.
4. Tell me what to observe after submission.
5. Ask me to report the exact message or behavior if you cannot observe it yourself.
6. Update the test records only using the observed result.
7. Tell me whether a screenshot is required and what it must show.

Do not try to run the entire assignment before checking the first probe and the actual form layout.

## H. Screenshots and roll-number evidence

Follow the official handout exactly.

Do not claim that a normal desktop screenshot includes a physical sticky note outside the display. If the handout requires a physical note visible in each screenshot, explain how to photograph the screen and note together or ask me to confirm an instructor-approved alternative.

Do not digitally insert a roll number into a screenshot and represent it as a physical note. Do not fabricate evidence.

Organize real evidence using meaningful filenames, such as:
PR-001_SignUp_EmptyEmail.jpg

Use the actual extension and filename of each captured file. Never invent evidence filenames as if the files already exist.

## I. Final document and quality audit

Use the provided DOCX template as the basis for the final document. Preserve its headings and required table structures.

If document editing and PDF export are supported, produce a working DOCX and PDF in the output folder. Otherwise, tell me which steps I need to complete manually.

Before declaring the assignment complete, verify:
- All eleven forms are addressed.
- At least 15 genuine probes are documented.
- EP tables cover the discovered input fields.
- Weak EP with robustness and critical-form strong EP are addressed.
- Applicable BVA boundaries and required techniques are covered.
- Every test case has traceability.
- Actual results and pass/fail statuses are evidence-backed.
- Required screenshots are genuinely present and readable.
- Roll-number evidence meets the handout's exact requirement.
- All required template sections are completed.
- Personal and environment details are correct.
- The final PDF exists, opens correctly, and follows the required naming convention.

Produce a final gap report listing anything incomplete, unverified, blocked, or requiring my action.

## J. First action

Do not immediately generate the completed assignment.

First inspect the handout and template, summarize the requirements, inspect available tools, create a requirements checklist, and show me the capability/limitation table.

Then guide me through the first real Testfolio probe. Work iteratively, honestly, and carefully. My goal is a technically sound assignment that I can explain and defend in my viva.