from playwright.sync_api import Page
import pytest

@pytest.fixture(autouse=True)
def open_browser(page: Page):
    page.goto("https://www.litres.ru/")
    page.wait_for_timeout(2000)
    yield