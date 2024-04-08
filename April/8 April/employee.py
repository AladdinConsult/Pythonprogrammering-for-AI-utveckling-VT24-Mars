class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary =salary

    def __str__(self):
        return f'{self.first_name}, {self.last_name} earns {self.salary}'

class Developer(Employee):
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)

print(emp1)
print(emp2)
