"""
Запис в файл pathlib
"""
from pathlib import Path
list_data = ['First line', 'Hello world', 'Hi guys!', 'Last line']

# C:/Users/pc/Desktop/заняття/group_10_01/lesson10/Temp  + '/test.txt'
folder = Path('Temp')

with open(folder / 'test.txt', 'w', encoding='utf-8') as fh:
    for line in list_data:
        fh.write(line + '\n')

with open(folder / 'test1.txt', 'w', encoding='utf-8') as fh:
    fh.writelines(list_data)



