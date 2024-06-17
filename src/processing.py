def filter_for_dict(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и значение для ключа state, (по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ state содержит
    переданное в функцию значение."""

    return [i for i in list_dict if i.get("state") == state]


def sort_list_to_date(list_dict: list[dict], reverse: bool = False) -> list[dict]:
    """Принимает список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты (ключ date). Второй аргумент необязательный задает порядок сортировки (убывание, возрастание)."""

    return sorted(list_dict, key=lambda item: item["date"], reverse=reverse)
