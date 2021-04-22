def func(element):
    if element == "-":
        return 0
    else:
        number = element.split("(")
        return int(number[0])


with open("text_6.txt", "r", encoding="utf-8") as my_file:
    sub_dict = {}
    for line in my_file:
        subject, *my_line_list = line.split()
        my_number_list = [
            func(sign)
            for sign in my_line_list
            if not sign.isalpha()
        ]
        hours = sum(my_number_list)
        sub_dict.setdefault(subject, hours)
    print(sub_dict)
