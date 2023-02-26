# Есть файл со списком сотрудников компании. В каждой строке файла записана информация
# только про одного сотрудника. Формат записи, в учебных целях, упрощенный в виде имени
# сотрудника, символа пробела и его должности, т.е. кем он работает.
#
# John courier
# Pipe cook
# Создайте функцию get_employees_by_profession(path, profession). Функция должна в файле
# (параметр path) найти всех сотрудников указанной профессии (параметр profession)
#
# Требования:
#
# откройте файл при помощи with для чтения.
# получите строки из файла при помощи метода readlines()
# с помощью метода find найдите все строки в файле, где есть указанная profession, и
# поместите записи в список.
# объедините все эти строки в списке в одну строку при помощи метода join
# (помните про перевод строк '\n' и лишние пробелы, которые надо убрать).
# уберите значение 'profession' (замените на пустую строку "" при помощи метода replace).
# верните итоговую строку из файла


def get_employees_by_profession(path, profession):
    with open(path, 'r', encoding='utf-8') as file:
        workers = file.readlines()  # ['John courier\n'
    result = []
    for worker in workers:
        man = worker.strip().split()  # ['John', 'courier']
        if man[1] == profession:
            result.append(man[0])
    return ', '.join(result)


if __name__ == "__main__":
    print(get_employees_by_profession('workers.txt', 'courier'))