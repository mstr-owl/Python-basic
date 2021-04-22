class NotnumberError:
    def __init__(self, *args):
        self.my_list = []

    def en_number(self):
        while True:
            try:
                value = int(input('Введите значения и нажмите Enter - '))
                self.my_list.append(value)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение,не число")
                attempt = input(f'Попробовать еще раз? Да/Нет:')
                if attempt == "Да" or attempt == "да":
                    print(try_except.en_number())
                else:
                    return f'Вы вышли'


try_except = NotnumberError(1)
print(try_except.en_number())
