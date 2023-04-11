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
# Создайте функцию get_favorites(contacts), которая будет возвращать список, содержащий только
# избранные контакты. Используйте при этом функцию filter, чтобы отфильтровать по полю favorite
# только избранные контакты.

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone": "(555) 123-4567",
        "favorite": True,
    },
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "(555) 987-6543",
        "favorite": True,
    },

]



def get_favorites(contacts):
    return list(filter(lambda contact: contact["favorite"], contacts))

favorites = get_favorites(contacts)
print(favorites)