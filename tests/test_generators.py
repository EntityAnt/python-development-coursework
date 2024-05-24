from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(get_transactions: Any) -> None:
    usd_transactions = filter_by_currency(get_transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_transaction_descriptions(get_transactions: Any) -> None:
    descriptions = transaction_descriptions(get_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1000033334444, 1000033334444, "0001 0000 3333 4444"),
        (1000033334445, 1000033334445, "0001 0000 3333 4445"),
        (1000033334446, 1000033334446, "0001 0000 3333 4446"),
        (1000033334447, 1000033334447, "0001 0000 3333 4447"),
    ],
)
def test_card_number_generator(start: int, end: int, expected: str) -> None:
    card_number = card_number_generator(start, end)
    assert next(card_number) == expected
