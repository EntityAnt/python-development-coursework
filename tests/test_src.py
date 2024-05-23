import pytest

from src.masks import counting_files_and_directories, get_account_mask, get_card_number_mask
from src.processing import filter_for_dict, sort_list_to_date
from src.widget import get_date_from_str, get_number_from_string


# +++++++++++++++++++++++ Для masks ++++++++++++++++++++++++++++++++
@pytest.mark.parametrize("num_card, expected", [("7000792289606361", "7000 79** **** 6361")])
def test_get_card_number_mask(num_card: str, expected: str) -> None:
    assert get_card_number_mask(num_card) == expected


@pytest.mark.parametrize("account, expected", [("73654108430135874305", "**4305")])
def test_get_account_mask(account: str, expected: str) -> None:
    assert get_account_mask(account) == expected


@pytest.mark.parametrize(
    "recursive, expected",
    [(False, {"files": 5, "folders": 1}), (True, {"files": 9, "folders": 1})],
)
def test_counting_files_and_directories(recursive: bool, expected: str) -> None:
    assert counting_files_and_directories(recursive=recursive) == expected


# +++++++++++++++++++++++ Для widget ++++++++++++++++++++++++++++++++
@pytest.mark.parametrize(
    "string, expected",
    [
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_get_number_from_string(string: str, expected: str) -> None:
    assert get_number_from_string(string) == expected


def test_get_date_from_str() -> None:
    assert get_date_from_str("2018-07-11T02:26:18.671407") == "11.07.2018"


# +++++++++++++++++++++++ Для processing ++++++++++++++++++++++++++++++++


def test_filter_for_dict(
        get_list_dict: list[dict], get_list_dict_executed: list[dict], get_list_dict_canceled: list[dict]
) -> None:
    assert filter_for_dict(get_list_dict) == get_list_dict_executed
    assert filter_for_dict(get_list_dict, "CANCELED") == get_list_dict_canceled


def test_sort_list_to_date(
        get_list_dict: list[dict], get_sort_list_to_date_true: list[dict], get_sort_list_to_date_false: list[dict]
) -> None:
    assert sort_list_to_date(get_list_dict) == get_sort_list_to_date_true
    assert sort_list_to_date(get_list_dict, reverse=False) == get_sort_list_to_date_false
