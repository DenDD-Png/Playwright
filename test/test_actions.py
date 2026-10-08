from playwright.sync_api import Page, expect
import pytest
from conftest import load_search_data


@pytest.mark.parametrize("query", ["Python","Игра престолов","Стивен Кинг"])

def test_main_actions(home, result, query):
    #page.get_by_placeholder("Искать на Литрес").fill("python")
    #page.get_by_role("button", name="Найти").click()
    #expect(page).to_have_url(f"https://www.litres.ru/search/?q={query}")
    #books = page.get_by_test_id("art__wrapper")
    #page.check("label[for='languages-ru']")
    query = "Игра Престолов"
    home.search(query, submit_with_enter=True)
    result.should_be_opened(query)
    expect(result.result_title).to_contain_text(query)
    expect(result.books).to_have_count(24, timeout=5000)
    result.apply_russian_filter()
    expect(result.russian_chip).to_be_visible()

@pytest.mark.parametrize("td", load_search_data(ids=["python_books","game_of_thrones"]))
def test_main(home, result, td):
    home.search(td.query, submit_with_enter=True)
    result.should_be_opened(td.query)
    expect(result.result_title).to_contain_text(td.query)
    expect(result.books).to_have_count(td.expected_results_count, timeout=5000)
    result.apply_russian_filter()
    expect(result.russian_chip).to_be_visible()
