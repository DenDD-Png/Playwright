from urllib.parse import quote

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.components.header import Header


class SearchResultPage(BasePage):

    URL = "https://www.litres.ru/search/?q={query}"

    def __init__(self, page: Page):
        super().__init__(page)

        #Components
        self.header = Header(page)

        #Locators
        self.result_title = self.page.get_by_test_id("search-title__wrapper")
        self.books = self.page.get_by_test_id("art__wrapper")
        self.russian_fill = self.page.locator("label[for='languages-ru']")
        self.russian_chip = self.page.locator("[data-testid='chip-content']:has-text('Русский')")

    #Actions

    def apply_russian_filter(self) -> None:

        self.russian_fill.check()

    #Checks

    def should_be_opened(self, query: str) -> None:

        expect(self.page).to_have_url(self.URL.format(query=quote(query)))
