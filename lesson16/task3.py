# При работе веб-сервисов общение по протоколу HTTP чаще всего происходит в формате JSON.
# И отправка данных на сервер при POST запросе — это необходимость использовать словарь,
# так как структура формата JSON идентична словарю Python.
#
# Реализуйте вспомогательную функцию, которая будет формировать запрос на сервер в виде
# словаря. Данная функция make_request(keys, values) принимает два параметра в виде списков.
# Функция должна создать словарь с ключами из списка keys и значениями из списка values.
#
# Порядок соответствия совпадает с индексами списков keys и data.
# Если длина keys и values не совпадают, верните пустой словарь.


# ['cat', 'age', 'owner'] ['Tom', 9, 'Sasha']
cat = ['cat', 'age', 'owner']
info = ['Tom', 9, 'Sasha']
print(dict(zip(cat, info)))


def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    return dict(zip(keys, values)) # keys[i]: values[i]

def make_request1(keys, values):
    dict1 = {}
    if len(keys) != len(values):
        return {}
    for i in range(len(keys)):
        dict1.update({keys[i]: values[i]})
    return dict1


if __name__ == "__main__":
    print(make_request(cat, info))
    print(make_request1(cat, info))