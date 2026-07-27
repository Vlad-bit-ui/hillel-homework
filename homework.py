MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def get_input():
    line = input("Введіть 12 значень опадів через пробіл: ")
    return line


def validate_input(line):
    parts = line.split()

    if len(parts) != 12:
        raise ValueError("Помилка: потрібно ввести рівно 12 чисел")

    precipitation = []
    for part in parts:
        try:
            value = float(part)
        except ValueError:
            raise ValueError(f"Помилка: {part} не є числом")

        if value < 0:
            raise ValueError("Помилка: опади не можуть бути від'ємними")

        precipitation.append(value)

    return precipitation


def calculate(precipitation):
    total = sum(precipitation)
    average = total / 12

    max_value = max(precipitation)
    min_value = min(precipitation)

    max_index = precipitation.index(max_value)
    min_index = precipitation.index(min_value)

    highest = (max_value, MONTHS[max_index])
    lowest = (min_value, MONTHS[min_index])

    return (total, average, highest, lowest)


def display_output(result):
    print(result)


def main():
    info = get_input()
    precipitation = validate_input(info)
    result = calculate(precipitation)
    display_output(result)


if __name__ == "__main__":
    main()