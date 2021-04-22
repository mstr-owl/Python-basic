from sys import argv


def salary(hours, rate, bonus):
    return hours * rate + bonus


if len(argv) == 4:
    args = int(argv[1]), int(argv[2]), int(argv[3])
    print(f"Заработная плата: {salary(*args):.2f}")
else:
    print("Вы ввели недостоверные данные")
