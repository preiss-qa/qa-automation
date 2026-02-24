# QA Automation Framework (API + E2E)

![CI](https://github.com/preiss-qa/qa-automation/actions/workflows/ci.yml/badge.svg)

CI Status: API and E2E test suites are executed automatically on every push. Smoke tests act as a quality gate.

A production-grade QA automation framework combining API contract testing and browser-based E2E testing.  
Built with scalability, maintainability, and CI integration in mind.

---

## Architecture Overview

This framework is structured in layers:

- **API layer** (pytest + requests) for fast backend validation
- **Contract validation layer** (Pydantic models) to detect breaking API changes
- **E2E layer** (Playwright + Page Object Model) for critical user journeys
- **CI quality gate** (GitHub Actions) running API and E2E suites with HTML reports as artifacts

---

### Simple Architecture Diagram

```text
Developer
   |
   v
pytest
 ├─ API tests (requests)
 │    └─ Contract validation (Pydantic models)
 └─ E2E tests (Playwright)
      └─ Page Object Model
   |
   v
GitHub Actions CI
 ├─ API job → report-api
 └─ E2E job → report-e2e
```

## 🚀 Overview

This project demonstrates how to design and implement a structured and scalable test automation framework using modern tools and clean architecture principles.

It includes:

- API contract validation using Pydantic
- Browser-based E2E testing using Playwright
- Marker-based suite selection (smoke / regression / api / e2e)
- Automated CI execution via GitHub Actions
- HTML reporting for local and CI runs

The framework demonstrates production-style QA automation design with clean architecture and CI-integrated quality gates.

---

## 🛠 Tech Stack

- **Python**
- **pytest**
- **requests** (API testing)
- **Playwright** (E2E browser automation)
- **Pydantic** (API contract validation)
- **pytest-html** (report generation)
- **GitHub Actions** (CI/CD)

---

## 🏗 Architecture & Design Principles

This framework follows several professional automation patterns:

- Separation of API and UI test layers
- Page Object Pattern for E2E maintainability
- Central configuration management
- Reusable pytest fixtures
- Marker-based test selection
- Contract-based API validation
- CI-integrated quality gates

---

## 📂 Project Structure

```
qa_automation/
│
├── models/              # Pydantic models for API contract validation
├── utils/               # Reusable API helpers
├── pages/               # Page Objects for E2E tests
│
tests/
├── api/                 # API contract tests
├── e2e/                 # Browser-based E2E tests
└── conftest.py          # Shared fixtures (API base URL, Playwright page)

.github/
└── workflows/           # CI configuration
```

---

## 🧪 Testing Strategy

This project follows the **Test Pyramid** approach:

- ✅ API tests for fast and stable backend validation  
- ✅ E2E tests for critical user flows  
- ✅ Smoke suite for CI quality gate  
- ✅ Regression suite for full validation  

### API Contract Testing

API responses are validated against strict Pydantic models to ensure:

- Correct response structure
- Required fields are present
- Correct data types
- Stable API contracts

If the API structure changes unexpectedly, tests fail immediately.

---

## ▶️ Local Setup (Windows PowerShell)

### 1️⃣ Create virtual environment

```
python -m venv .venv
.\.venv\Scripts\activate
```

### 2️⃣ Install dependencies

```
python -m pip install -r requirements.txt
```

### 3️⃣ Install Playwright browsers

```
python -m playwright install
```

---

## ▶️ Running Tests

### Run all tests

```
pytest -q
```

### Run API tests only

```
pytest -m api -q
```

### Run E2E tests only

```
pytest -m e2e -q
```

### Run smoke suite

```
pytest -m smoke -q
```

### Run regression suite

```
pytest -m regression -q
```

---

## 📊 HTML Reporting

Generate a local test report:

```
pytest --html=report.html
```

The report includes:

- Test summary
- Execution time
- Pass / Fail overview
- Environment metadata

CI reports are uploaded as workflow artifacts.

---

## ⚙ Continuous Integration (GitHub Actions)

The CI pipeline:

- Runs automatically on push and pull requests
- Executes smoke tests as a quality gate
- Uploads HTML reports as artifacts
- Ensures reproducible test execution in a clean environment

Smoke tests act as a **quality gate** before changes are considered stable.

---

## 🎯 What This Repository Demonstrates

- Structured QA automation design
- Clean separation of concerns
- API contract validation
- Scalable test architecture
- CI-integrated automation strategy
- Professional repository documentation

---

## 👤 Author

QA Automation Engineer focused on:

- API testing
- E2E automation
- Test architecture design
- CI/CD integration
- Quality engineering best practices
