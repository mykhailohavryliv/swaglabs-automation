import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
    PASSWORD = os.getenv("PASSWORD")


settings = Settings()

if not settings.PASSWORD:
    raise ValueError("PASSWORD env var not set")
