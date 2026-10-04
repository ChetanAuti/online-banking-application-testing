# Online Banking Application Testing

## Project Overview

This project focuses on end-to-end testing of an Online Banking Application using Manual Testing, API Testing, and Automation Testing.

The application was tested to verify functional behavior, UI behavior, API responses, and stability of major banking features.

### QA Testing Workflow

Requirement → Test Planning → Test Case Design → Test Execution → Bug Reporting → API Testing → Automation Testing → Regression Testing → Final Test Report

---

## Application Under Test

**Application:** ParaBank Demo Banking Application

**Application URL:** https://parabank.parasoft.com/parabank/

**Testing Type:** Web Application Testing

---

## Project Objectives

- Verify major banking functionalities.
- Identify functional defects.
- Create and execute test cases.
- Perform positive and negative testing.
- Perform API testing using Postman.
- Automate test cases using Selenium and Python.
- Execute automation tests using PyTest.
- Perform regression testing.
- Report and document defects.
- Prepare a final test summary report.

---

## Modules Tested

1. Login
2. Registration
3. Dashboard
4. Account Balance
5. Fund Transfer
6. Transaction History
7. Forgot Password

---

## Testing Types

- Functional Testing
- UI Testing
- Positive Testing
- Negative Testing
- Smoke Testing
- Sanity Testing
- Regression Testing
- API Testing
- SQL / Database Testing Concepts
- Automation Testing

---

## Tools & Technologies

- **Selenium WebDriver** – Web Automation
- **Python** – Automation Programming
- **PyTest** – Test Execution Framework
- **Postman** – API Testing
- **Microsoft Excel** – Test Case Management
- **Jira** – Defect Tracking
- **Git** – Version Control
- **GitHub** – Source Code Management

---

## Test Case Management

Test cases were prepared and executed using Excel.

Test case details include:

- Test Case ID
- Test Scenario
- Test Description
- Preconditions
- Test Steps
- Expected Result
- Actual Result
- Status
- Priority
- Severity
- Test Type

The Excel file also contains API Testing test cases and results.

---

## Automation Testing

Selenium WebDriver with Python and PyTest was used to automate the major application modules.

### Automated Modules

- Login
- Registration
- Dashboard
- Account Balance
- Fund Transfer
- Transaction History
- Forgot Password

### Installation

```bash
pip install selenium pytest
```

### Run All Tests

```bash
python -m pytest -v
```

### Run Specific Test Module

```bash
python -m pytest test_login.py -v
```

---

## API Testing

API testing was performed using Postman.

### API Endpoint

```text
GET https://parabank.parasoft.com/parabank/services/bank/accounts/{accountId}
```

### API Test Scenarios

- Valid Account ID
- Invalid Account ID
- Invalid Endpoint
- Response Data Validation
- Status Code Validation
- Response Time Validation

The API test cases and results are documented in the Excel test case file.

---

## Bug Report

### BUG_TRANSFER_001

**Title:** System allows transfer with zero amount

**Module:** Fund Transfer

**Severity:** Medium

**Priority:** Medium

**Status:** Open

### Steps to Reproduce

1. Login to the application.
2. Navigate to Transfer Funds.
3. Select the source account.
4. Select the destination account.
5. Enter `0` as the transfer amount.
6. Click the Transfer button.

### Expected Result

The system should reject the zero amount and display an appropriate validation message.

### Actual Result

The system successfully processed the zero amount transfer and displayed the transfer completion message.

---

## Regression Testing

Regression testing was performed by re-executing the completed automated test cases to verify that previously working functionality remained stable.

The Zero Amount Fund Transfer defect remained reproducible and was documented as an open defect.

---

## Test Execution Summary

| Module | Result |
|---|---|
| Login | PASS |
| Registration | PASS |
| Dashboard | PASS |
| Account Balance | PASS |
| Fund Transfer | 5 PASS / 1 FAIL |
| Transaction History | PASS |
| Forgot Password | PASS |
| API Testing | PASS |

---

## Project Structure

```text
Online-Banking-Testing/
│
├── README.md
├── Banking_Test_Cases.xlsx
│
├── Automation/
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_dashboard.py
│   ├── test_account_balance.py
│   ├── test_fund_transfer.py
│   ├── test_transaction_history.py
│   └── test_forgot_password.py
│
├── Bug-Reports/
│   └── BUG_TRANSFER_001.xlsx
│
└── Test-Report/
    └── Final_Test_Summary_Report.pdf
```

---

## Skills Demonstrated

- Manual Testing
- Test Case Design
- Test Scenario Design
- Functional Testing
- Positive Testing
- Negative Testing
- UI Testing
- Smoke Testing
- Sanity Testing
- Regression Testing
- API Testing
- Selenium Automation
- Python
- PyTest
- SQL / Database Testing
- Postman
- Bug Reporting
- Test Documentation
- Git
- GitHub

---

## Project Outcome

This project demonstrates an end-to-end Software Testing and QA workflow for an Online Banking Application.

The project includes:

- Manual test case preparation
- Test execution
- Functional testing
- API testing
- Selenium automation
- PyTest execution
- Regression testing
- Defect identification
- Bug reporting
- Final test summary reporting

A genuine functional defect was identified in the Fund Transfer module where the application accepted a zero amount transfer.

---

## Author

**Chetan Auti**

**Role:** QA / Software Testing Fresher

**Skills:** Manual Testing | Selenium | Python | PyTest | API Testing | Postman | SQL | Excel | Git | GitHub
