import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start}")
        return result
    return wrapper

def validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if None in args:
            raise ValueError("Invalid input")
        return func(*args, **kwargs)
    return wrapper
