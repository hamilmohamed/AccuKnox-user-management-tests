# AccuKnox - User Management Tests (Playwright + Python)

Repo: AccuKnox-user-management-tests

## Summary
Automated Playwright tests (Python) for OrangeHRM User Management:
- Add user
- Search user
- Edit user
- Validate updated details
- Delete user

## Playwright version used
Playwright for Python 1.38.0

## Setup
1. Create and activate virtualenv:
   python -m venv venv
   # macOS / Linux
   source venv/bin/activate
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1

2. Install dependencies:
   pip install -r requirements.txt

3. Install Playwright browsers:
   playwright install

## Run tests
Run all tests:
pytest -q

Run a single test:
pytest tests/test_user_management.py::test_add_user -q

## Credentials (AUT)
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
Username: Admin
Password: admin123
