from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.username_input = page.locator("input[data-test='username']")
        self.password_input = page.locator("input[data-test='password']")
        self.login_button = page.locator("input[data-test='login-button']")
        self.error_message_container = page.locator("h3[data-test='error']")

    def navigate_to_login(self):
        super().navigate()
        self.username_input.wait_for()

    def login(self, username, password):
        self.password_input.fill(password)
        self.username_input.fill(username)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message_container.inner_text()
