def number(x, y):
    try:
        resultat = "%.2f" % (x / y)
    except ZeroDivisionError:
        return "Нельзя делить на 0"
    except ValueError:
        return "Неправильное значение переменной"
    return resultat
# print(number(int(input("Введите первое число:")), int(input("Введите второе число:"))))
print(number(4, 9))
