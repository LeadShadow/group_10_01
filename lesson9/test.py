from pathlib import Path


p = Path('C:/Users/pc/Desktop/заняття/group_10_01/lesson9')

print(p.parent)
print(p.name)
print(p.suffix)
print(p.exists())
print(p.is_dir())
print(p.is_file())


for i in p.iterdir():
    print(i.name)


# 'r' -> відкриття на читання (значення за замовчуванням)
# 'w' -> відкриття на запис, все шо в нас в файлі видаляється, якшо файла не існує, то створює новий
# 'x' -> відкриття на запис, все шо в нас в файлі видаляється, якщо файлу не існує, буде помилка
# 'a' -> вікриття на дозапис, інформація додається в кінець файлу
# 'b' -> запис в бінарному вигляді(1010101010101010101)
# 't' -> відкриття в текстовому режимі
# '+' -> відкриття на запис і на читання

fh = open('test_file.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)
fh.close()


fh = open('test.txt', 'w')
fh.write('Hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)
fh.close()


fh = open('test.txt', 'w')
fh.write('Hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()


fh = open('test.txt', 'w', encoding='utf-8')
fh.write('first line\nsecond line\nthird line')
fh.close()


fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)
fh.close()


fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)

fh.close()

with open('text.txt', 'w+') as fh:
    fh.write('hello!')
