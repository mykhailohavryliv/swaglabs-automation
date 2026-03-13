from pages.base_page import BasePage
from playwright.sync_api import Page


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.page_title = page.locator(".title")
        self.product_titles = page.locator("div[data-test='inventory-item-name']")
        self.product_descriptions = page.locator("div[data-test='inventory-item-desc']")
        self.product_prices = page.locator("div[data-test='inventory-item-price']")
        self.product_add_to_cart_buttons = page.locator(
            "button[data-test*='add-to-cart']"
        )
        self.shppoing_cart_badge = page.locator(".shopping_cart_badge")

    def navigate_to_products(self):
        # Navigate to the products (inventory) page and wait for it to load.
        super().navigate("/inventory.html")
        self.page_title.wait_for()

    def add_product_to_cart_by_number(self, product_number):
        button = self.product_add_to_cart_buttons.nth(product_number)
        button.click()

    def get_shopping_cart_badge_count(self):
        if self.shppoing_cart_badge.is_visible():
            return int(self.shppoing_cart_badge.inner_text())
        return 0
