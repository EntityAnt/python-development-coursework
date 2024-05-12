import masks
from datetime import datetime



def get_number_from_string(string: str) -> str:
    """
    Функция принимает строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета.
    """
    tmp_list = string.strip().split()
    if tmp_list[0] == 'Счет':
        return f'Счет {masks.get_account_mask(tmp_list[-1])}'
    return f'{" ".join(tmp_list[0:-1])} {masks.get_card_number_mask(tmp_list[-1])}'


def get_date_from_str(str_date: str) -> str:
    """
    Функция, принимает строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018.
    """
    return str(datetime.strptime(str_date.split('T')[0], "%Y-%m-%d").strftime('%d.%m.%Y'))


def get_first_equal_last(str_list: list[str]) -> list[str]:
    """
    Функция, принимает на вход список строк и возвращает
    список строк, в которых первая и последняя буквы совпадают.
    Если список пустой, верните пустой список.
    """
    if len(str_list) == 0:
        return []
    new_list = list()
    for string in str_list:
        if len(string) > 0 and string[0] == string[-1]:
            new_list.append(string)
    return new_list


def get_maximum_multiplication(num_list: list[int]) -> int:
    """
    Функция, принимает список целых чисел и возвращает максимальное произведение
    двух чисел из списка. Если в списке менее двух чисел, функция должна вернуть 0.
    """
    if len(num_list) < 2:
        return 0
    new_list = list()
    for num in num_list:
        new_list.append(abs(num))
    num1 = max(new_list)
    new_list.remove(num1)
    num2 = max(new_list)
    return num1 * num2


if __name__ == "__main__":
    print(get_number_from_string('Visa Classic 6831982476737658'))
    print(get_number_from_string('Maestro 1596837868705199'))
    print(get_number_from_string('Счет 64686473678894779589'))
    print(get_date_from_str('2018-07-11T02:26:18.671407'))
    print(get_first_equal_last(['', 'madam', 'racecar', 'noon', 'level', '']))
    print(get_maximum_multiplication([-5, -7, -9, -13]))