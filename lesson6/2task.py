# Написати функцію useless(list) де параметр list буде випадковий список
# Знайти в цьому списку максимальне значення і розділити його на довжину списка


def useless(list: list) -> int:
    max = 0
    for i in list:
        if i > max:
            max = i
    return max // len(list)


print(useless([1, 3, 5, 9, 11, 16, 4, 6]))


