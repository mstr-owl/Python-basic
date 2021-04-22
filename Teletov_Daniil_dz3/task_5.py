def my_func():
    sum_res = 0
    exet = False
    while not exet:
        numbers = input("Введите числа через пробел или нажмите 'q' для выхода:").split()
        res = 0
        for i in numbers:
            if i.lower() == 'q':
                exet = True
                break
            else:
                res += int(i)
        sum_res += res
    print(f'Итоговая сумма чисел равна: {sum_res}')
my_func()
