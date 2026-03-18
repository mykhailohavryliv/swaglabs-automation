from pages.base_page import BasePage
from playwright.sync_api import Page
from config.settings import settings


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.username_input = page.get_by_test_id("username")
        self.password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.error_message_container = page.get_by_test_id("error")

    def navigate_to_login(self):
        super().navigate()
        self.username_input.wait_for()

    def login(self, username="standard_user", password=settings.PASSWORD):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message_container.inner_text()
