from time import time

baz = int(input('Enter a number: '))
foo = int(input('Enter a number: '))


if baz < foo:
    baz, foo = (baz + foo) / 2, baz * foo  # розпаковка кортежу
else:
    foo, baz = (foo + baz) / 2, foo * baz

print(baz, foo)


sum = 0
count = 26
# for _ in range(1, 26+1):
#     sum += 5  # 26 * 5
while count > 0:
    sum += 5
    count -= 1


print(sum)


num = int(input('Enter the first number: '))
print(type(num))
print(type(str(num)))
length = len(str(num))  # len -> integer
print(length)

if length == 2 and num % 2 == 0:
    print('Парне двузначне число')
else:
    print('Ні')


sum = 0
for i in range(1, 3):
    print('----')
    for _ in range(1, 26):
        if sum >= 10:
            break
        else:
            sum *= 1391293
    print(i)

print(sum)


n = input('Enter a number: ')

count_zero = 0

for i in n:  # 1000
    if i == '0':
        count_zero += 1

print(count_zero)


n = input('Enter a number: ')
print(n[0])
max = int(n[0])
min = int(n[0])
sum = 0
for ch in n:
    num = int(ch)
    sum += num
    if num > max:
        max = num
    if num < min:
        min = num

print(f'max = {max}, min = {min}, sum = {sum}')



string = input('Введіть строку: ')

count_symbols = 0
count_a = 0
count_b = 0
count_c = 0
count_space = 0


for i in string:
    count_symbols += 1
    if i == 'a':
        count_a += 1
    if i == 'b':
        count_b += 1
    if i == 'c':
        count_c += 1
    if i == ' ':
        count_space += 1


print(f'count_symbols = {count_symbols}, count_a = {count_a}, count_b = {count_b}, count_c = {count_c}, count_spaces = {count_space}')


a = 10
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1


num = input('Введіть число: ')
result = None

try:
    result = 2 / int(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
else:
    print(result)


a = 'hello'

for i in a:
    print(i)
