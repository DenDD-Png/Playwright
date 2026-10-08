from urllib.parse import quote

from playwright.sync_api import expect

from pages.base_page import BasePage, BASE_URL


class SearchPage(BasePage):
    """Страница результатов поиска /search/?q=..."""

    URL = BASE_URL + "/search/?q={query}"

    def __init__(self, page):
        super().__init__(page)
        # Ищем по test-id: get_by_text находит ещё и __next-route-announcer__
        self.result_title = page.get_by_test_id("search-title__wrapper")
        self.books = page.get_by_test_id("art__wrapper")
        self.first_filter_toggle = page.locator("xpath=(//div[@class='uik-toggle-KN8WZd'])[1]")
        self.russian_language_checkbox = page.locator("label[for='languages-ru']")
        self.russian_chip = page.locator("[data-testid='chip-content']:has-text('Русский')")

    #Actions

    def toggle_first_filter(self) -> None:
        self.first_filter_toggle.click()

    def apply_russian_filter(self) -> None:
        self.russian_language_checkbox.check()

    #Checks

    def should_be_opened(self, query: str) -> None:
        expect(self.page).to_have_url(self.URL.format(query=quote(query)))

    def should_show_results_for(self, query: str) -> None:
        expect(self.result_title).to_have_text(f"Результаты поиска «{query}»", ignore_case=True)

    def should_have_books_count(self, count: int) -> None:
        expect(self.books).to_have_count(count, timeout=5000)

    def should_show_russian_chip(self) -> None:
        expect(self.russian_chip).to_be_visible()

    def should_show_text(self, text: str) -> None:
        expect(self.page.get_by_text(text).first).to_be_visible()
