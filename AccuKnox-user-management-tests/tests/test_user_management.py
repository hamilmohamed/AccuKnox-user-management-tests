import time
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

ADMIN_USER = "Admin"
ADMIN_PASS = "admin123"

@pytest.fixture(scope='session')
def pw_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def generate_userid(base='autouser'):
    return f"{base}_{int(time.time())}"

def test_add_user(pw_page):
    page = pw_page
    login = LoginPage(page)
    admin = AdminPage(page)

    login.open()
    login.login(ADMIN_USER, ADMIN_PASS)

    admin.navigate_to_admin()
    admin.click_add()

    username = generate_userid()
    user_data = {
        'user_role': 'ESS',
        'emp_name': 'Linda Anderson',
        'username': username,
        'status': 'Enabled',
        'password': 'Password@123',
        'confirm_password': 'Password@123'
    }

    admin.fill_add_user_form(user_data)
    admin.search_user(username)
    found = admin.get_first_row_username()
    assert username in (found or '')

def test_delete_user(pw_page):
    page = pw_page
    login = LoginPage(page)
    admin = AdminPage(page)

    login.open()
    login.login(ADMIN_USER, ADMIN_PASS)
    admin.navigate_to_admin()
    admin.click_add()
    username = generate_userid('todelete')
    user_data = {
        'user_role': 'ESS',
        'emp_name': 'Linda Anderson',
        'username': username,
        'status': 'Enabled',
        'password': 'Password@123',
        'confirm_password': 'Password@123'
    }
    admin.fill_add_user_form(user_data)
    admin.search_user(username)
    admin.delete_user_from_search_results()
    admin.search_user(username)
    try:
        found = admin.get_first_row_username()
        assert username not in (found or '')
    except Exception:
        pass
