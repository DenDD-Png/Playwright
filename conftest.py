from playwright.sync_api import Page
import pytest
from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage
from pathlib  import Path
from dataclasses import dataclass
from typing import Optional, Iterable
import json

# Тестовыве данные
DATA_DIR = Path(__file__).parent / "test_data"

@dataclass
class SeacrhTestData:
    id: str
    query:str
    expected_results_count: int

def load_search_data(ids: Optional[Iterable[str]] = None):
    with open(DATA_DIR / "search_data.json", encoding="utf-8") as f:
        rew_data = json.load(f)["search_input"]
    if ids is not None:
        rew_data = [item for item in rew_data if item["id"] in ids]

    return [
        SeacrhTestData(
            id = item["id"],
            query = item["query"],
            expected_results_count = item["expected_results_count"])
        for item in rew_data
    ]

@pytest.fixture(autouse=True)
def open_browser(page: Page):
    page.goto("https://www.litres.ru/")
    page.wait_for_timeout(2500)
    yield

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def result(page: Page) -> SearchResultPage:
    return SearchResultPage(page)
