import collections
class User:
    def __init__(self, name, last_name, age, birth_place, index):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.birth_place = birth_place
        self.index = index



person = ('Sasha', 'Samus', 30, 'Keletskya', '98')


Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'index'])
person = Person('Sasha', 'Samus', 30, 'Keletskya', '98')
print(person.name)
print(person.last_name)
print(person.age)
print(person.birth_place)
print(person.index)


user = User('Sasha', 'Samus', 30, 'Keletskya', '98')
print('-----------------')
print(user.name)
print(user.last_name)
print(user.age)
print(user.birth_place)
print(user.index)
