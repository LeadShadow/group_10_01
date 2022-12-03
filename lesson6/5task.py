# Всем известно, что для доступа к кредитной карте банка необходим пин-код. Классически сложилось,
# что это сочетание четырех цифр. Нам необходимо решить следующую программистскую задачу.
# Есть подготовленный список пин-кодов. Напишите функцию is_valid_pin_codes, которая будет
# принимать в качестве параметра список этих пин-кодов — строка из четырех цифр, и возвращать
# логическое значение — валидный список или нет. Убедитесь в том, что среди этих пин-кодов в
# списке не будет дубликатов, все они хранятся в виде строк, их длина равна 4 символам и содержат
# они только цифры.
list_a = [1, 2, 2]
print(set(list_a))
list_codes = ['100g', '1000', '4040']


def is_valid_pin_codes(pin_codes: list) -> bool:
    if len(pin_codes) > len(set(pin_codes)) or len(pin_codes) == 0:
        return False
    for code in pin_codes:
        if len(code) != 4 or type(code) != str:
            return False
        for i in code:
            if i not in '0123456789':
                return False
    return True


if __name__ == "__main__":
    print(is_valid_pin_codes(list_codes))
