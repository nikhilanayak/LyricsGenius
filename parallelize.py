import concurrent.futures
import numpy as np
from typing import Any, List, TypeVar, Sequence

def parallelize(l: List[Any], num_threads = 1):
    def wrapper(f):
        def wrapper_function():
            with concurrent.futures.ThreadPoolExecutor(num_threads) as executor:
                for i in executor.map(f, l):
                    yield i
        return wrapper_function
    return wrapper