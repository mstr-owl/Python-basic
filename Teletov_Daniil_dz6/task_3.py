class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Имя сотрудника: {self.name +' '+ self.surname}"

    def get_total_income(self):
        return f"Доход сотрудника с премией составляет: {self._income.get('wage')+self._income.get('bonus')} рублей"


worker_1 = Position("Федор", "Смолов", "бугалтер", 55000, 20000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
