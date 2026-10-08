import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

# Тестовые данные
DATA_DIR = Path(__file__).parent


@dataclass
class SearchTestData:
    id: str
    query: str
    expected_results_count: int
    page_title: Optional[str] = None


@dataclass
class EmptySearchTestData:
    id: str
    suggestion: str


@dataclass
class PageTestData:
    id: str
    path: Optional[str] = None
    title: Optional[str] = None


@dataclass
class LoginTestData:
    id: str
    email: str
    expected_error: Optional[str] = None


def _load(file_name: str, key: str, data_class, ids: Optional[Iterable[str]]):
    with open(DATA_DIR / file_name, encoding="utf-8") as f:
        raw_data = json.load(f)[key]
    if ids is not None:
        raw_data = [item for item in raw_data if item["id"] in ids]

    return [data_class(**item) for item in raw_data]


def load_search_data(ids: Optional[Iterable[str]] = None):
    return _load("search_data.json", "search_input", SearchTestData, ids)


def load_empty_search_data(ids: Optional[Iterable[str]] = None):
    return _load("search_data.json", "empty_search", EmptySearchTestData, ids)


def load_pages_data(ids: Optional[Iterable[str]] = None):
    return _load("pages_data.json", "pages", PageTestData, ids)


def load_login_data(ids: Optional[Iterable[str]] = None):
    return _load("login_data.json", "login_input", LoginTestData, ids)


def data_id(td) -> str:
    """Имя кейса в выводе pytest: test_search[python_books]."""
    return td.id
