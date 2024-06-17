import os
from datetime import datetime

from dotenv import load_dotenv

from src.logger import setup_logging
from src.masks import get_card_number_mask, get_account_mask, counting_files_and_directories
from src.utils import get_financial_transactions_data, get_amount, search_in_descriptions, get_data_from_json, \
    statistics_by_states

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")


def main():
    formats = ['JSON', 'CSV', 'EXCEL']
    print('''Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.''')
    while True:
        print('''Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла''')
        answer = input('Пользователь: ')
        if answer in ['1', '2', '3']:
            if answer == '1':
                result = get_data_from_json(PATH_TO_OPERATION_JSON)
            elif answer == '2':
                result = get_data_form_csv()
            break
    print(f'Программа: Для обработки выбран {formats[int(answer) - 1]}-файл.')

    while True:
        print(""" Программа: Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        state = input('Пользователь: ')
        if state.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
            break
        else:
            print(f'Программа: Статус операции "{state}" недоступен.')

    print(f'Программа: Операции отфильтрованы по статусу {state.upper()}.')

    while True:
        print('Программа: Отсортировать операции по дате? Да/Нет')
        answer = input('Пользователь: ')
        if answer.lower() == 'да':
            is_sort_by_date = True
            break
        elif answer.lower() == 'нет':
            is_sort_by_date = False
            break
    while True:
        print('Программа: Отсортировать по возрастанию или по убыванию?')
        answer = input('Пользователь:')
        if answer.lower() == 'по возрастанию':
            by_ascending = True
            break
        elif answer.lower() == 'по убыванию':
            by_ascending = False
            break

    while True:
        print('Программа: Выводить только рублевые транзакции? Да/Нет')
        answer = input('Пользователь:')
        if answer.lower() == 'да':
            only_rubles = True
            break
        elif answer.lower() == 'нет':
            only_rubles = False
            break

    while True:
        print('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        answer = input('Пользователь:')
        if answer.lower() == 'да':
            word = input('Введите слово для фильтрации: ')
            break
        elif answer.lower() == 'нет':
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
