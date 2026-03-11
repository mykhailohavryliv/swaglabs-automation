import os

class Settings:
    BASE_URL = os.getenv('BASE_URL', 'https://www.saucedemo.com')
    BROWSER = os.getenv('BROWSER', 'chromium')
    HEADLESS = os.getenv('HEADLESS', 'true').lower() == 'true'
    DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '10000'))

settings = Settings()
