from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.username_input = "input[data-test='username']"
        self.password_input = "input[data-test='password']"
        self.login_button = "input[data-test='login-button']"
        self.error_message_container = "h3[data-test='error']"

    def navigate_to_login(self):
        super().navigate()
        self.wait_for_selector(self.username_input)

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.page.locator(self.error_message_container).inner_text()
