# Напишіть функцію sum_range(start, end), яка сумує всі цілі числа від
# значення start до end включно. Якщо користувач задасть перше число більше ніж друге
# просто поміняйте їх місцями


def sum_range(start: int, end: int) -> int:
    sum = 0
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        sum += i
    return sum


print(sum_range(10, 0))
