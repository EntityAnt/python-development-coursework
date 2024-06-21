import os

from dotenv import load_dotenv

from src.processing import sort_list_to_date, filter_for_dict
from src.utils import get_data_from_excel, get_data_from_csv, get_data_from_json, search_in_descriptions
from src.widget import get_date_from_str, get_number_from_string

load_dotenv()
PATH_TO_OPERATION_JSON = os.getenv("PATH_TO_OPERATION_JSON")
PATH_TO_DATA = os.getenv("PATH_TO_DATA")


def main():
    result: list[dict]
    formats = ["JSON", "CSV", "EXCEL"]

    print(
        """Привет! Добро пожаловать в программу работы
    с банковскими транзакциями."""
    )
    while True:
        print(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        answer = input("Пользователь: ").strip()
        if answer == "1":
            result = get_data_from_json(PATH_TO_OPERATION_JSON)
            break
        elif answer == "2":
            result = get_data_from_csv(os.path.join(PATH_TO_DATA, "transactions.csv"))
            break
        elif answer == "3":
            result = get_data_from_excel(os.path.join(PATH_TO_DATA, "transactions_excel.xlsx"))
            break
    format_file = formats[int(answer) - 1]
    print(f"Программа: Для обработки выбран {format_file}-файл.")

    while True:
        print(
            """ Программа: Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        state = input("Пользователь: ").upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            result = filter_for_dict(result, state=state)
            break
        else:
            print(f'Программа: Статус операции "{state}" недоступен.')

    print(f"Программа: Операции отфильтрованы по статусу {state}.")

    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        main_answer = input("Пользователь: ").lower().strip()
        if main_answer == "да":
            while True:
                print("Программа: Отсортировать по возрастанию или по убыванию?")
                answer = input("Пользователь:").lower().strip()
                if answer == "по возрастанию":
                    result = sort_list_to_date(result)
                    break
                elif answer == "по убыванию":
                    result = sort_list_to_date(result, reverse=True)
                    break
            break
        elif main_answer == "нет":
            break

    while True:
        print("Программа: Выводить только рублевые транзакции? Да/Нет")
        answer = input("Пользователь:").lower().strip()
        if answer == "да":
            result = [item for item in result if item.get("currency_code") == "RUB"]
            break
        elif answer == "нет":
            break

    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer = input("Пользователь:").lower().strip()
        if answer == "да":
            word = input("Введите слово для фильтрации: ")
            result = search_in_descriptions(result, word)
            break
        elif answer == "нет":
            break

    if len(result) > 0:
        print("Программа: Распечатываю итоговый список транзакций...\n\n")
        print(f"Программа:\nВсего банковских операций в выборке: {len(result)}")
        print("*" * 50 + "\n")
        for item in result:
            date = get_date_from_str(item.get("date"))
            from_ = get_number_from_string(item.get("from"))
            to_ = get_number_from_string(item.get("to"))
            description = item.get("description")
            if format_file != "JSON":
                amount = item.get("amount")
                currency_code = item.get("currency_code")
            else:
                amount = item.get("operationAmount")["amount"]
                currency_code = item.get("operationAmount")["currency"]["code"]
            if from_ is None:
                print(f"{date} {description}\n{to_}\nСумма: {amount} {currency_code}.\n" + "-" * 50 + "\n")
            else:
                print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency_code}.\n" + "-" * 50 + "\n")
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
