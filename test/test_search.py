import allure
import pytest

from data import load_json
from pages.home_page import HomePage
from pages.search_page import SearchPage

DATA = load_json("search_data")


@allure.feature("Поиск")
class TestSearch:

    @allure.title("Поиск через кнопку «Найти»: {query}")
    @pytest.mark.smoke
    @pytest.mark.parametrize("query", DATA["queries"])
    def test_search_by_button(self, search_page: SearchPage, query):
        search_page.search(query)
        search_page.should_be_opened_for(query)
        search_page.should_show_results_for(query)

    @allure.title("Поиск через Enter: {query}")
    @pytest.mark.parametrize("query", DATA["queries"])
    def test_search_by_enter(self, search_page: SearchPage, query):
        search_page.search_by_enter(query)
        search_page.should_show_results_for(query)

    @allure.title("Заголовок вкладки на странице результатов")
    def test_search_page_title(self, search_page: SearchPage):
        item = DATA["titled_query"]
        search_page.search(item["query"])
        search_page.should_show_results_for(item["query"])
        search_page.should_have_title(item["title"])

    @allure.title("Пустой поиск показывает популярные запросы")
    def test_empty_search(self, search_page: SearchPage):
        search_page.search_button.click()
        search_page.should_show_text(DATA["empty_search_suggestion"])

    @allure.title("Пустой поиск со страницы «С чего начать»")
    def test_empty_search_from_start_here(self, home_page: HomePage):
        home_page.open_start_here()
        home_page.should_have_title(load_json("pages_data")["start_here_title"])
        search_page = SearchPage(home_page.page)
        search_page.search_button.click()
        search_page.should_show_text(DATA["empty_search_suggestion"])

    @allure.title("Переключение фильтра в результатах поиска")
    def test_toggle_filter(self, search_page: SearchPage):
        search_page.search("python")
        search_page.should_be_opened_for("python")
        search_page.toggle_first_filter()
        search_page.take_screenshot("search_filter_toggled")

    @allure.title("Фильтр по русскому языку")
    def test_russian_language_filter(self, search_page: SearchPage):
        search_page.search("python")
        search_page.should_be_opened_for("python")
        search_page.check_russian_language()
        search_page.accept_cookies()
        search_page.take_screenshot("search_russian_filter")
