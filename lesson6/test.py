# списки

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list1:
    print(type(i))

print(list1[-1])
print(list1[0:5])
my_string = 'This is awesome string'
print(my_string[5:10])
odd_numbers = list1[0::2]
even_numbers = list1[1:10:2]
three_numbers = list1[2:10:3]
print(odd_numbers)
print(even_numbers)
print(three_numbers)
list_copy = list1[:]
print(list_copy)
print(list1)


list1.append(5)
list1.append(5)
list1.append(5)
numbers_5 = list1.pop(5)
print(list1)
list2 = ['a', 'b']

list1.extend(list2)
print(list1)

list1.insert(0, 0)
ind_0 = list1.index('a')
print(ind_0)
print(list1)
count_5 = list1.count(5)

list_alfavit = ['z', 'a', 'b', 'i', 'g', 'e', 'c']
list_alfavit.sort(reverse=True)
print(list_alfavit)
print(count_5)

# словники
chars = {'a': 1, "b": 2}

print(chars)
b_num = chars.pop('b')
print(b_num)
print(chars)
chars1 = {'c': 3, 'd': 4}
chars.update(chars1)
print(chars)
print(chars.get('a'))
chars.clear()
print(chars)
chars_copy = chars.copy()
print(chars == chars_copy)
name_phone = {
    'Oksana': '4332423',
    'Sasha': '43924823'
}

for k, v in name_phone.items():
    print(f'{k}: {v}')


# множини
list_numbers = ['+380937316048', '+380937316048', '+49328428342']
set_numbers = set(list_numbers)
print(set_numbers)
a_set = {1, 2, 3, 4}
a_set.add(5)
a_set.remove(5)
a_set.discard(6)
print(a_set)
b_set = {1, 3, 10, 12}
print(a_set & b_set)  # -> and
print(a_set ^ b_set)  # -> xor
print(a_set | b_set)  # -> or

# кортежі
tuple_a = (1, 2, 3, 5)
print(tuple_a[1])

# строка
my_string = "Its my string"

print(my_string[0] + my_string[1] + my_string[2])
print(my_string[0:3])

print(my_string.upper())
print(my_string)
print(my_string.lower())

list_numbers1 = ['+380937316048', '+43284854', '+438247237', '+9875348954']

for i in list_numbers1:
    if i.endswith('54'):  # True or False
        print('На 54')
    else:
        print('Не на 54')


password = 'qwerty123'
if 'qwerty' in password or '123' in password:
    print("This password it's wrong")


user = {
    'name': 'Bill',
    'surname': 'Samus',
    'age': 18
}

if 'age' in user:
    print(f'User is {user["age"]} years old')


password = input('Input password: ')
if len(password) < 8:
    print('Your password is too short')
else:
    print('Your password is True')
