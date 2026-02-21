# QA Automation Framework (API + E2E)

![CI](https://github.com/preiss-qa/qa-automation/actions/workflows/ci.yml/badge.svg)

A structured test automation project using **Python**, **pytest**, and **Playwright**.
Includes API tests, browser-based E2E tests, test tagging (smoke/regression), and CI execution via GitHub Actions.

## Tech Stack
- Python
- pytest
- requests (API)
- Playwright (E2E)
- GitHub Actions (CI)
- pytest-html (report)

## Project Structure
- `tests/api/` API tests
- `tests/e2e/` E2E browser tests
- `tests/conftest.py` shared pytest fixtures (API client + Playwright page)
- `utils/api/` reusable API client
- `pages/` Page Objects for E2E maintainability
- `config.py` central configuration (URLs, credentials, headless mode)

## Run Locally

### Setup
Create and activate venv (Windows PowerShell):
- `python -m venv venv`
- `.\venv\Scripts\Activate.ps1`

Install dependencies:
- `python -m pip install -r requirements.txt`

Install Playwright browsers:
- `python -m playwright install`

### Run all tests
- `python -m pytest -q`

### Run suites by marker
API only:
- `python -m pytest -q -m api`

E2E only:
- `python -m pytest -q -m e2e`

Smoke suite (fast checks):
- `python -m pytest -q -m smoke`

Regression suite:
- `python -m pytest -q -m regression`

### Generate HTML report
- `python -m pytest --html=report.html`

## CI (GitHub Actions)
A GitHub Actions workflow runs the **smoke suite** on every push to `main` and on pull requests.
The HTML report is uploaded as a workflow artifact.

## Notes
This project demonstrates maintainable test automation patterns:
- central config
- reusable fixtures
- Page Object Pattern for UI tests
- marker-based suite selection for CI strategy
