import json
import os
from datetime import datetime

from dotenv import load_dotenv

from src.external_api import currency_exchange_rate
from src.logger import setup_logging

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")

logger = setup_logging(datetime.today().strftime("%Y-%m-%d"))


def get_financial_transactions_data(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                json_data = json.load(file)
            except json.JSONDecodeError as ex:
                logger.exception(f"Ошибка декодирования файла. {ex}")
                return []
    except FileNotFoundError as ex:
        logger.exception(f"Файл не найден! {ex}")
        return []
    if len(json_data) == 0 or type(json_data) is not list:
        logger.warning("Файл пустой или неверный формат файла")
        return []
    else:
        result = [operation.get("operationAmount") for operation in json_data]
        logger.info(f"Сформировано {len(result)} записей с транзакциями")
        return result


def get_amount(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    if transaction["currency"]["code"] == "RUB":
        result = float(transaction["amount"])
        logger.info(f"Получена транзакция на сумму {result} руб.")
    else:
        rate = currency_exchange_rate(transaction["currency"]["code"])
        result = round(float(transaction["amount"]) * rate, 2)
        logger.info(f"Получена транзакция на сумму {result} руб.")
    return result


