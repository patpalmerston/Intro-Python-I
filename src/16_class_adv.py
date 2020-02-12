import datetime
'''
look up the http exception class and import?
'''


class Employee:
    # class variable / accesses through the class or instance
    raise_amount = 1.04

    # a variable that is always the same regardless of new instances of parent class
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # using the class reference insted of the self(instance reference) this increments for every instantiation of the class
        Employee.num_of_emps += 1

    # used for debugging - have the repr as a minimum as the str will use it as a fall back if it is not there. Try to display something you can copy and past back into python
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # used as a display to the end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # or Employee.raise_amount, but using self gives us the ability to change that amount for any instance of Employee that would choose to add the raise_amount variable to
        self.pay = int(self.pay * self.raise_amount)

    # class Method , alters the method, so now our method takes a class method, insted of the instance (self), can not use the word 'class' so convention is 'cls'
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # use this class method as alternate constructor to help translate strings into our instance values
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # creating a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('---->', emp.fullname())


# dev_1 = Developer('Pat', 'Palmerston', 50000, 'JS')
# dev_2 = Developer('Leroy', 'Jenkins', 100000, 'Python')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

emp_1 = Employee('Pat', 'Palmerston', 50000)
emp_2 = Employee('Leroy', 'Jenkins', 100000)

print(emp_1 + emp_2)
print(len(emp_1))

# print(repr(emp_1))
# print(str(emp_1))

# isinstance will tell us if an object is an instance of a class
# print(isinstance(mgr_1, Manager))  # True
# print(isinstance(mgr_1, Employee))  # True
# print(isinstance(mgr_1, Developer))  # False

# issubclass will tell us if an object is an instance of a subclass
# print(issubclass(Manager, Employee))  # True
# print(issubclass(Manager, Developer))  # False


# print(mgr_1.email)

# mgr_1.add_emp(dev_2)

# mgr_1.print_emps()

# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# These are all notes and tests pre sub classes


# emp_1 = Employee('Pat', 'Palmerston', 50000)
# emp_2 = Employee('Leroy', 'Jenkins', 100000)

# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))

# creates raise amount on the emp_1 instance
# emp_1.raise_amount = 1.10

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# emp_1.apply_raise()
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# returns instance but no raise amount, because it is in originates from the parent class
# print(emp_1.__dict__)
# returns the class dict with the raise amount in it
# print(Employee.__dict__)
# print(Employee.num_of_emps)

# Creating a new Employee from a string / But lets make it a class method
# emp_str_1 = 'John-Doe-60000'
# new_emp_1 = Employee.from_string(emp_str_1)

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.first)
# print(new_emp_1.email)
# print(new_emp_1.pay)
