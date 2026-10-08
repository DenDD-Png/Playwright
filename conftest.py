from playwright.sync_api import Page
import pytest

from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage

@pytest.fixture(autouse=True)
def open_browser(page: Page):
    page.goto("https://www.litres.ru/")
    page.wait_for_timeout(2500)
    yield

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def result(page: Page) -> SearchResultPage:
    return SearchResultPage(page)
