def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def positive_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError("Всі аргументи мають бути додатними числами")
        return func(*args, **kwargs)
    return wrapper


@positive_only
def add_two(x):
    return x + 2


@shout
def add_suffix(value):
    return value + "suffix"


if __name__ == "__main__":
    print(add_two(5))
    print(add_suffix("i"))

    try:
        add_two(-3)
    except ValueError as e:
        print(e)