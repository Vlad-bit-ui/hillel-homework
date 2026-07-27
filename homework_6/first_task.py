def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_args
def alotofargs(*args, **kwargs):
    print("Виконую функцію з переданими аргументами")


alotofargs(1, 2, 3, name="Влад", age=25)