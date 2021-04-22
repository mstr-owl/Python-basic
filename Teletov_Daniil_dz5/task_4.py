def func():
    with open("text_4.txt", "r", encoding="utf-8") as file_en:
        for stroka in file_en:
            yield stroka


number_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Ten": "Десять"
}


def convert(en_line):
    for key, value in number_dict.items():
        if key in en_line:
            return en_line.replace(key, value)


with open("text_4_new.txt", "w", encoding="utf-8") as file_ru:
    for line_ru in func():
        file_ru.write(convert(line_ru))
