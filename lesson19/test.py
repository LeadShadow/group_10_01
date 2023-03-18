SOME_VAR = 3

def func(x):
    SOME_VAR = x
    print(SOME_VAR)


def procedure():
    print(SOME_VAR)


procedure()  # 3
func(5)  # 5
print(SOME_VAR)  # 3


GLOBAL_SCOPE_VAR = 1

def func():
    enclosed_scope_var = 2
    def inner():
        inner_var = 3


# Замикання
def adder(val):
    def inner(x):
        return x + val
    return inner


two_adder = adder(3)
print(two_adder(3))

three_adder = adder(3)
print(three_adder(3))  # 8
print(three_adder(-3))  # 0

print(two_adder == three_adder)


# Карірування
# Каррирование — это преобразование функции от многих аргументов в набор функций, каждая из которых
# является функцией от одного аргумента. Мы можем передать часть аргументов в функцию и получить
# обратно функцию, ожидающую остальные аргументы.

def handle_operation(x, y, operator):
    if operator == '-':
        return x - y
    elif operator == '+':
        return x + y


handle_operation(2, 3, '+')  # 5
handle_operation(2, 3, '-')  # -1


def sum_func(x, y):
    return x + y

def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}

def get_handler(operator):
    return OPERATIONS[operator]


handler = get_handler('-')
print(handler(2, 3))  # -1
