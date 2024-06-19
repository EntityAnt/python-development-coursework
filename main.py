import os
from datetime import datetime
from io import StringIO

import pandas as pd
from dotenv import load_dotenv

from src.logger import setup_logging
from src.masks import counting_files_and_directories, get_account_mask, get_card_number_mask
from src.utils import get_amount, get_data_from_excel, get_financial_transactions_data

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")
PATH_TO_DATA = os.getenv("PATH_TO_DATA")


def main():
    formats = ["JSON", "CSV", "EXCEL"]
    print(
        """Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями."""
    )
    while True:
        print(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        question_1 = input("Пользователь: ")
        if question_1 in ["1", "2", "3"]:
            break

    print(f"Программа: Для обработки выбран {formats[int(question_1) - 1]}-файл.")


if __name__ == "__main__":
    # main()

    # logger = setup_logging(datetime.today().strftime('%Y-%m-%d'))
    #
    # # Для masks
    # logger.info('Запуск функций из модуля masks')
    #
    # get_card_number_mask("7000792289606361")
    # get_account_mask("73654108430135874305")
    # counting_files_and_directories(recursive=False)
    #
    # # Для utils
    # logger.info('Запуск функций из модуля utils')
    # transaction = get_financial_transactions_data(PATH_TO_OPERATION_JSON)[3]
    # get_amount(transaction)
    #
    # # Модуль 13.1
    get_data_from_excel(os.path.join(PATH_TO_DATA, "transactions_excel.xlsx"))

    # # Модуль 13.2
    # list_dict = get_data_from_json(PATH_TO_OPERATION_JSON)
    # # print(f"Найдено {len(search_in_descriptions(list_dict, 'нА кАрТу'))} транзакций")
    # print(statistics_by_states(list_dict, {'state': ['EXECUTED', 'CANCELED', 'PENDING']}))
