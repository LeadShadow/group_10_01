# a + b -> a.__add__(b)


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


sasha = Human('Sasha')
print(sasha.say_hello())

# __str__, __repr__

l = [1, 2]
print(l)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(1, 9)
print(a)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(1, 9)
print(a)


class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]  # {1: [1, 2, 3]}

    def __getitem__(self, item):
        result = str(self.data[item][0])
        for value in self.data[item][1:]:
            result += ', ' + str(value)
        return result


l_dict = ListedValuesDict()
l_dict[1] = 1
l_dict[1] = 2
print(l_dict[1])

# Функтори метод __call__


class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(2)
print(two_adder(5))
print(two_adder(4))

class Session:
    def __init__(self, host, port=8080):
        self.connected = True
        self.host = host
        self.port = port

    def __enter__(self):
        print(f'Connected to {self.host}:{self.port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print(f'Some error!')
        else:
            print('No problem')


localhost_session = Session('localhost')
with localhost_session as session:
    print(localhost_session.connected)

