# Методы: __new__ и __init__


class Foo:
    def __new__(cls, *args, **kwargs):
        print('Метод new Foo')
        print(args)
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print('Конструктор Foo')
        self.value = value


foo = Foo(10)  # __new__() -> __init__
foo1 = Foo(20)

print(foo.value, foo1.value)
print(foo, foo1)