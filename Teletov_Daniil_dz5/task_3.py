with open("text_3.txt", "r", encoding="utf-8") as my_file:
    staff_dict = {}
    for stroka in my_file:
        key, value = stroka.split()
        staff_dict[key] = float(value)
        if float(value) < 20000:
            print(f"Сотрудник чей оклад составляет менее 20 000 рублей: {key}")
    average_salary = sum(staff_dict.values())/len(staff_dict)
    print(f"Средняя зарплата сотрудников составялет: {average_salary:.2f}")
