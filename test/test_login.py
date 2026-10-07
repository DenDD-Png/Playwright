import allure
import pytest

from data import load_json
from pages.login_page import LoginPage

DATA = load_json("login_data")


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Форма входа открывается")
    @pytest.mark.smoke
    def test_login_form_opens(self, login_page: LoginPage):
        login_page.should_be_opened()

    @allure.title("Ошибка при пустом поле почты")
    def test_empty_email_error(self, login_page: LoginPage):
        login_page.submit()
        login_page.should_show_error(DATA["empty_field_error"])

    @allure.title("Поле почты принимает ввод")
    def test_email_input(self, login_page: LoginPage):
        login_page.enter_email(DATA["sample_email"])
        login_page.should_have_email(DATA["sample_email"])
