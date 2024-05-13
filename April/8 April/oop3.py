class Person:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
    
    def __str__(self):
        return f'{self.name} is {self.age} years old'

p1 = Person(name = 'Alice', age = 23)
p2 = Person(name = 'Bob')
print(p1)
print(p2)