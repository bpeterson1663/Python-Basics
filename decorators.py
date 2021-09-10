# Decorator
from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*******")
        func(*args, **kwargs)
        print("*******")

    return wrap_func


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


@my_decorator
def bye(message):
    print(message)


hello('hello this is a greeting', ":)")
bye('bye everyone')


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}ms')
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
