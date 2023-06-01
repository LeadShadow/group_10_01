# У класса Point через конструктор __init__ объявлены два атрибута: координаты x и y.
# Скройте доступ к ним с помощью двойного подчеркивания: __x и __y
#
# Реализуйте для класса Point механизмы setter и getter к атрибутам __x и __y с помощью
# декораторов property и setter.
#
# Пример:
#
# point = Point(5, 10)
#
# print(point.x)  # 5
# print(point.y)  # 10

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y