# Разработайте функцию sanitize_file(source, output), переписывающую в текстовый файл output
# содержимое текстового файла source, очищенное от цифр.

# Требования:

# прочтите содержимое файла source, используя менеджер контекста with и режим "r".
# запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
# запись нового содержимого файла output должна быть единоразовая и использовать метод write
from pathlib import Path
import re

def sanitize_file(source: Path, output: str):
    with open(source, 'r', encoding='utf-8') as file:
        string_read = file.read()
        print(string_read)
        string = re.sub(r'\d', '', string_read)
        print(string)
    with open(output, 'w', encoding='utf-8') as file:
        file.write(string)

sanitize_file(Path('test.txt'), 'test1.txt')