class User:
    name = 'UserName'
    age = 15

    def say_name(self):
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age):
        self.age = age


sasha = User()
sasha.name = 'Sasha'

sasha.say_name()

sasha.set_age(18)
sasha.say_name()


class Human:
    name = ''

    def hello(self, value):
        if self.name:
            return f'Hello {value} I am {self.name}'
        return f'Hello {value}'


hum = Human()

print(hum.hello('Bill'))

hum.name = 'Sasha'
print(hum.hello('Bill'))

# Інкапсуляція - скриваємо деталі реалізації під інтерфейсом класса, надаючи лише деякий
# інтерфейс програми


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greeting(self):
        return f'Hi {self.name}'


p = Person('Sasha', 18)

print(p.name)
print(p.age)
print(p.greeting())


# Наслідування(успадкування)

class Human:
    name = ''
    def voice(self):
        print(f'Hello! My name is {self.name}')


class Developer(Human):
    field_description = 'My programming Language'
    language = ''

    def make_some_code(self):
        return f'{self.field_description} is {self.value}'


class PythonDeveloper(Developer):
    value = 'Python'


class JSDeveloper(Developer):
    value = 'JavaScript'


p_dev = PythonDeveloper
p_dev.language = 'Python'
p_dev.name = 'Sasha'
h = Human()
p_dev.voice(h)
print(p_dev.name)




class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exists only in B'


class C(B, A):
    z = 'This is exists only in C'


c = C()

print(c.z)
print(c.y)
print(c.x)
