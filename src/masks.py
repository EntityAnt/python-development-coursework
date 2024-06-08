import logging
import os
from datetime import datetime

from src.logger import setup_logging

logger = setup_logging(datetime.today().strftime('%Y-%m-%d'))


def get_card_number_mask(num_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску,
    в формате XXXX XX** **** XXXX"""
    result = f"{num_card[:4]} {num_card[4:6]}** **** {num_card[-4:]}"
    logging.info(f"Создана маска для карты: {result}")
    return result


def get_account_mask(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, в формате
    **XXXX"""
    result = f"**{account[-4:]}"
    logging.info(f"Создана маска для карты: {result}")
    return result


def counting_files_and_directories(path: str = "", recursive: bool = False) -> dict:
    """Функция, принимает путь до директории и возвращает словарь вида:
    {"files": количество файлов в директории, "folders": количество папок в директории}
    """

    res_dict = {}
    files = 0
    folders = 0
    if not os.path.isdir(path):
        path = os.path.dirname(os.path.abspath(__file__))
    logging.warning(f"Путь {path} не найден!")
    if recursive:
        tree = os.walk(path)
        for dir, folder, file in tree:
            files += len(file)
            folders += len(folder)
    else:
        for entity in os.scandir(path):
            if entity.is_file():
                files += 1
            if entity.is_dir():
                folders += 1

    res_dict["files"] = files
    res_dict["folders"] = folders
    logging.info(f"Найдено {files} файлов и {folders} папок")
    return res_dict
