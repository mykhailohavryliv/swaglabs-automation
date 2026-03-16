import allure
from pages.login_page import LoginPage
from playwright.sync_api import expect


@allure.feature("Login")
class TestLogin:

    @allure.story("Successful Login")
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate_to_login()

        login_page.login("standard_user")

        # Verify successful login by checking the URL or a specific element on the inventory page
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.locator(".title")).to_have_text("Products")

    @allure.story("Locked Out User")
    def test_locked_out_user(self, page):
        login_page = LoginPage(page)
        login_page.navigate_to_login()

        login_page.login("locked_out_user")

        # Verify error message
        expect(login_page.error_message_container).to_be_visible()
        error_text = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_text
