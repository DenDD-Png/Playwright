from urllib.parse import quote

import allure
from playwright.sync_api import expect

from config import BASE_URL
from pages.base_page import BasePage


class SearchPage(BasePage):
    """Страница результатов поиска /search/?q=..."""

    path = "/search/"

    def __init__(self, page):
        super().__init__(page)
        # Ищем по test-id: get_by_text находит ещё и __next-route-announcer__
        self.title = page.get_by_test_id("search-title__wrapper")
        self.first_filter_toggle = page.locator("xpath=(//div[@class='uik-toggle-KN8WZd'])[1]")
        self.russian_language_checkbox = page.locator("label[for='languages-ru']")

    @staticmethod
    def url_for(query: str) -> str:
        return f"{BASE_URL}/search/?q={quote(query)}"

    def should_be_opened_for(self, query: str):
        self.should_have_url(self.url_for(query))

    def should_show_results_for(self, query: str):
        with allure.step(f"Показаны результаты поиска «{query}»"):
            expect(self.title).to_have_text(f"Результаты поиска «{query}»", ignore_case=True)

    def toggle_first_filter(self):
        with allure.step("Переключить первый фильтр"):
            self.first_filter_toggle.click()

    def check_russian_language(self):
        with allure.step("Отметить фильтр «Русский язык»"):
            self.russian_language_checkbox.check()

    def should_show_text(self, text: str):
        expect(self.page.get_by_text(text).first).to_be_visible()
