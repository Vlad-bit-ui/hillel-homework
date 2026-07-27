def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Старт!"


for value in countdown(5):
    print(value)