# kol=int(input("Введите количество элементов списка: "))
kol=5
my_list=[2,5,7,8,9]
j=0
# for i in range(1,kol+1):
#     my_list.append(input("Введите по одному значение списка: "))
for _ in range(len(my_list)//2):
    my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
    j+=2
print(my_list)
