import os
import time
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> None:
    """Логирует вызов функции и записывает результат в файл или в консоль.
    Если filename не задан, то логи будут выводиться в консоль"""

    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                res_str = f"{func.__name__} - OK\n"
            except Exception as ex:
                res_str = f"{func.__name__} error: {ex}. Input {args}, {kwargs}\n"
                raise Exception("{func.__name__} error: {ex}.")
            finally:
                if filename != "":
                    os.chdir(os.path.dirname(os.path.abspath(__file__)))
                    os.chdir("..")
                    os.chdir("logs")
                    path = os.path.join(os.getcwd(), filename)
                    with open(path, "a", encoding="utf-8") as file:
                        file.write(res_str)
                else:
                    print(res_str.rstrip())

            return result

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function(1, 2))
