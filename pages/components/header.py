from playwright.sync_api import Page


class Header:

    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.search_input = self.page.get_by_placeholder("Искать на Литрес")
        self.search_button = self.page.get_by_role("button", name="Найти")

    #Actions

    def search(self, query: str, submit_with_enter: bool = False) -> None:
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            self.search_button.click()
