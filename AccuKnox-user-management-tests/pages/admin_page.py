from playwright.sync_api import Page
from pages.base_page import BasePage

class AdminPage(BasePage):
    def navigate_to_admin(self):
        self.page.get_by_role("link", name="Admin").click()
        self.page.wait_for_selector('h6:has-text("System Users")')

    def click_add(self):
        self.wait_and_click('button:has-text("Add")')
        self.page.wait_for_selector('h6:has-text("Add User")')

    def fill_add_user_form(self, user_data: dict):
        self.wait_and_click('label:has-text("User Role") + div')
        self.wait_and_click(f'text={user_data.get("user_role")}')
        self.wait_and_fill('input[placeholder="Type for hints..."]', user_data.get('emp_name'))
        self.page.wait_for_timeout(700)
        self.wait_and_click('.oxd-autocomplete-dropdown > div:nth-child(1)')
        self.wait_and_fill('input[name="username"]', user_data.get('username'))
        self.wait_and_click('label:has-text("Status") + div')
        self.wait_and_click(f'text={user_data.get("status")}')
        self.wait_and_fill('input[placeholder="Password"]', user_data.get('password'))
        self.wait_and_fill('input[placeholder="Confirm Password"]', user_data.get('confirm_password'))
        self.wait_and_click('button:has-text("Save")')
        self.page.wait_for_selector('div.oxd-toast-container', timeout=10000)

    def search_user(self, username: str):
        self.wait_and_fill('input[placeholder="Username"]', username)
        self.wait_and_click('button:has-text("Search")')
        self.page.wait_for_selector('div.oxd-table-body')

    def get_first_row_username(self):
        self.page.wait_for_selector('div.oxd-table-body div.oxd-table-card')
        return self.text_content('div.oxd-table-body div.oxd-table-card div.oxd-table-cell:nth-child(2)')

    def click_edit_on_user(self):
        self.wait_and_click('button[title="Edit"]')
        self.page.wait_for_selector('h6:has-text("Edit User")')

    def update_user_username(self, new_username: str):
        self.wait_and_fill('input[name="username"]', new_username)
        self.wait_and_click('button:has-text("Save")')
        self.page.wait_for_selector('div.oxd-toast-container', timeout=10000)

    def delete_user_from_search_results(self):
        self.wait_and_click('div.oxd-table-body div.oxd-table-card input[type="checkbox"]')
        self.wait_and_click('button:has-text("Delete")')
        self.wait_and_click('button:has-text("Yes, Delete")')
        self.page.wait_for_selector('div.oxd-toast-container', timeout=10000)
