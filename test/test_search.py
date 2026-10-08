import pytest

from data import data_id, load_empty_search_data, load_pages_data, load_search_data


@pytest.mark.smoke
@pytest.mark.parametrize("td", load_search_data(ids=["python_books", "game_of_thrones"]), ids=data_id)
def test_search_by_button(home, result, td):
    home.search(td.query)
    result.should_be_opened(td.query)
    result.should_show_results_for(td.query)
    result.should_have_books_count(td.expected_results_count)

@pytest.mark.parametrize("td", load_search_data(ids=["python_books", "game_of_thrones"]), ids=data_id)
def test_search_by_enter(home, result, td):
    home.search(td.query, submit_with_enter=True)
    result.should_be_opened(td.query)
    result.should_show_results_for(td.query)
    result.should_have_books_count(td.expected_results_count)

@pytest.mark.parametrize("td", load_search_data(ids=["self_teacher_python"]), ids=data_id)
def test_search_page_title(home, result, td):
    home.search(td.query)
    result.should_show_results_for(td.query)
    result.should_have_title(td.page_title)

@pytest.mark.parametrize("td", load_empty_search_data(ids=["popular_queries"]), ids=data_id)
def test_empty_search(home, result, td):
    home.search("")
    result.should_show_text(td.suggestion)

@pytest.mark.parametrize("td", load_empty_search_data(ids=["popular_queries"]), ids=data_id)
def test_empty_search_from_start_here(home, result, td):
    start_here = load_pages_data(ids=["start_here"])[0]
    home.open_start_here()
    home.should_have_title(start_here.title)
    home.search("")
    result.should_show_text(td.suggestion)

@pytest.mark.parametrize("td", load_search_data(ids=["python_books"]), ids=data_id)
def test_toggle_filter(home, result, td):
    home.search(td.query)
    result.should_be_opened(td.query)
    result.toggle_first_filter()
    result.take_screenshot("search_filter_toggled")

@pytest.mark.parametrize("td", load_search_data(ids=["python_books", "game_of_thrones"]), ids=data_id)
def test_russian_language_filter(home, result, td):
    home.search(td.query, submit_with_enter=True)
    result.should_be_opened(td.query)
    result.should_have_books_count(td.expected_results_count)
    result.apply_russian_filter()
    result.should_show_russian_chip()
