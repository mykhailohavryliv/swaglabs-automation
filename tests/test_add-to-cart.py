import pytest
import allure
from config.settings import settings

from pages.login_page import LoginPage

from pages.products_page import ProductsPage


@allure.feature("Add to Cart")
class TestAddToCart:

    @pytest.fixture(autouse=True)
    def before_each(self, page):
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login("standard_user", settings.PASSWORD)
        ProductsPage(page).navigate_to_products()

    @allure.story("Add Product to Cart")
    def test_add_to_cart(self, page):
        products_page = ProductsPage(page)
        products_page.add_product_to_cart_by_number(0)
        assert products_page.get_shopping_cart_badge_count() == 1
        products_page.add_product_to_cart_by_number(1)
        assert products_page.get_shopping_cart_badge_count() == 2
