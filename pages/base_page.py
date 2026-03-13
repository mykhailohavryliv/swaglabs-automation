from typing import Union
from playwright.sync_api import Page, Locator
from config.settings import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        self.page.goto(f"{settings.BASE_URL}{path}")

    def click(self, locator: Union[str, Locator]):
        if isinstance(locator, str):
            self.page.locator(locator).click()
        else:
            locator.click()

    def fill(self, locator: Union[str, Locator], text: str):
        if isinstance(locator, str):
            self.page.locator(locator).fill(text)
        else:
            locator.fill(text)

    def is_visible(self, locator: Union[str, Locator]) -> bool:
        if isinstance(locator, str):
            return self.page.locator(locator).is_visible()
        else:
            return locator.is_visible()

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)
