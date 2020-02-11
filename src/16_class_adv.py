class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Pat', 'Palmerston', 50000)
emp_1 = Employee('Leroy', 'Jenkins', 100000)
