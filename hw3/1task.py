# Ввести рядок з клавіатури, пробігтись в циклі, підрахувати кількість букв а, в рядку, і
# якщо ця кількість - парна, то вивести на екран 'кількість букв а - парна', якщо непарна, то
# вивести 'кількість букв а - непарна'

some_text = input('Input some text: ')

count_a = 0
for i in some_text:
    if i == 'a':
        count_a += 1

if count_a % 2 == 0:
    print('кількість букв а - парна')
else:
    print('кількість букв а - непарна')



data = [10, 20, 30, 40]
data.pop()
print(data)



i = 'welcome'
y = [2, 5j, 6]

y.sort()
print(y)