# Вначале четвертого модуля мы решали задачу выплат по коммунальным платежам.
# Они представляли собой список payment с положительными и отрицательными значениями.
# Создайте функцию positive_values и с помощью функции filter отфильтруйте список payment
# по положительным значениям, и верните его из функции.

#
payment = [100, -3, 400, 35, -100]
def positive_values(list_payment):
    return list(filter(lambda num: num > 0, list_payment))


def positive_values1(list_payment):
    list1 = []
    for i in list_payment:
        if i > 0:
            list1.append(i)
    return list1

if __name__ == "__main__":
    print(positive_values(payment))
    print(positive_values1(payment))