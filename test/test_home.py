import pytest

from data import data_id, load_pages_data
from pages.base_page import BASE_URL


@pytest.mark.smoke
@pytest.mark.parametrize("td", load_pages_data(ids=["home"]), ids=data_id)
def test_home_title(home, td):
    home.should_have_title(td.title)

@pytest.mark.parametrize("td", load_pages_data(ids=["audiobooks"]), ids=data_id)
def test_audiobooks_title(home, td):
    home.open_audiobooks()
    home.should_have_title(td.title)

@pytest.mark.parametrize("td", load_pages_data(ids=["start_here"]), ids=data_id)
def test_logo_from_start_here(home, td):
    home_data = load_pages_data(ids=["home"])[0]
    home.open_start_here()
    home.should_have_title(td.title)
    home.click_logo()
    home.should_have_url(BASE_URL + home_data.path)

@pytest.mark.parametrize("td", load_pages_data(ids=["promotions"]), ids=data_id)
def test_logo_from_promotions(home, td):
    home_data = load_pages_data(ids=["home"])[0]
    home.open(td.path)
    home.click_logo()
    home.should_have_url(BASE_URL + home_data.path)
    home.should_show_start_here_link()

def test_youtube_icon(home):
    home.should_show_youtube_icon()
