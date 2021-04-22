from functools import reduce


def chet_func(num_1, num_2):
    return num_1*num_2


print(reduce(chet_func, [number for number in range(100, 1001) if number % 2 == 0]))
