# number=int(input("Введите чилсо:"))
number=5
my_list=[9,8,7,5,5,4,3,2]
if number>my_list[0]:
    my_list.insert(0,number)
elif number<my_list[-1]:
    my_list.append(number)
else:
    for i in my_list:
        if my_list.count(number)>0:
            a=my_list.index(number)
            b=my_list.count(number)
            my_list.insert(a+b,number)
            break
print(my_list)
