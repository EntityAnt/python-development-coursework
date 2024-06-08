import logging

from src.logger import setup_logging
from src.masks import get_card_number_mask, get_account_mask, counting_files_and_directories

logger = setup_logging(__name__)
if __name__ == '__main_':
    # Для masks
    logging.info('123')
    get_card_number_mask("7000792289606361")
    get_account_mask("73654108430135874305")
    counting_files_and_directories(recursive=False)
