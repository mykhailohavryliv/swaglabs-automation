import pytest
import allure
from playwright.sync_api import expect
from config.settings import settings


@allure.feature("Add to Cart")
class TestAddToCart:

    @pytest.fixture(autouse=True)
    def before_each(self, login_page, products_page):
        login_page.navigate_to_login()
        login_page.login("standard_user", settings.PASSWORD)
        products_page.navigate_to_products()

    @allure.story("Add Product to Cart")
    def test_add_to_cart(self, products_page):
        products_page.add_product_to_cart_by_number(0)
        expect(products_page.shopping_cart_badge).to_have_text("1")
        products_page.add_product_to_cart_by_number(1)
        expect(products_page.shopping_cart_badge).to_have_text("2")
