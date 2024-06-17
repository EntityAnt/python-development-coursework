from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator:
    """Принимает список словарей с банковскими операциями, возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.
    """

    transactions_by_currency = filter(
        lambda item: item["operationAmount"]["currency"]["code"] == currency, transactions_list
    )
    for trans in transactions_by_currency:
        yield trans


def transaction_descriptions(transactions_list: list[dict]) -> Generator:
    """Генератор, который принимает список словарей и возвращает описание каждой операции по очереди."""
    for trans in transactions_list:
        yield trans["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров банковских карт, который должен генерировать номера карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне
    """
    card_numbers = ["0" * (16 - len(str(i))) + str(i) for i in list(range(start, end + 1))]
    card_numbers_str = []
    for key, item in enumerate(card_numbers):
        card_numbers_str.append(f"{item[:4]} {item[4:8]} {item[8:12]} {item[12:]}")
        yield card_numbers_str[key]
