import re

import allure
import pytest
from playwright.sync_api import Page

from config import BASE_URL, SCREENSHOTS_DIR
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Настройки контекста браузера: page.goto("/") откроет BASE_URL."""
    return {
        **browser_context_args,
        "base_url": BASE_URL,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "ru-RU",
    }


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page).open()


@pytest.fixture
def search_page(home_page: HomePage) -> SearchPage:
    """Страница поиска; поиск запускается с главной."""
    return SearchPage(home_page.page)


@pytest.fixture
def login_page(home_page: HomePage) -> LoginPage:
    return LoginPage(home_page.page).open_form()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """При падении теста сохраняет скриншот в screenshots/ и прикладывает его к Allure."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    page = item.funcargs.get("page")
    if page is None:
        return
    safe_name = re.sub(r"[^\w-]+", "_", item.name)
    path = SCREENSHOTS_DIR / f"FAILED_{safe_name}.png"
    page.screenshot(path=str(path), full_page=True)
    allure.attach.file(str(path), name="screenshot", attachment_type=allure.attachment_type.PNG)
