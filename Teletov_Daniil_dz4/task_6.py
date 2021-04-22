from itertools import count, cycle


for number in count(3):
    print(number)
    if number == 10:
        break


kol = 0
my_list = ['Moscow', 'Barcelona', 25, 'Madrid', 999, 'Berlin', 'Rome', 777, None, True]
for stroka in cycle(my_list):
    if kol > 55:
        break
    print(stroka)
    kol += 1
