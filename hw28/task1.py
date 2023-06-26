# Магический метод __getstate__ вызывается, когда pickle пытается получить представление
# объекта в виде byte-строки. В обычной реализации __getstate__ возвращает __dict__ словарь,
# в котором хранятся все атрибуты класса. Но вы можете поменять этот метод.

# Мы продолжим расширять пример из предыдущей задачи. Добавьте в класс Contacts атрибут count_save,
# по умолчанию он должен иметь значение 0. Реализуйте магический метод __getstate__ для класса Contacts.
# При упаковке экземпляра класса метод должен увеличивать значение атрибута count_save на единицу.
# Таким образом, это свойство — счетчик повторных операций упаковок экземпляра класса.
#
# Пример работы кода:
#
# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# first = persons.read_from_file()
# first.save_to_file()
# second = first.read_from_file()
# second.save_to_file()
# third = second.read_from_file()
# print(persons.count_save) # 0
# print(first.count_save) # 1
# print(second.count_save) # 2
# print(third.count_save) # 3

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
