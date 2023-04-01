# Пусть есть строка с числами (в целях упрощения числа только целые), определяющая какие-то
# части общего дохода. Например,
#
# "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500,
# and the king gave $1000."
# Необходимо реализовать функцию generator_numbers, которая будет парсить строку и находить все
# целые числа в ней, и работая как генератор, отдавать указанные числа при обращении к ней в цикле.
#
# С парсингом строки мы уже сталкивались в задаче модуля 7, когда разбивали на лексемы
# арифметическое выражение
#
# Функция generator_numbers(string="") непосредственно распарсивает строку и при помощи
# yield возвращает текущее число.
#
# Функция sum_profit(string) суммирует числа, полученные от generator_numbers, и возвращает
# общую сумму прибыли из строки.
import re


def generator_numbers(string=''):
    str_to_list = re.split(r'\W+', string)
    print(str_to_list)
    for char in str_to_list:
        if char.isdigit():
            yield int(char)

def sum_profit(string):
    result = 0
    for num in generator_numbers(string):
        result += num
    return str(result) + "$"


if __name__ == "__main__":
    print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))