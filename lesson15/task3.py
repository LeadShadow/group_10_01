# Все вы, возможно, сталкивались с ребусами "Найди слово". Они существуют как текстовые варианты,
# так и программы для мобильных приложений. Напомним кратко суть ребуса. В большом квадрате с набором
# букв необходимо найти слово по горизонтали и, иногда, по вертикали.
# Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False)
# для нахождения искомого слова в строке ребуса.
#
# Параметры функции:
#
# riddle - строка с зашифрованным словом.
# word_length - длина зашифрованного слова.
# start_letter - буква, с которой начинается слово (подразумевается, что до начала слова
# буква не встречается в строке).
# reverse - указывает, в каком порядке записано слово. По умолчанию — в прямом.
# Для значения True слово зашифровано в обратном порядке, к примеру, в строке mi1rewopret
# зашифровано слово power.
# Функция должна возвращать первое найденное искомое слово. Если слово не найдено, вернуть пустую строку.

# К І Т Р Н У Г С

def solve_riddle(riddle:str, word_length:int, start_letter:str, reverse=False):
    if reverse:
        riddle = riddle[::-1]
        pos = riddle.rfind(start_letter, 0, len(riddle) - word_length)
    else:
        pos = riddle.find(start_letter, 0, len(riddle) - word_length)
    return '' if pos == -1 else riddle[pos:pos+word_length]  # pos = 1, [1:4]


if __name__ == "__main__":
    print(solve_riddle('РКІТГШЙУ', 3, 'П', reverse=True))
