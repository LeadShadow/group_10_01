print('hello world')
print('hello world')


def say_hello():  # локальне сховище
    print('Привіт, світ!')


print('hello world')
say_hello()


def print_max(a=3, b=3):
    # a -> 3, b -> 4
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, '==', b)
    else:
        print(b, 'максимально')


print_max(3, 4)  # пряма передача значень

x = int(input('Введіть число: '))
y = int(input('Введіть число: '))
print_max(x, y)  # передача змінних в якості аргументів
print_max()


def plus(a, b):
    return a + b


result = plus
print(result(3, 4))


x = 50
print(x)


def func(x):
    x = 2
    return x


x = func(x)
print('x вже', x)


def func_1(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')


func_1(a=3)
func_1(b=3, c=12, a=5)
func_1(a=3)


def say(message, times=1):
    print(message * times)


say('Привіт')
say('Привіт', 5)


def total(a=5, *numbers, **phone_book):
    print('a', a)
    print(numbers)
    print(phone_book)


print(total(10, 1, 2, 3, 1111, 2212))

