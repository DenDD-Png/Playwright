import allure
import pytest

from data import load_json
from pages.home_page import HomePage

DATA = load_json("pages_data")


@allure.feature("Главная страница")
class TestHome:

    @allure.title("Заголовок главной страницы")
    @pytest.mark.smoke
    def test_home_title(self, home_page: HomePage):
        home_page.should_have_title(DATA["home_title"])

    @allure.title("Переход в «Аудиокниги»")
    def test_audiobooks_title(self, home_page: HomePage):
        home_page.open_audiobooks()
        home_page.should_have_title(DATA["audiobooks_title"])

    @allure.title("Логотип со страницы «С чего начать» ведёт на главную")
    def test_logo_from_start_here(self, home_page: HomePage):
        home_page.open_start_here()
        home_page.should_have_title(DATA["start_here_title"])
        home_page.click_logo()
        home_page.should_have_url(DATA["home_url"])

    @allure.title("Логотип со страницы акций ведёт на главную")
    def test_logo_from_promotions(self, home_page: HomePage):
        home_page.page.goto(DATA["promotions_path"])
        home_page.click_logo()
        home_page.should_have_url(DATA["home_url"])
        home_page.should_show_start_here_link()

    @allure.title("Иконка YouTube в подвале")
    def test_youtube_icon(self, home_page: HomePage):
        home_page.should_show_youtube_icon()
