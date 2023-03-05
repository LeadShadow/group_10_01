# Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый
# и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ <new_key>
# со значением <new_value>. Выведите на печать итоговый словарь. Важно чтобы сллварь остался
# тем же (имел тот же адрес в памяти)

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5"}

first_key, last_key = list(my_dict.keys())[0], list(my_dict.keys())[-1]
my_dict[last_key], my_dict[first_key] = my_dict[first_key], my_dict[last_key]
del my_dict[list(my_dict.keys())[1]]
new_key, new_value = "new_key", "new_value"
my_dict[new_key] = new_value

print(my_dict)