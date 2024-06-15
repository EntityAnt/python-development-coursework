import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.utils import get_financial_transactions_data, get_data_from_csv

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")
PATH_TO_DATA = os.getenv("PATH_TO_DATA")
TRASACTIONS_LIST = [
    {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "50870.71", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "3348.98", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "90582.51", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "43861.89", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "7484.91", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "26334.08", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "49192.52", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "26971.25", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "2631.44", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "71771.90", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "45849.53", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "96900.90", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "79428.73", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "90688.44", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "60888.63", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "34380.08", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "77302.31", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "62621.51", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "66263.93", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "63150.74", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "23036.03", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "21344.35", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "98657.83", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "30153.72", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "978.31", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "51203.12", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "47022.09", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "33249.01", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "16872.46", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "31222.43", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "2974.30", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "55985.82", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "19683.25", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "10083.68", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "621.37", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "44493.45", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "52245.30", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "18536.73", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "82946.19", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "29033.65", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "74604.56", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "62654.30", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "24260.78", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "22007.02", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "30234.99", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "19010.50", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "37044.95", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "56071.02", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "47408.20", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "48150.39", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "73778.48", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "62814.53", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "95860.47", "currency": {"name": "руб.", "code": "RUB"}},
    None,
    {"amount": "81513.74", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "65169.27", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "42210.20", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "92130.50", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "90297.21", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "66906.45", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "16796.95", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "84732.61", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "6004.00", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "37160.27", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "45653.70", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "74895.83", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "69311.35", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "82139.20", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "91121.62", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "60030.73", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "6357.56", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "96350.51", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "81150.87", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "56516.63", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
    {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
    {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
]


@pytest.mark.parametrize(
    "path, expected", [(PATH_TO_OPERATION_JSON, TRASACTIONS_LIST), ("", []), ("test_utils.py", [])]
)
def test_get_financial_transaction_data(path, expected) -> None:
    assert get_financial_transactions_data(path) == expected


@patch("csv.reader")
def test_get_data_from_csv(mock_get):
    mock_get.return_value.json.return_value = (
        ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
        ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'Sol', 'PEN', 'Счет 58803664561298323391',
         'Счет 39745660563456619397', 'Перевод организации']
    )
    assert get_data_from_csv(os.path.join(PATH_TO_DATA, 'transactions.csv')) == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации"
        },

    ]
