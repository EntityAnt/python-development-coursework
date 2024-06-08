import logging
import os

from dotenv import load_dotenv

from src.logger import setup_logging
from src.masks import get_card_number_mask, get_account_mask, counting_files_and_directories
from src.utils import get_financial_transactions_data, get_amount

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")

if __name__ == '__main__':
    # Для masks
    logger = setup_logging(__name__)
    logging.info('Запуск функций из модуля masks')

    get_card_number_mask("7000792289606361")
    get_account_mask("73654108430135874305")
    counting_files_and_directories(recursive=False)

    # Для utils
    logging.info('Запуск функций из модуля utils')
    transaction = get_financial_transactions_data(PATH_TO_OPERATION_JSON)[1]
    get_amount(transaction)

