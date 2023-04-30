from collections import UserDict, UserList, UserString
import string


class ValueSearchDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


as_dict = ValueSearchDict()
as_dict['a'] = 1
print(as_dict.has_in_values(1)) # True
print(as_dict.has_in_values(2)) # False



class CountList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


count = CountList([1, '2', 3, '4', '5'])
count.append('6')
print(count.sum()) # 21


class TruncatedString(UserString):
    MAX_LEN = 7
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('Hello world!')
ts.truncate()
print(ts)



def input_number():
    num = 0
    while True:
        try:
            num = input('Enter integer number: ')
            return int(num)
        except:
            print(f'{num} is not a number. Tru Again')


num = input_number()


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input('Enter name: ')
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 3 symbols. Try again')
    except NameStartsFromLowError:
        print('Name should start from uppercase letter')



class Mammal:
    phrase = ''
    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'WHOOOO!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)
r.record_animal(dog)
r.record_animal(strange_animal)
