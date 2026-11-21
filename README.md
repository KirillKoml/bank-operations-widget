# Виджет банковских операций

Консольная программа показывает 5 последних успешных (EXECUTED) банковских операций из файла JSON.

<img width="395" height="383" alt="screenshot" src="https://github.com/user-attachments/assets/2e04aa4e-b696-4515-a59a-a8f917ffa23e" />

## Возможности
- сортировка операций по дате (от новых к старым)
- маскировка номера карты/счёта: Visa Platinum 1246 **** **** 3576
- вывод даты, описания, направления перевода и суммы с валютой

## Стек
Python 3 (только стандартная библиотека: json, pathlib)

## Запуск

```bash
git clone https://github.com/KirillKoml/bank-operations-widget.git
cd bank-operations-widget
python main.py
```

## Тесты
8 автотестов на pytest


