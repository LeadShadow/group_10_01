# Создайте список, который называется surprise и содержит элементы 'Groucho',
# 'Chico' и 'Harpo'.
# Напишите последний элемент списка surprise со строчной буквы,
# затем обратите его и напишите с прописной буквы.


def get_last_word(list1: list) -> None:
    print(list1[-1].title())
    print(list1[-1].lower())


if __name__ == "__main__":
    get_last_word(['Groucho', 'Chico', 'Harpo'])

