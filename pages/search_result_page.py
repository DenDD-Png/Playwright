from urllib.parse import quote

from playwright.sync_api import Locator, expect
from pages.base_page import BasePage


class SearchResultPage(BasePage):

    URL = "https://www.litres.ru/search/?q={query}"

    #Locators
    @property
    def result_title(self) -> Locator:

        return self.page.get_by_test_id("search-title__wrapper")

    @property
    def books(self) -> Locator:

        return self.page.get_by_test_id("art__wrapper")

    @property
    def russian_fill(self) -> Locator:

        return self.page.locator("label[for='languages-ru']")

    @property
    def russian_chip(self) -> Locator:

        return self.page.locator("[data-testid='chip-content']:has-text('Русский')")

    #Actions

    def apply_russian_filter(self) -> None:

        self.russian_fill.check()

    #Checks

    def should_be_opened(self, query: str) -> None:

        expect(self.page).to_have_url(self.URL.format(query=quote(query)))