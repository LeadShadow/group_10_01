"""
defaultdict
collections.defaultdict ничем не отличается от обычного словаря за исключением того, что
по умолчанию всегда вызывается
функция, возвращающая значение:
"""

from collections import defaultdict

data = defaultdict(list)
print(data)
data[0].append(10)
print(data)

colors = [('yellow', 1), ('blue', 3), ('yellow', 5), ('red', 15)]
colors_dict = defaultdict(list)

for k, v in colors:
    colors_dict[k].append(v)
print(colors_dict)
