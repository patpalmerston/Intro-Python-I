class Employee:
    # class variable / accesses through the class or instance
    raise_amount = 1.04

    # a variable that is always the same regardless of new instances of parent class
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
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
        pass


emp_1 = Employee('Pat', 'Palmerston', 50000)
emp_2 = Employee('Leroy', 'Jenkins', 100000)

# creates raise amount on the emp_1 instance
emp_1.raise_amount = 1.10

# print(Employee.raise_amount)
# emp_1.apply_raise()
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# returns instance but no raise amount, because it is in originates from the parent class
# print(emp_1.__dict__)
# returns the class dict with the raise amount in it
# print(Employee.__dict__)
print(Employee.num_of_emps)
