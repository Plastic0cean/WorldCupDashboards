from typing import Callable

def retry_if_fail(function: Callable, attempts: int=5):
    def inner(*args, **kwargs):
        for _ in range(attempts):
            try:
                result = function(*args, **kwargs)
                return result
            except:
                continue
    return inner