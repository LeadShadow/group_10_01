# Для списка numbers подсчитать сумму элементов с помощью функции reduce.
#
# numbers = [3, 4, 6, 9, 34, 12]
# Создайте функцию sum_numbers(numbers), результатом выполнения которой будет сумма чисел
# всех элементов списка numbers.

from functools import reduce

# reduce(func, iterable[, initial])
numbers = [3, 4, 6, 9, 34, 12]
def sum_numbers(numbers):
    return reduce(lambda a, b: a + b, numbers, 0)


def sum_num(numbers):
    summ = 0
    for i in numbers:
        summ += i
    return summ

print(sum_num(numbers))
print(sum_numbers(numbers))
