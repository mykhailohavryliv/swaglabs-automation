from playwright.sync_api import Page
from config.settings import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        self.page.goto(f"{settings.BASE_URL}{path}")
