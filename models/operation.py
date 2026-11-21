"""Модель банковской операции: форматирование даты,
маскировка реквизитов и вывод суммы."""


class Operation:
    def __init__(self, operation: dict):
        self.operation = operation

    def date(self) -> str:
        """Возвращает дату в формате ДД.ММ.ГГГГ и описание операции."""
        raw_date = self.operation["date"]
        date_ = f"{raw_date[8:10]}.{raw_date[5:7]}.{raw_date[0:4]}"
        return f"{date_} {self.operation['description']}"

    def _mask_number(self, number: str) -> str:
        """Маскирует номер карты или счёта."""
        name, digits = number.rsplit(" ", 1)
        if len(digits) == 16:  # карта: 1234 56** **** 5678
            return f"{name} {digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        # счёт: **1234
        return f"{name} **{digits[-4:]}"

    def from_to(self) -> str:
        """Возвращает направление перевода с замаскированными реквизитами."""
        parts = []
        if "from" in self.operation:
            parts.append(self._mask_number(self.operation["from"]))
        parts.append("->" + self._mask_number(self.operation["to"]))
        return " ".join(parts)

    def amount(self) -> str:
        """Возвращает сумму и валюту операции."""
        info = self.operation["operationAmount"]
        return f"{info['amount']} {info['currency']['name']}"
