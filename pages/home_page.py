import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class HomePage(BasePage):
    """Главная страница litres.ru."""

    path = "/"

    def __init__(self, page):
        super().__init__(page)
        self.start_here_link = page.get_by_role("link", name="С чего начать")
        self.audiobooks_link = page.get_by_role("link", name="Аудиокниги").first
        self.youtube_icon = page.locator("xpath=//img[@alt='YouTube']")

    def open_start_here(self):
        with allure.step("Перейти в «С чего начать»"):
            self.start_here_link.click()

    def open_audiobooks(self):
        with allure.step("Перейти в «Аудиокниги»"):
            self.audiobooks_link.click()

    def should_show_start_here_link(self):
        expect(self.start_here_link).to_be_visible()

    def should_show_youtube_icon(self):
        expect(self.youtube_icon).to_be_visible()
