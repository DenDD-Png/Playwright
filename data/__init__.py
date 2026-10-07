import json

from config import DATA_DIR


def load_json(name: str):
    """Читает data/<name>.json."""
    with open(DATA_DIR / f"{name}.json", encoding="utf-8") as f:
        return json.load(f)
