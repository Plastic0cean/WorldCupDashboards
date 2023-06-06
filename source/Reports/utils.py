from typing import Callable 
import pandas as pd

def to_dataframe(function: Callable):
    def inner(*args, **kwargs):
        return pd.DataFrame(function(*args, **kwargs))
    return inner
