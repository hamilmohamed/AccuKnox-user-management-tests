from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def wait_and_click(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)
        self.page.click(selector)

    def wait_and_fill(self, selector: str, text: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)
        self.page.fill(selector, text)

    def text_content(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)
        return self.page.text_content(selector)
