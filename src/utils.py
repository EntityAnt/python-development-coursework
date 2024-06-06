import json
import os

from dotenv import load_dotenv


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
        return json_data






if __name__ == '__main__':
    load_dotenv()
    PATH_TO_OPERATION_JSON = os.getenv('PATH_TO_OPERATION_JSON')
    print(get_financial_transaction_data(PATH_TO_OPERATION_JSON))
