# Создайте функцию decimal_average(number_list, signs_count), которая
# будет вычислять среднее арифметическое типа Decimal с количеством значащих
# цифр signs_count.
#
# number_list — список чисел
#
# Внимание
# Не забывайте приводить все числа в списке к типу `decimal`
#
# Пример:
#
# вызов функции decimal_average([3, 5, 77, 23, 0.57], 6) вернет 21.714
# вызов функции decimal_average([31, 55, 177, 2300, 1.57], 9) вернет 512.91400

from decimal import Decimal, getcontext

def decimal_average(number_list: list, signs_count: int):
    getcontext().prec = signs_count
    decimal_list = [Decimal(i) for i in number_list]
    dec_list = []
    for i in number_list:
        dec_list.append(Decimal(i))
    return sum(decimal_list) / len(decimal_list)


if __name__ == "__main__":
    print(decimal_average([31, 55, 177, 2300, 1.57], 9))