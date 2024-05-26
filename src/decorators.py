import os
from functools import wraps
import time
from typing import Callable, Any


def log(filename: str = '') -> None:
    """ Логирует вызов функции и записывает результат в файл или в консоль.
        Если filename не задан, то логи будут выводиться в консоль"""
    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                res_str = f'{time.ctime(time.time())} - {func.__name__} - OK\n'
            except Exception as ex:
                res_str = f'{time.ctime(time.time())} - {func.__name__} error: {ex}. Input {args}, {kwargs}\n'
            if filename != '':
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                os.chdir('..')
                os.chdir('logs')
                path = os.path.join(os.getcwd(), filename)
                with open(path, 'a', encoding='utf-8') as file:
                    file.write(res_str)
            else:
                print(res_str.rstrip())

            return result

        return wrapper

    return decorator


@log()
def my_function(x, y):
    return x + y


print(my_function(1, 2))
