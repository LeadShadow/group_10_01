# Продолжаем расширять функциональность класса Contacts. На этом этапе мы добавим
# в класс метод get_contact_by_id. Метод должен искать контакт по уникальному id в
# списке contacts и возвращать словарь из него с указанным ключом id . Если словаря с
# указанным id в списке contacts не найдено, метод возвращает None.
#
# Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде.
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            'id': Contacts.current_id,
            'name': name,
            'phone': phone,
            'email': email,
            'favorite': favorite
        }
        Contacts.current_id += 1
        self.contacts.append(contact)
        return contact

    def get_contact_by_id(self):


contacts = Contacts()
print(contacts.add_contacts('Oleksandr', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))
print(contacts.add_contacts('Misha', '+380937316048', 'olexandr.samus.2004@gmail.com', True))