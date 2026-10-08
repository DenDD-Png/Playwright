from playwright.sync_api import Page
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@pytest.fixture(autouse=True)
def open_browser(page: Page):
    HomePage(page).open()
    page.wait_for_timeout(2500)
    yield

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def result(page: Page) -> SearchPage:
    return SearchPage(page)

@pytest.fixture
def login(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open_form()
    return login_page
