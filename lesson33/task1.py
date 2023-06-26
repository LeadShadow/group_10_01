# Есть список, каждый элемент которого — это словарь с контактами пользователя следующего вида:
#
# { "name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite":
# False, }
# Словарь содержит имя пользователя name, его email, телефонный номер phone и свойство favorite —
# избранный контакт или нет.
#
# Разработайте две функции для сериализации и десериализации списка контактов с помощью пакета csv и
# хранения полученных данных в текстовом файле.
#
# Первая функция write_contacts_to_file принимает два параметра: filename — имя файла, contacts —
# список контактов. Она сохраняет указанный список в файл формата csv.
#
# Структура csv файла должна быть следующей:
#
# name,email,phone,favorite Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
# Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
# Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
# Wylie Pope,est@utquamvel.net,(692) 802-2949,False
# Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
# Обратите внимание, первой строкой в файле идут заголовки — это названия ключей.
#
# Вторая функция read_contacts_from_file читает, выполняет преобразование данных и возвращает указанный
# список contacts из файла filename, сохраненного ранее функцией write_contacts_to_file.
#
# Примечание: При чтении csv файла мы получаем свойство словаря favorite в виде строки, т.е. например
# favorite='False' . Необходимо его привести к логическому выражению обратно, чтобы стало favorite=False.

import csv


def write_contacts_to_file(filename, contacts):


def read_contacts_from_file(filename):