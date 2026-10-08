from pathlib import Path

from playwright.sync_api import Page, expect

BASE_URL = "https://www.litres.ru"
SCREENSHOTS_DIR = Path(__file__).parent.parent / "screenshots"


class BasePage:
    """Общие для всех страниц действия и элементы шапки сайта."""

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id("search__input")
        self.search_button = page.get_by_test_id("search__button")
        self.logo = page.get_by_alt_text("Логотип Литрес")
        self.cookie_accept_button = page.get_by_test_id("cookieAcceptPopup__accept")

    #Actions

    def open(self, path: str = "/") -> None:
        self.page.goto(BASE_URL + path)

    def search(self, query: str, submit_with_enter: bool = False) -> None:
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            self.search_button.click()

    def click_logo(self) -> None:
        self.logo.click()

    def accept_cookies(self) -> None:
        self.cookie_accept_button.click()

    def take_screenshot(self, name: str) -> None:
        self.page.screenshot(path=str(SCREENSHOTS_DIR / f"{name}.png"))

    #Checks

    def should_have_title(self, title: str) -> None:
        expect(self.page).to_have_title(title)

    def should_have_url(self, url: str) -> None:
        expect(self.page).to_have_url(url)
