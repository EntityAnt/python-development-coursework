def filter_for_dict(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и значение для ключа state, (опциональный параметр со значением
    по умолчанию EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ state содержит
    переданное в функцию значение."""

    return [i for i in list_dict if i.get("state") == state]


def sort_list_to_date(list_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Принимает список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты (ключ date). Второй аргумент необязательный задает порядок сортировки (убывание, возрастание)."""

    return sorted(list_dict, key=lambda item: item["date"], reverse=reverse)


def main() -> None:
    print(
        filter_for_dict(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    )

    print(
        sort_list_to_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )


if __name__ == "__main__":
    main()
