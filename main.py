"""Точка входа: вывод пяти последних успешных операций."""

from models.operation import Operation
from utils.operations import last_executed_operation, load_operations, sort_by_date


def main() -> None:
    operations = sort_by_date(load_operations())
    for item in last_executed_operation(operations):
        op = Operation(item)
        print(op.date())
        print(op.from_to())
        print(op.amount())


if __name__ == "__main__":
    main()
