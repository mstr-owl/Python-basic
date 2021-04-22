class Data:
    def __init__(self, day_montn_year):
        self.day_month_year = str(day_montn_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != "-":
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f"Everything is ok!"
                else:
                    return f'Wrong year'
            else:
                return f'Wrong month'
        else:
            return f"Wrong day"

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('20 - 11 - 2020')
print(today)
print(Data.valid(11, 11, 2077))
print(today.valid(11, 20, 2011))
print(Data.extract('9 - 2 - 1990'))
print(today.extract('23 - 12 - 2009'))
print(Data.valid(7, 3, 2005))
