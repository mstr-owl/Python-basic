import json
with open("text_7.txt", "r", encoding="utf-8") as my_file:
    firm = {}
    for line in my_file:
        firm_name, *firm_list = line.split()
        firm_income = int(firm_list[1])
        firm_expenses = int(firm_list[2])
        firm[firm_name] = firm_income - firm_expenses

    profit_firm = {}
    profit = 0
    count = 0
    for val in firm.values():
        if val >= 0:
            profit += val
            count += 1
    average_profit = profit / count
    profit_firm["средний доход фирм составляет"] = int(average_profit)

    end_firm_list = [firm, profit_firm]
    print(end_firm_list)

with open("task_7.json", "w", encoding="utf-8") as write_f:
    json.dump(end_firm_list, write_f)
