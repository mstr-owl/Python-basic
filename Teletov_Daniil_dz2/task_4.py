# stroka=input("Enter string:")
stroka="Барселона Мюнхен Толедо Мехико Москва Варшава Каменск-Уральский"
tr_stroka=stroka.split()
for number_stroka, word in enumerate(tr_stroka,1):
    if len(word)>10:
        word=word[0:10]
    print(f'{number_stroka}.-{word}')
