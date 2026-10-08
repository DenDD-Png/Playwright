from playwright.sync_api import Locator
from pages.base_page import BasePage

class HomePage(BasePage):

    #Locators
    @property
    def search_input(self) -> Locator:

        return self.page.get_by_placeholder("Искать на Литрес")

    @property
    def search_button(self) -> Locator:
        return self.page.get_by_role("button", name="Найти")

    #Actions

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_button.click()