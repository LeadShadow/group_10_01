# not, and, or

# A B A and B
# 1 1    1 -> True
# 1 0    0 -> False
# 0 1    0 -> False
# 0 0    0 -> False

# A B A or B
# 1 1    1
# 1 0    1
# 0 1    1
# 0 0    0

a = False
b = False
print(a or b)

# A not A
# 1    0
# 0    1

# name = input('Input name: ')
# age = int(input('Input age: '))
# driver_license = bool(input('Do you have driver license?: '))
#
# if name and age >= 18 and driver_license:
#     print(f'Human {name}, can rent a car')
# else:
#     print(f'Human {name}, can\'t rent a car')
#
#
# message = f'Human {name}, can rent a car' if name and age >= 18 and driver_license else f'Human {name}, can\'t rent a ' \
#                                                                                         f'car '
# print(message)
fruit = 'apple'
for i in fruit:
    print(i)

# Розробити банкового помічника, який буде допомагати обраховувати гривні в долари і навпаки
# в залежності від вибору(умову if data == <вибір>) і в залежності від вибору обрахувати і обробити
# помилку ValueError якщо з консолі вводять в змінну sum не число


while True:
    dollar_rate = 40.5
    print('Input 1 if you want transit hryvnias to dollars(exit that exit) ')
    print('Input 2 if you want transit dollars to hryvnias(exit that exit) ')
    data = input('Choose: ')
    if data == 'exit':
        print('Good Bye!')
        break
    sum = int(input('Enter the quantity: '))
    if data == '1':
        result = sum / dollar_rate
        print(f"{result} \n")
    elif data == '2':
        result = sum * dollar_rate
        print(f"{result} \n")


value = 'a'
try:
    value = int(value)
except ValueError:
    print(f'value {value} is not a number')
else:
    print(value > 0)
finally:
    print('This will be printed anyway')


age = input('How old are you? ')
try:
    age = int(age)  # -> ValueError
    if age >= 18:
        print('You are adult')
    else:
        print('You are infant')
except ValueError:
    print(f'{age} is not a number')


a = 0
while a < 10:
    a += 1
    if not a % 2:  # if a % 2 == 0
        continue
    print(a)
