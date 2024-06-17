import os
from datetime import datetime

from dotenv import load_dotenv

from src.logger import setup_logging
from src.masks import get_card_number_mask, get_account_mask, counting_files_and_directories
from src.processing import filter_for_dict, sort_list_to_date
from src.utils import get_financial_transactions_data, get_amount, search_in_descriptions, get_data_from_json, \
    statistics_by_states, get_data_from_csv, get_data_from_excel

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")
PATH_TO_DATA = os.getenv("PATH_TO_DATA")
def main():
    result: list[dict]
    formats = ['JSON', 'CSV', 'EXCEL']

    print('''Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.''')
    while True:
        print('''Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла''')
        answer = input('Пользователь: ').strip()
        if answer == '1':
            result = get_data_from_json(PATH_TO_OPERATION_JSON)
            break
        elif answer == '2':
            result = get_data_from_csv(os.path.join(PATH_TO_DATA, 'transactions.csv'))
            break
        elif answer == '3':
            result = get_data_from_excel(os.path.join(PATH_TO_DATA, 'transactions_excel.xlsx'))
            break
    print(f'Программа: Для обработки выбран {formats[int(answer) - 1]}-файл.')

    while True:
        print(""" Программа: Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        state = input('Пользователь: ').upper()
        if state in ['EXECUTED', 'CANCELED', 'PENDING']:
            result = filter_for_dict(result, state=state)
            break
        else:
            print(f'Программа: Статус операции "{state}" недоступен.')

    print(f'Программа: Операции отфильтрованы по статусу {state}.')

    while True:
        print('Программа: Отсортировать операции по дате? Да/Нет')
        main_answer = input('Пользователь: ').lower().strip()
        if main_answer == 'да':
            while True:
                print('Программа: Отсортировать по возрастанию или по убыванию?')
                answer = input('Пользователь:').lower().strip()
                if answer == 'по возрастанию':
                    result = sort_list_to_date(result)
                    break
                elif answer == 'по убыванию':
                    result = sort_list_to_date(result, reverse=True)
                    break
            break
        elif main_answer == 'нет':
            break


    while True:
        print('Программа: Выводить только рублевые транзакции? Да/Нет')
        answer = input('Пользователь:').lower().strip()
        if answer == 'да':
            result = [item for item in result if item.get('currency_code') == "RUB"]
            print(result)
            break
        elif answer == 'нет':
            break

    while True:
        print('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        answer = input('Пользователь:').lower().strip()
        if answer == 'да':
            word = input('Введите слово для фильтрации: ')
            result =
            break
        elif answer == 'нет':
            break


if __name__ == '__main__':
    main()

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
    # # Модуль 13.2
    # list_dict = get_data_from_json(PATH_TO_OPERATION_JSON)
    # # print(f"Найдено {len(search_in_descriptions(list_dict, 'нА кАрТу'))} транзакций")
    # print(statistics_by_states(list_dict, {'state': ['EXECUTED', 'CANCELED', 'PENDING']}))


PATH_TO_DATA = os.getenv("PATH_TO_DATA")
