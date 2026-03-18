import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Login")
class TestLogin:

    @allure.story("Login Scenarios")
    @pytest.mark.parametrize(
        "username, is_success, expected_url, expected_text, error_message",
        [
            (
                "standard_user",
                True,
                "https://www.saucedemo.com/inventory.html",
                "Products",
                None,
            ),
            (
                "locked_out_user",
                False,
                None,
                None,
                "Epic sadface: Sorry, this user has been locked out.",
            ),
        ],
    )
    def test_login(
        self,
        login_page,
        page,
        username,
        is_success,
        expected_url,
        expected_text,
        error_message,
    ):
        login_page.navigate_to_login()
        login_page.login(username)

        if is_success:
            expect(page).to_have_url(expected_url)
            expect(page.locator(".title")).to_have_text(expected_text)
        else:
            expect(login_page.error_message_container).to_be_visible()
            expect(login_page.error_message_container).to_contain_text(error_message)
