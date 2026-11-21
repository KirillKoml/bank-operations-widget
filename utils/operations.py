"""Загрузка, сортировка и фильтрация банковских операций."""

import json
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent / "operations.json"


def load_operations(path: Path = FILE_PATH) -> list[dict]:
    """Читает JSON-файл и возвращает список операций,
    отбрасывая пустые записи и записи без даты."""
    with open(path, "r", encoding="utf8") as file:
        raw = json.load(file)
    return [item for item in raw if item and "date" in item]


def sort_by_date(operations: list[dict]) -> list[dict]:
    """Сортирует операции по дате: от новых к старым."""
    return sorted(operations, key=lambda x: x["date"], reverse=True)


def last_executed_operation(operations: list[dict], count: int = 5) -> list[dict]:
    """Возвращает последние count выполненных (EXECUTED) операций."""
    executed = [item for item in operations if item.get("state") == "EXECUTED"]
    return executed[:count]
