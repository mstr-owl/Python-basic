with open("text_5.txt", "w", encoding="utf-8") as my_file:
    my_file.write("5 15 25 50 75 93 120 231 432 590")
with open("text_5.txt", "r", encoding="utf-8") as my_file:
    my_list = [
        int(number)
        for line in my_file
        for number in line.split()
    ]
    print(sum(my_list))
