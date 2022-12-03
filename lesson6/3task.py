# Написати функцію. Є послідовність чисел - наприклад список, перевірити чи всі значення в
# ньому будуть унікальними(не повторюватись)


def check_unique(list: list) -> str:
    if len(list) > len(set(list)):
        return 'Є неунікальні значення'
    if len(list) == len(set(list)):
        return 'Все ок!'


print(check_unique([1, 3, 4, 5, 6]))

