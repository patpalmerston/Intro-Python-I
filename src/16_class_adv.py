import datetime


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


emp_1 = Employee('Pat', 'Palmerston', 50000)
emp_2 = Employee('Leroy', 'Jenkins', 100000)

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

# creates raise amount on the emp_1 instance
# emp_1.raise_amount = 1.10

Employee.set_raise_amt(1.05)

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
