# Есть список contacts, элементы которого — словари контактов следующего вида:
#
#     {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }
# Словарь содержит имя пользователя, его email, телефонный номер и свойство — избранный контакт или нет.
#
# Разработайте функцию get_emails, которая получает в параметре список list_contacts и
# возвращает список, который содержит электронные адреса всех контактов из списка list_contacts.
# Используйте при этом функцию map.


def get_emails(list_contacts: list) -> list:
    return list(map(lambda contact: contact['email'], list_contacts))


contacts = [
    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Sasha Samus",
    "email": "olexandr.samus.2004@gmail.com",
    "phone": "+380937316048",
    "favorite": True,
},
{
    "name": "Sasha Samus",
    "email": "olexandr.samus.2004@gmail.com",
    "phone": "+380937316048",
    "favorite": True,
},
{
    "name": "Sasha Samus",
    "email": "olexandr.samus.2004@gmail.com",
    "phone": "+380937316048",
    "favorite": True,
},
{
    "name": "Sasha Samus",
    "email": "olexandr.samus.2004@gmail.com",
    "phone": "+380937316048",
    "favorite": True,
},
{
    "name": "Sasha Samus",
    "email": "olexandr.samus.2004@gmail.com",
    "phone": "+380937316048",
    "favorite": True,
},
{
    "name": "Sasha Samus",
    "email": "olexandr.samus.2004@gmail.com",
    "phone": "+380937316048",
    "favorite": True,
},
]


if __name__ == "__main__":
    print(get_emails(contacts))