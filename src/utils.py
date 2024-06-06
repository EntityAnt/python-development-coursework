import json
import os

from dotenv import load_dotenv

from src.external_api import currency_exchange_rate

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv('PATH_TO_OPERATION_JSON')


def get_financial_transaction_data(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path, encoding='utf-8') as file:
            try:
                json_data = json.load(file)
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
    except FileNotFoundError:
        print('Файл не найден!')
        return []
    if len(json_data) == 0 or type(json_data) != list:
        return []
    else:
        return [operation.get('operationAmount') for operation in json_data]


def get_amount(transaction: dict) -> float:
    """ Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях """
    if transaction['currency']['code'] == 'RUB':
        return transaction['amount']
    else:
        rate = currency_exchange_rate(transaction['currency']['code'])
        return round(float(transaction['amount']) * rate, 2)


if __name__ == '__main__':
    transaction = get_financial_transaction_data(PATH_TO_OPERATION_JSON)[1]
    print(get_amount(transaction))
