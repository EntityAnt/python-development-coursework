def filter_for_dict(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция, принимает список словарей и значение для ключа state,
        (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
        содержащий только те словари, у которых ключ state содержит переданное в функцию значение. """

    return [i for i in list_dict if i.get('state') == state]


def main() -> None:
    print(filter_for_dict([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                     ], 'CANCELED')
          )


if __name__ == "__main__":
    main()
