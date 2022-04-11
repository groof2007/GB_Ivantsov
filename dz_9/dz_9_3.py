class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position.capitalize()
        self._income = income


class Position(Worker):

    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> int:
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    worker_1 = Position('степан', 'степанов', 'сварщик', {'wage': 30000, 'bonus': 7000})
    worker_2 = Position('иван', 'иванов', 'водитель', {'wage': 40000, 'bonus': 8000})
    worker_3 = Position('петр', 'петров', 'ученый', {'wage': 50000, 'bonus': 9000})
    print(worker_1.get_full_name(), worker_1.get_total_income())
    print(worker_2.get_full_name(), worker_2.get_total_income())
    print(worker_3.get_full_name(), worker_3.get_total_income())