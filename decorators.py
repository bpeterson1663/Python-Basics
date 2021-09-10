# Decorator

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


