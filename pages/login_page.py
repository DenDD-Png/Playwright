from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Форма входа, открывается из шапки кнопкой «Войти»."""

    def __init__(self, page):
        super().__init__(page)
        self.login_tab = page.get_by_test_id("tab-login")
        self.email_label = page.get_by_text("Почта или логин")
        self.email_input = page.get_by_test_id("auth__input--enterEmailOrLogin")
        self.continue_button = page.get_by_test_id("auth__button--continue")
        self.input_error = page.get_by_test_id("textbox--input__error")

    #Actions

    def open_form(self) -> None:
        self.login_tab.click()

    def enter_email(self, email: str) -> None:
        self.email_input.fill(email)

    def submit(self) -> None:
        self.continue_button.click()

    #Checks

    def should_be_opened(self) -> None:
        expect(self.email_label).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.continue_button).to_be_visible()

    def should_show_error(self, text: str) -> None:
        expect(self.input_error).to_have_text(text)

    def should_have_email(self, email: str) -> None:
        expect(self.email_input).to_have_value(email)
