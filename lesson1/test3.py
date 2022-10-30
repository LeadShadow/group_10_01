# Перепишіть приклад із теорії, але для позитивного числа перевіряйте — парне воно чи ні.
# Таким чином, після перевірок змінна result повинна містити одне з чотирьох значень:

# "Positive even number"
# "Positive odd number"
# "Negative number"
# "It is zero"
# Підказка: перевірка на парність виконується порівнянням залишку від розподілу на 2 з 0 або 1.
# Нагадаємо, залишок від розподілу можна отримати після операції %
# % -> залишок від ділення
# 2 4 6 8 10 12 14 16
# 1 3 5 7 9 11
# 3 % 2 -> 1
# 4 % 2 -> 0

num = int(input("Enter a number: "))

if num > 0:
    if num % 2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)

