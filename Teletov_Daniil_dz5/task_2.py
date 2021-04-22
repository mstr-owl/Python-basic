with open("text_2.txt", "r", encoding="utf-8") as my_file:
    count = 0
    for stroka in my_file:
        count += 1
        words = len(stroka.split())
        print(f"в {count} строке количетсво слов составляет: {words}")
    print(f"общие количество строк в файле составляет: {count}")
