"""Автотесты модели Operation на pytest."""

import pytest

from models.operation import Operation

SAMPLE = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "15850.15",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счёт 98854127650462711873",
}


@pytest.fixture
def operation() -> Operation:
    return Operation(SAMPLE)


def test_date_format(operation):
    assert operation.date() == "26.08.2019 Перевод организации"


def test_mask_card(operation):
    assert operation.from_to() == (
        "Maestro 1596 83** **** 5199 ->Счёт **1873"
    )


def test_without_from():
    op = Operation({"date": "2019-08-26T10:50:58.294041",
                    "to": "Счёт 98854127650462711873"})
    assert op.from_to() == "->Счёт **1873"


def test_amount(operation):
    assert operation.amount() == "15850.15 руб."


def test_last_executed_operation():
    from utils.operations import last_executed_operation

    ops = [{"state": "EXECUTED", "date": f"2024-0{i}-01"} for i in range(7, 0, -1)]
    result = last_executed_operation(ops)
    assert len(result) == 5
    assert result[0]["date"] == "2024-07-01"


def test_last_executed_skips_non_executed():
    from utils.operations import last_executed_operation

    ops = [{"state": "EXECUTED", "date": "2024-05-01"},
           {"state": "CANCELED", "date": "2024-06-01"},
           {"state": "EXECUTED", "date": "2024-04-01"}]
    result = last_executed_operation(ops)
    assert len(result) == 2


def test_sort_then_last_executed():
    from utils.operations import last_executed_operation, sort_by_date

    ops = [{"state": "EXECUTED", "date": f"2024-0{i}-01"} for i in range(1, 8)]
    result = last_executed_operation(sort_by_date(ops))
    assert result[0]["date"] == "2024-07-01"
    assert result[-1]["date"] == "2024-03-01"

    def test_load_operations_skips_empty():
        from utils.operations import load_operations
        import json
        import tempfile
        from pathlib import Path

        data = [
            {},
            {"state": "EXECUTED", "date": "2024-06-01T00:00:00"},
            "",
            {"state": "CANCELED", "date": "2024-05-01T00:00:00"},
        ]
        with tempfile.NamedTemporaryFile("w", suffix=".json",
                                         encoding="utf8", delete=False) as f:
            json.dump(data, f, ensure_ascii=False)
            tmp = Path(f.name)

        result = load_operations(tmp)
        assert len(result) == 2
        assert result[0]["date"] == "2024-06-01"


def test_load_operations_skips_empty():
    from utils.operations import load_operations
    import json
    import tempfile
    from pathlib import Path

    data = [
        {},
        {"state": "EXECUTED", "date": "2024-06-01T00:00:00"},
        "",
        {"state": "CANCELED", "date": "2024-05-01T00:00:00"},
    ]
    with tempfile.NamedTemporaryFile("w", suffix=".json",
                                     encoding="utf8", delete=False) as f:
        json.dump(data, f, ensure_ascii=False)
        tmp = Path(f.name)

    result = load_operations(tmp)
    assert len(result) == 2
    assert result[0]["date"] == "2024-06-01T00:00:00"
    assert result[1]["state"] == "CANCELED"