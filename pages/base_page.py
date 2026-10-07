import allure
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect

from config import SCREENSHOTS_DIR


class BasePage:
    """Общие для всех страниц действия и элементы шапки сайта."""

    path = "/"

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id("search__input")
        self.search_button = page.get_by_test_id("search__button")
        self.logo = page.get_by_alt_text("Логотип Литрес")
        self.cookie_accept_button = page.get_by_test_id("cookieAcceptPopup__accept")

    def open(self):
        with allure.step(f"Открыть страницу {self.path}"):
            self.page.goto(self.path)
            self.page.wait_for_load_state("load")
        return self

    def search(self, query: str):
        with allure.step(f"Найти «{query}» через кнопку «Найти»"):
            self._submit_search(query, self.search_button.click)

    def search_by_enter(self, query: str):
        with allure.step(f"Найти «{query}» через Enter"):
            self._submit_search(query, lambda: self.page.keyboard.press("Enter"))

    def _submit_search(self, query: str, submit, attempts: int = 3):
        # Пока Next.js не закончил гидратацию, React сбрасывает введённый текст
        # и поиск не уходит. Повторяем, пока не откроется страница результатов.
        for attempt in range(attempts):
            self.search_input.fill(query)
            submit()
            try:
                self.page.wait_for_url("**/search/**", timeout=3000)
                return
            except PlaywrightTimeoutError:
                if attempt == attempts - 1:
                    raise

    def click_logo(self):
        with allure.step("Нажать на логотип Литрес"):
            self.logo.click()

    def accept_cookies(self):
        with allure.step("Принять куки"):
            self.cookie_accept_button.click()

    def should_have_title(self, title: str):
        with allure.step(f"Заголовок вкладки: «{title}»"):
            expect(self.page).to_have_title(title)

    def should_have_url(self, url: str):
        with allure.step(f"URL страницы: {url}"):
            expect(self.page).to_have_url(url)

    def take_screenshot(self, name: str):
        path = SCREENSHOTS_DIR / f"{name}.png"
        self.page.screenshot(path=str(path))
        allure.attach.file(str(path), name=name, attachment_type=allure.attachment_type.PNG)
