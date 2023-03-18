# Функция как объект первого класса

# Третье требование - функция может быть возвращена из функции как результат


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def ops(operator: str):
    if operator == '*':
        return mul
    elif operator == '+':
        return add
    else:
        raise ValueError('operator not supported')


try:
    f_mul = ops('*')
    result = f_mul(2, 4)
    print(result)
except ValueError:
    print('Не вийшло виконати операцію')


try:
    f_add = ops('+')
    result = f_add(2, 4)
    print(result)
except ValueError:
    print('Не вийшло виконати операцію')


try:
    f_div = ops('/')
    result = f_div(2, 4)
    print(result)
except ValueError:
    print('Не вийшло виконати операцію')