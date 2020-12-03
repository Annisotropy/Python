class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print('Full name: ', self.name, self.surname)

    def get_total_income(self):
        print('Total income: ', self._income['wage'] + self._income['bonus'])


Employee = Position('Alex', 'Petrov', 'analyst', 50, 30)
Employee.get_full_name()
Employee.get_total_income()



