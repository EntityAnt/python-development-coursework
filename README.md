9.2 Основы Git

Задачи:
Создайте локальный Git-репозиторий.
Создайте файл 
.gitignore
.
Сделайте минимум три коммита в процессе разработки кода.
Создайте модуль 
widget
 для размещения новых функций.
Реализуйте одну функцию, которая будет уметь работать как с картами, так и со счетами.
Функция должна:

Принимать на вход строку с информацией — тип карты/счета и номер карты/счета.
Функция принимает на вход только один аргумент — строку, которая состоит из требуемых частей. Это может быть строка типа 
Visa Platinum 7000 7922 8960 6361
, или 
Maestro 7000 7922 8960 6361
, или 
Счет 73654108430135874305
. Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!

Возвращать исходную строку с замаскированным номером карты/счета.
Для карты и счета используйте разные маскировки.

Обратите внимание на то, что функции для маскировки уже реализованы. Переиспользуйте код, который уже написан в проекте, а не дублируйте его.

# Пример для карты
Visa Platinum 7000 7922 8960 6361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции

Примеры входных данных:

Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305

Напишите функцию, которая принимает на вход строку вида 
2018-07-11T02:26:18.671407
 и возвращает строку с датой в виде 
11.07.2018.

* Дополнительное задание 1
Напишите функцию, которая принимает на вход список строк и возвращает список строк, в которых первая и последняя буквы совпадают. Если список пустой, верните пустой список.

Примеры входных данных:

['hello', 'world', 'apple', 'pear', 'banana', 'pop']
['', 'madam', 'racecar', 'noon', 'level', '']
[]

Примеры выходных данных:

['pop']
['', 'madam', 'racecar', 'noon', 'level', '']
[]

* Дополнительное задание 2
Напишите функцию, которая принимает на вход список целых чисел и возвращает максимальное произведение двух чисел из списка. Если в списке менее двух чисел, функция должна вернуть 0.

Примеры входных данных:

[2, 3, 5, 7, 11]
[-5, -7, -9, -13]
[1, 2]
[4]

Примеры выходных данных:

77
117
2
0

====================================================================================
# 10.1 Продвинутый Git

1. Создайте GitHub-репозиторий.
2. Залейте текущий проект в GitHub-репозиторий.
3. Создайте модуль processing для новых функций.
4. Напишите функцию, которая принимает на вход список словарей и значение для ключа 
state (опциональный параметр со значением по умолчанию EXECUTED) и 
возвращает новый список, содержащий только те словари, у которых ключ state 
содержит переданное в функцию значение.

### Вход функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

### Выход функции со статусом по умолчанию EXECUTED
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

### Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


5. Напишите функцию, которая принимает на вход список словарей и возвращает новый 
список, в котором исходные словари отсортированы по убыванию даты (ключ date). 
Функция принимает два аргумента, второй необязательный задает порядок сортировки 
(убывание, возрастание).

### Вход функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

### Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


