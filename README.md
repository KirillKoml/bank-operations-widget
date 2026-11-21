# Виджет банковских операций

Учебный проект (курсовая работа Skypro): консольная программа показывает
5 последних успешных (EXECUTED) банковских операций из файла JSON.

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

<img width="1280" height="1024" alt="2026-11-21_17-11-46" src="https://github.com/user-attachments/assets/40864419-8da5-4d37-bc74-6f2979210717" />
