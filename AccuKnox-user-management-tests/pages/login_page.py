from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.goto(self.URL)
        self.page.wait_for_selector('input[name="username"]')

    def login(self, username: str, password: str):
        self.wait_and_fill('input[name="username"]', username)
        self.wait_and_fill('input[name="password"]', password)
        self.wait_and_click('button[type="submit"]')
