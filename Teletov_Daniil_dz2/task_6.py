spisok_tovar=[(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
              (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
              (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
analitic_tovar={}
for tovar in spisok_tovar:
    for key,value in tovar[1].items():
        analitic_tovar.setdefault(key,[]).append(value)
print(analitic_tovar)


