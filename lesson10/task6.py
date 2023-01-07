""""
Робота з файлами середовища pathlib
"""
from pathlib import Path

filetext = Path('Test/my_text_file.txt')


filetext.write_text('First block\nSecond block\nThird block')
print(filetext.read_text())

# 101001010101010101101010101011001010
file_bin = Path('Test/my_bin.bin')
file_bin.write_bytes(b'Binary data')
print(file_bin.read_bytes().decode())




