# Створення об'єкта ітератора генератора
from collections import UserDict
class Iterable:
    MAX_VALUE = 10
    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()



c = CustomIterator()
for i in c:
    print(i)



class Secret:
    public_field = 'this is public'
    _private_field = 'this is private'
    __real_secret = 'I am hidden'



s = Secret()
print(s.public_field)
print(s._private_field)
print(s._Secret__real_secret)



class PositiveNumber:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        print('Only numbers greater zero accepted')


p = PositiveNumber(1)
print(p.value)
p.value = -1
p._PositiveNumber__value = -1
print(p.value)



class MyDict(UserDict):
    def __add__(self, other):
        self.data.update(other)
        return self

    def __sub__(self, other):
        for key in other:
            if key in other:
                self.data.pop(key)
        return self


d1 = MyDict({1: 'a', 2: 'b'})
d2 = MyDict({3: 'c', 4: 'd'})
d2_test = MyDict({5: 'e'})
d3 = d1 + d2
print(d3)
# d3 = {}
# d3.update({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
# print(d3)
d4 = d3 - d2
print(d4)


# Операції зрівняння
# __eq__, __ne__, __lt__, __gt__, __le__, __ge__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y


print(Point(0,0) == Point(0,0))  # True
print(Point(0,0) != Point(0,0))  # False
print(Point(0,0) < Point(1,0))  # False
print(Point(0,0) > Point(0,1))  # False
print(Point(0,2) >= Point(0,1))  # True
print(Point(0,0) <= Point(0,0))  # True