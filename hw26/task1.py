# У класса Point к механизму setter свойств x и y добавьте проверку на вводимое значение.
# Разрешите устанавливать значения свойств x и y для экземпляра класса, только, если они
# имеют числовое значение (int или float).
#
# Пример:
#
# point = Point("a", 10) print(point.x) # None print(point.y) # 10
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            print("Invalid value for x. Must be an integer or float.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y
        else:
            print("Invalid value for y. Must be an integer or float.")
