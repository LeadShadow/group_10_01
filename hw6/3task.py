# У нас есть список показателей студентов группы — это список с полученными
# балами по тестированию. Необходимо список поделить на две части.
# Напишите функцию split_list, которая принимает список (целые числа),
# находит среднее значение балла в списке и делит его на два списка.
# В первый попадают значения меньше среднего, включая среднее значение,
# а во второй — строго больше среднего. Функция возвращает кортеж этих двух списков.
# Для пустого списка возвращаем два пустых списка.

def split_list(grade):
    list_bigger = []
    list_smaller = []
    sum_grades = 0
    for i in grade:
        sum_grades += i
    average = sum_grades // len(grade)
    print(average)
    for i in grade:
        if i > average:
            list_bigger.append(i)
        elif i <= average:
            list_smaller.append(i)
    return list_bigger, list_smaller


if __name__ == "__main__":
    print(split_list([12, 12, 10, 9, 8, 5, 3]))

