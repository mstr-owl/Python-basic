def int_func(word):
    return f"{word.title()}"


def strok_words(en_words):
    res_stroka_words = []
    for word in en_words.split():
        res_stroka_words.append(int_func(word))
    return " ".join(res_stroka_words)
# statement=input("Введите свое высказывание:")
statement = "may there be peace in the world!"
print(strok_words(statement))
