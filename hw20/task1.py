# Создайте класс Animal. Также создайте экземпляр класса Animal (вместо реализации класса
# можете использовать pass) и присвойте переменной animal.

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


animal = Animal("cat", "Whiskers")