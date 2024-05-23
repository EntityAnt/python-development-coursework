from src.generators import filter_by_currency, transactions, transaction_descriptions, card_number_generator


def test_filter_by_currency() -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_transaction_descriptions() -> None:
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator() -> None:
    assert card_number_generator(1000033334444, 1000033334449) == [
        "0001 0000 3333 4444",
        "0001 0000 3333 4445",
        "0001 0000 3333 4446",
        "0001 0000 3333 4447",
        "0001 0000 3333 4448",
        "0001 0000 3333 4449",
    ]
