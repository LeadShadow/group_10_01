"""
Именованные кортежи
Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж с
возможностью присвоить каждому
элементу имя, по которому в дальнейшем можно получить доступ
"""
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Cat = collections.namedtuple('Cat', ['nick', 'age', 'owner'])
print(Cat.__name__)
cat = Cat('Tom', 9, 'Lead')
print(cat.nick, cat.age, cat.owner)

print(f'This is cat {cat.nick}, {cat.age} age, his owner {cat.owner}')

