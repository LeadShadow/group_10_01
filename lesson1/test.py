# user_input = input('Input something: ')
# print(type(user_input))
a = 0.3

# int, float, str, None, Boolean
x = 0.1
b = 0.2
# c = str(x)
# print(type(b))
# print(type(c))
g = x + b
# Boolean - True or False -> 1 0
print(a == round(g, 2))



# if, elif, else

if a > g:
    print('hello world')
elif a <= g:
    print('hello')
else:
    print('world')


# age = int(input('How old are you?: '))
#
# if age > 18:
#     print('You are adult already')
# elif age == 18:
#     print('You only 18')
# else:
#     print('You are infant yet')


# num = int(input('Введіть число '))
# if num > 0:
#     print('Число додатнє')
# if num < 0:
#     print("Число від'ємне")
# elif num == 0:
#     print('Число == нуль')


# a = int(input('Введіть число: '))
# if a > 0:
#     print('Число додатнє')
# elif a == 1:
#     print('Число == 1')
# else:
#     print('a <= 0')


money = None  # False
if money:  # if False -> ніколи не виконається
    print(f'You have {money}')
else:
    print("You haven't money")

# None -> False
work_experience = int(input ("Enter your full work expirience in years: "))


if 1 < work_experience <= 5:
    print(f"You are Middle")
if work_experience <= 1:
    print(f"You Are Junior")
else:
    print("You are Senior")
