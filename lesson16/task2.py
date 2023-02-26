# Возвращает количество (количество) гласных в заданной строке. Мы будем рассматривать
# a, e, i, o, u как гласные для этой Ката (но не y). Входная строка будет состоять только
# из строчных букв и/или пробелов.

# 'Sasha'


def get_count(s: str) -> int:
    count = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count += 1
    return count


if __name__ == "__main__":
    print(get_count('Sasha'))
