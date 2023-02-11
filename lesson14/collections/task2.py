"""
Counter
Например есть набор температур за первые 15 дней января. Найти количество общих температур,
наиболее частую
"""

import collections

temperatures = [0.5, 0.0, -3.5, 0.0, 2.5, -3.5, 4.0, 0.5, 3.5, 0.0, 6.0, 2.5, 7.0]

count = collections.Counter(temperatures)
print(count)
print(count.most_common(1))
print(count.most_common())