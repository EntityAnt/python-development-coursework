import os

import requests
from dotenv import load_dotenv

load_dotenv()
headers = {"apikey": os.getenv("API_KEY_FOR_APILAYER")}


def currency_exchange_rate(currency: str) -> float:
    """Принимает название валюты и возвращает ее курс к рублю"""
    response = requests.get(
        f"https://api.apilayer.com/fixer/latest?base={currency.upper()}&symbols=RUB", params=headers
    )
    return float(response.json()["rates"]["RUB"])


if __name__ == "__main__":
    print(currency_exchange_rate("USD"))
