import os

import pytest

from src.masks import get_account_mask, get_card_number_mask, counting_files_and_directories
from src.processing import sort_list_to_date, filter_for_dict
from src.widget import get_number_from_string, get_date_from_str


# +++++++++++++++++++++++ Для masks ++++++++++++++++++++++++++++++++
@pytest.mark.parametrize("num_card, expected", [("7000792289606361", '7000 79** **** 6361')])
def test_get_card_number_mask(num_card, expected):
    assert get_card_number_mask(num_card) == expected


@pytest.mark.parametrize("account, expected", [("73654108430135874305", '**4305')])
def test_get_account_mask(account, expected):
    assert get_account_mask(account) == expected


@pytest.mark.parametrize("path, recursive, expected", [(os.getcwd(), False, {'files': 3, 'folders': 1}),
                                                       (os.getcwd(), True, {'files': 6, 'folders': 1})])
def test_counting_files_and_directories(path, recursive, expected):
    assert counting_files_and_directories(path, recursive=recursive) == expected


# +++++++++++++++++++++++ Для widget ++++++++++++++++++++++++++++++++
@pytest.mark.parametrize("string, expected", [('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                              ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                              ('Счет 64686473678894779589', 'Счет **9589')])
def test_get_number_from_string(string, expected):
    assert get_number_from_string(string) == expected


def test_get_date_from_str():
    assert get_date_from_str("2018-07-11T02:26:18.671407") == '11.07.2018'


# +++++++++++++++++++++++ Для processing ++++++++++++++++++++++++++++++++


def test_filter_for_dict(get_list_dict, get_list_dict_executed, get_list_dict_canceled):
    assert filter_for_dict(get_list_dict) == get_list_dict_executed
    assert filter_for_dict(get_list_dict, "CANCELED") == get_list_dict_canceled


def test_sort_list_to_date(get_list_dict, get_sort_list_to_date_true, get_sort_list_to_date_false):
    assert sort_list_to_date(get_list_dict) == get_sort_list_to_date_true
    assert sort_list_to_date(get_list_dict, reverse=False) == get_sort_list_to_date_false
