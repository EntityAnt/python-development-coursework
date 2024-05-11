import os


def get_card_number_mask(num_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску,
    в формате XXXX XX** **** XXXX"""
    return f"{num_card[:4]} {num_card[4:6]}** **** {num_card[-4:]}"


def get_account_mask(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, в формате
    **XXXX"""
    return f"**{account[-4:]}"


def counting_files_and_directories(path: str = "", recursive: bool = False) -> dict:
    """Функция, принимает путь до директории и возвращает словарь вида:
    {"files": количество файлов в директории, "folders": количество папок в директории}
    """

    res_dict = {}
    files = 0
    folders = 0
    if not os.path.isdir(path):
        path = os.getcwd()
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
    return res_dict


if __name__ == "__main__":
    print(get_card_number_mask("7000792289606361"))
    print(get_account_mask("73654108430135874305"))
    print(counting_files_and_directories())
