# ���������� ����� __getstate__ ����������, ����� pickle �������� �������� �������������
# ������� � ���� byte-������. � ������� ���������� __getstate__ ���������� __dict__ �������,
# � ������� �������� ��� �������� ������. �� �� ������ �������� ���� �����.

# �� ��������� ��������� ������ �� ���������� ������. �������� � ����� Contacts ������� count_save,
# �� ��������� �� ������ ����� �������� 0. ���������� ���������� ����� __getstate__ ��� ������ Contacts.
# ��� �������� ���������� ������ ����� ������ ����������� �������� �������� count_save �� �������.
# ����� �������, ��� �������� � ������� ��������� �������� �������� ���������� ������.
#
# ������ ������ ����:
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
