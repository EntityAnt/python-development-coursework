import logging
import os

from src.logger import setup_logging
from src.masks import get_card_number_mask, get_account_mask, counting_files_and_directories

# logger = setup_logging(__name__)
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler(os.path.join('logs', f'{__name__}.log'))
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)

if __name__ == '__main__':
    # Для masks
    logger = setup_logging(__name__)
    logging.info('123456')
    # get_card_number_mask("7000792289606361")
    # get_account_mask("73654108430135874305")
    # counting_files_and_directories(recursive=False)
