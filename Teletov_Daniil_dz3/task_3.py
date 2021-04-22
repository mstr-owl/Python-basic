def sum_number(x, y, z):
    if x >= z and y >= z:
        res = x + y
    elif y < x <= z:
        res = x + z
    else:
        res = y + z
    return res
# print(sum_number(int(input("Введите первое число:")), int(input("Введите второе число:")), int(input("Введите третье число:"))))
print(f'{sum_number(int(5), int(3), int(9))}')
