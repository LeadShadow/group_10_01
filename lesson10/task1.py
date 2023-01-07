# # Приклад 1
# # Наступна програма зчитує весь вміст файлу input.txt, записує його в змінну s,
# а потім виводить її в файл output.txt.
# Нехай в файл input.txt записано We are learning Python programming language

fh1 = open('input.txt', 'r')
fh2 = open('output.txt', 'w')
s = fh1.read()
fh2.write(s)
fh1.close()
fh2.close()

