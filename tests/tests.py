import os

import pytest

from src.masks import get_account_mask, get_card_number_mask, counting_files_and_directories


@pytest.mark.parametrize("num_card, expected", [("7000792289606361", '7000 79** **** 6361')])
def test_get_card_number_mask(num_card, expected):
    assert get_card_number_mask(num_card) == expected


@pytest.mark.parametrize("account, expected", [("73654108430135874305", '**4305')])
def test_get_account_mask(account, expected):
    assert get_account_mask(account) == expected


@pytest.mark.parametrize("path, recursive, expected", [(os.getcwd(), False, {'files': 2, 'folders': 1}),
                                                       (os.getcwd(), True, {'files': 4, 'folders': 1})])
def test_counting_files_and_directories(path, recursive, expected):
    assert counting_files_and_directories(path, recursive=recursive) == expected
