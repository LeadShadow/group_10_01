from lesson7.task1 import sanitize_phone_number
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380
# Напишите функцию get_phone_numbers_for_countries, которая будет:
#
# Принимать список телефонных номеров.
# Нормализовать полученный список телефонов клиентов с помощью нашей функции sanitize_phone_number.
# Сортировать телефонные номера по указанным в таблице странам.
# Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
# {
#     "UA": [<здесь список телефонов>],
#     "JP": [<здесь список телефонов>],
#     "TW": [<здесь список телефонов>],
#     "SG": [<здесь список телефонов>],
# }
# Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в
# список словаря с ключом "UA".
# ["    +38023423(42)  ", "+65(10)432848273"]
# 3802342342


def get_phone_numbers_for_countries(list_phones: list) -> dict:
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone.startswith('81'):
            list1.append(phone)
            continue
        elif phone.startswith('65'):
            list2.append(phone)
            continue
        elif phone.startswith('886'):
            list3.append(phone)
            continue
        else:
            list4.append(phone)
            continue
    return {"JP": list1, "SG": list2, "TW": list3, "UA": list4}


