# В арифметическом выражении лексемами являются: операторы, числа и скобки. Операторами у нас
# будут следующие символы: * , /, - и +. Операторы и скобки легко выделить в строке — они состоят
# из одного символа и никогда не являются частью других лексем. Числа выделить сложнее,
# поскольку эти лексемы могут состоять из нескольких символов. Поэтому любая непрерывная
# последовательность цифр — это одна числовая лексема.
# Напишите функцию, принимающую в качестве параметра строку, содержащую математическое выражение,
# и преобразующую ее в список лексем. Каждая лексема должна быть либо оператором, либо числом, либо скобкой.
#
# Пример:
#
# "2+ 34 -5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
# В целях упрощения считаем, что числа могут быть только целыми, и входная строка всегда будет
# содержать математическое выражение, состоящее из скобок, чисел и операторов.
#
# Обратите внимание, что лексемы могут отделяться друг от друга разным количеством пробелов,
# а могут и не отделяться вовсе. Пробелы не являются лексемами и в итоговый список попасть не должны.

import re
# 0 1 2 3 4 5 6 7 8 9 189 4378 3298382 38283 28382
# \( -> '('
'didn\'t'
def parser(s:str) -> list:
    return re.findall(r'\d+|[\(\)\+\-\*]', s)


if __name__ == "__main__":
    print(parser("(2+ 34 -5 * 3)"))