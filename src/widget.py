from datetime import datetime

from src import masks


def get_number_from_string(string: str) -> str:
    """
    Функция принимает строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета.
    """
    if type(string) is str and len(string) > 0:
        tmp_list = string.strip().split()
        if tmp_list[0] == "Счет":
            return f"Счет {masks.get_account_mask(tmp_list[-1])}"
        return f'{" ".join(tmp_list[0:-1])} {masks.get_card_number_mask(tmp_list[-1])}'
    return None


def get_date_from_str(str_date: str) -> str:
    """
    Функция, принимает строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018.
    """
    return str(datetime.strptime(str_date.split("T")[0], "%Y-%m-%d").strftime("%d.%m.%Y"))
