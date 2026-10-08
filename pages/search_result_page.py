from idlelib import query

from playwright.sync_api import Locator
from pages.base_page import BasePage


class SearchResultPage(BasePage):

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