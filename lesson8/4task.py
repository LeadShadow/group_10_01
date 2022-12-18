# Для закрепления материала напишите функцию find_all_words, которая ищет совпадение слова в тексте.
# Функция возвращает список всех нахождений слова в параметре word в тексте в любом виде написания, т.е. например,
# возможные варианты написания слова "Python" как pYthoN, pythOn, PYTHOn и т.д. главное, чтобы сохранялся
# порядок слов, регистр не имеет значение.
#
# Подсказка: функции модуля re принимают еще последний параметр flags и мы можем определить нечувствительность к
# регистру, присвоив ему значение re.IGNORECASE
import re


def find_all_words(text: str, word: str) -> str:
    s = re.findall(word, text, flags=re.IGNORECASE)
    return s


if __name__ == "__main__":
    print(find_all_words('PyThon is the best language', 'python'))
