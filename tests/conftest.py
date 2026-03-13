import pytest
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from config.settings import settings

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    browser_type = getattr(playwright, settings.BROWSER)
    browser = browser_type.launch(
        headless=settings.HEADLESS,
        args=["--start-maximized"]
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
    )
    # Automatically start tracing for each test
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(settings.DEFAULT_TIMEOUT)
    yield page
    
@pytest.fixture(autouse=True)
def trace_on_failure(request, context: BrowserContext):
    yield
    if request.node.rep_call.failed:
        trace_path = f"test-results/trace-{request.node.name}.zip"
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set an attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
