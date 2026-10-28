# ☕ Coffee Shop Order System

### Lab 6 — Code Coverage & Branch Coverage Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Testing-Pytest-0A9EDC?logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Code%20Coverage-100%25-brightgreen" alt="Code Coverage">
  <img src="https://img.shields.io/badge/Branch%20Coverage-100%25-brightgreen" alt="Branch Coverage">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
</p>

---

## 📌 Project Overview

This repository contains the implementation and testing work for **Lab 6: Code and Branch Coverage Analysis**.

The lab focuses on evaluating software test quality by writing and executing automated tests against a Python-based Coffee Shop Order System.

The application processes coffee shop orders by calculating order totals, handling customization options, enforcing allergy-related safety rules, and checking espresso machine conditions.

The primary objective is to achieve **at least 90% code coverage and 90% branch coverage** through systematic test-case design and execution.

---

## 🎯 Objectives

* Understand the fundamentals of code coverage and branch coverage.
* Design and execute automated test cases using `pytest`.
* Measure code coverage using the `coverage.py` tool.
* Identify and exercise conditional branches within the application.
* Verify application behaviour across different input conditions and edge cases.
* Generate coverage reports and capture terminal evidence.
* Maintain a structured GitHub repository with separate commits for code coverage and branch coverage work.

---

## 📊 Coverage Results

| Metric                |    Result |          Requirement | Status     |
| --------------------- | --------: | -------------------: | ---------- |
| Code Coverage         |  **100%** |                ≥ 90% | ✅ Achieved |
| Branch Coverage       |  **100%** |                ≥ 90% | ✅ Achieved |
| Code Coverage Tests   | 20 passed | Successful execution | ✅ Passed   |
| Branch Coverage Tests | 20 passed | Successful execution | ✅ Passed   |

### 🔍 Code Coverage

Code coverage measures the proportion of executable statements exercised during test execution.

**Result: 100% statement coverage**

![Code Coverage Report](code_coverage.png)

### 🌿 Branch Coverage

Branch coverage measures whether the possible outcomes of conditional decisions have been exercised by the test suite.

**Result: 100% branch coverage**

![Branch Coverage Report](branch_coverage.png)

> **Note:** The results above represent the local test execution results recorded for this submission.

---

## 🧪 Testing Approach

The application is tested using two dedicated test files.

### 1. Code Coverage Testing

**Test file:** `CodeCoverageTest_xxxx_application.py`

This test suite evaluates application behaviour across supported inputs, invalid inputs, edge cases, and relevant error-handling scenarios.

Run the tests:

```bash
python -m pytest CodeCoverageTest_xxxx_application.py -v
```

Measure code coverage:

```bash
python -m coverage erase
python -m coverage run --source=coffee_shop_order -m pytest CodeCoverageTest_xxxx_application.py
python -m coverage report -m
```

### 2. Branch Coverage Testing

**Test file:** `BranchCoverageTest_xxxx_application.py`

This test suite evaluates conditional paths and branch outcomes in the application to measure branch coverage.

Run the tests:

```bash
python -m pytest BranchCoverageTest_xxxx_application.py -v
```

Measure branch coverage:

```bash
python -m coverage erase
python -m coverage run --branch --source=coffee_shop_order -m pytest BranchCoverageTest_xxxx_application.py
python -m coverage report -m
```

---

## 🛠️ Technologies Used

| Technology  | Purpose                                       |
| ----------- | --------------------------------------------- |
| Python      | Application implementation and test execution |
| Pytest      | Automated testing framework                   |
| Coverage.py | Code and branch coverage measurement          |
| Git         | Version control                               |
| GitHub      | Repository hosting and submission             |

---

## 📁 Repository Structure

```text
Lab 6/
│
├── coffee_shop_order.py
│
├── test_coffee_shop.py
│
├── CodeCoverageTest_xxxx_application.py
│
├── BranchCoverageTest_xxxx_application.py
│
├── Coverage_Analysis_Report.md
│
├── code_coverage.png
│
├── branch_coverage.png
│
└── README.md
```

### File Descriptions

| File                                     | Description                                    |
| ---------------------------------------- | ---------------------------------------------- |
| `coffee_shop_order.py`                   | Main Python application being tested           |
| `test_coffee_shop.py`                    | Existing application test file                 |
| `CodeCoverageTest_xxxx_application.py`   | Test suite for code coverage analysis          |
| `BranchCoverageTest_xxxx_application.py` | Test suite for branch coverage analysis        |
| `Coverage_Analysis_Report.md`            | Summary of coverage results and analysis       |
| `code_coverage.png`                      | Screenshot showing the code coverage results   |
| `branch_coverage.png`                    | Screenshot showing the branch coverage results |
| `README.md`                              | Project overview, instructions, and results    |

---

## ⚙️ Installation and Execution

### Prerequisites

Ensure the following are installed:

* Python 3
* pip
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/raviteja2028tech/L6_L7_03_coffee_shop_order.git
```

### Step 2: Navigate to the Lab Directory

```bash
cd "L6_L7_03_coffee_shop_order/Lab 6"
```

### Step 3: Install Required Testing Packages

```bash
python -m pip install pytest coverage
```

### Step 4: Execute Code Coverage Tests

```bash
python -m coverage erase
python -m coverage run --source=coffee_shop_order -m pytest CodeCoverageTest_xxxx_application.py
python -m coverage report -m
```

### Step 5: Execute Branch Coverage Tests

```bash
python -m coverage erase
python -m coverage run --branch --source=coffee_shop_order -m pytest BranchCoverageTest_xxxx_application.py
python -m coverage report -m
```

---

## 📈 Analysis and Conclusion

The testing process achieved **100% statement coverage and 100% branch coverage** for the measured application during the recorded test runs.

The results indicate that all measured executable statements and branch outcomes were exercised by the corresponding test suites.

This lab demonstrates how automated testing and coverage measurement can help evaluate test completeness and identify untested application logic.

However, achieving 100% coverage does not guarantee that an application is free from defects. Test quality also depends on the correctness of assertions, the scenarios tested, and the requirements being validated.

---

## 📄 Deliverables

The repository includes the following submission components:

* ✅ Code coverage test file
* ✅ Branch coverage test file
* ✅ Code coverage terminal screenshot
* ✅ Branch coverage terminal screenshot
* ✅ Coverage analysis report
* ✅ Application source files
* ✅ GitHub version history with separate commits for the two coverage tasks

---

## 👨‍🎓 Student Information

| Field                 | Details                           |
| --------------------- | --------------------------------- |
| **Name**              | RAVITEJA                          |
| **SRN**               | PES1UG24AM001                     |
| **Course / Lab**      | Software Engineering — Lab 6      |
| **Assignment**        | Code and Branch Coverage Analysis |
| **Submission Status** | Completed                         |

---

## 🔗 Repository

**GitHub Repository:**
https://github.com/raviteja2028tech/L6_L7_03_coffee_shop_order

---

<p align="center">
  <strong>Lab 6 — Code and Branch Coverage Analysis</strong><br>
  <em>Systematic testing. Measurable coverage. Better software quality.</em>
</p>
