import os
from datetime import datetime

from dotenv import load_dotenv

from src.logger import setup_logging
from src.masks import get_card_number_mask, get_account_mask, counting_files_and_directories
from src.utils import get_financial_transactions_data, get_amount, get_data_from_csv, get_data_from_excel

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")
PATH_TO_DATA = os.getenv("PATH_TO_DATA")

if __name__ == '__main__':
    logger = setup_logging(datetime.today().strftime('%Y-%m-%d'))

    # Для masks
    logger.info('Запуск функций из модуля masks')

    # get_card_number_mask("7000792289606361")
    # get_account_mask("73654108430135874305")
    # counting_files_and_directories(recursive=False)

    # Для utils
    logger.info('Запуск функций из модуля utils')
    # transaction = get_financial_transactions_data(PATH_TO_OPERATION_JSON)[3]
    # get_amount(transaction)
    print(get_data_from_csv(os.path.join(PATH_TO_DATA, 'transactions.csv')))
    # print(get_data_from_excel(os.path.join(PATH_TO_DATA, 'transactions_excel.xlsx')))

