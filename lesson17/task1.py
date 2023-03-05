# Напишите функцию to_indexed(source_file, output_file), которая будет считывать содержимое
# файла, добавлять к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.
#
# Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела,
# после чего должен идти текст строки из исходного файла. Нумерация строк идет от 0.


def to_indexed(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as file, open(output_file, 'w', encoding='utf-8') as fh:
        counter = 1
        for line in file:
            fh.write(str(counter) + ': ' + line)
            counter += 1


if __name__ == "__main__":
    to_indexed('test.txt', 'output.txt')