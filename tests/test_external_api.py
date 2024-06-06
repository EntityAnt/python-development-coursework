import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import currency_exchange_rate

load_dotenv()
headers = {"apikey": os.getenv("API_KEY_FOR_APILAYER")}


@patch("requests.get")
def test_currency_exchange_rate(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "timestamp": 1717678144,
        "base": "USD",
        "date": "2024-06-06",
        "rates": {"RUB": 88.848824},
    }
    assert currency_exchange_rate("USD") == 88.848824
    mock_get.assert_called_once_with("https://api.apilayer.com/fixer/latest?base=USD&symbols=RUB", params=headers)
