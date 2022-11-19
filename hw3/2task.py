# Введено число з клавіатури, знайти мінімальне та максимальне значення введеного числа,
# створити дві змінні поза циклом sum_min, sum_max -> знайти суму всіх чисел до мінімального
# та максимального числа використовуючи цикл for та діапазон range


n = input('Enter a number: ')
print(n[0])
max = int(n[0])
min = int(n[0])
sum_min = 0
sum_max = 0
for ch in n:
    num = int(ch)
    if num > max:
        max = num
    if num < min:
        min = num


for i in range(0, max+1):
    sum_max += i
for i in range(0, min+1):
    sum_min += 1
