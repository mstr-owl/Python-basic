def func(x, y):
    return 1/x ** abs(y)
# print(func(int(input("Введите первое число:")),int(input("Введите второе число:"))))
print(func(4, -2))


def func(x, y):
    res = 1
    for _ in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res
# print(func(int(input("Введите первое число:")),int(input("Введите второе число:"))))
print(func(4, -2))
