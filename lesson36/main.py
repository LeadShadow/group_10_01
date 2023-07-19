# Добавить функционал сохранения адресной книги на диск и восстановления с диска.
# Для этого вы можете выбрать любой удобный для вас протокол сериализации/десериализации
# данных и реализовать методы, которые позволят сохранить все данные в файл и загрузить
# их из файла.
#
# Добавить пользователю возможность поиска по содержимому книги контактов, чтобы можно
# было найти всю информацию об одном или нескольких пользователях по нескольким цифрам
# номера телефона или буквам имени, и т.п.
#
# Критерии приёма:
# Приложение не теряет данные после выхода из приложения и восстанавливает их из файла.
# Приложение выводит список пользователей, у которых в имени или номере телефона есть
# совпадения с введенной строкой.
import pickle
from collections import UserDict
import re
from datetime import datetime, date
from pathlib import Path


N = 3


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        def is_code_valid(phone_code: str) -> bool:
            if phone_code[0:2] in ('03', '04', '05', '06', '09'):
                return True
            return False
        result = None
        phone = value.removeprefix('+').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if phone.isdigit():
            if phone.startswith('0') and len(phone) == 10 and is_code_valid(phone[:3]):
                result = '+38' + phone  # 0937316048 -> +380937316048
            elif phone.startswith('380') and len(phone) == 12 and is_code_valid(phone[2:5]):
                result = '+' + phone  # 380937316048 -> +380937316048
            elif 10 <= len(phone) <= 14 and not phone.startswith('0') and not phone.startswith('380'):
                result = '+' + phone
        if result is None:
            raise ValueError(f'Неправильний тип значення {value}')
        self.__value = result


class Birthday(Field):
    def __str__(self):
        if self.value is None:
            return 'Unknown!'
        else:
            return f'{self.value: %d %b %Y}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value is None:
            self.__value = None
        else:
            try:
                self.__value = datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                try:
                    self.__value = datetime.strptime(value, '%d.%m.%Y').date()
                except ValueError:
                    raise DateIsNotValid

class Record:
    def __init__(self, name: Name, phones=[], birthday=None) -> None:
        self.name = name
        self.phone_list = phones
        self.birthday = birthday

    def __str__(self) -> str:
        return f'User \033[35m{self.name.value}\033[0m - Birthday {self.birthday}\n' \
               f'Phones: {", ".join([phone for phone in self.phone_list])}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone)

    def del_phone(self, phone: Phone) -> None:
        self.phone_list.remove(phone)

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        self.phone_list.remove(phone)
        self.phone_list.append(new_phone)

    def days_to_birthday(self, birthday):
        if birthday.value is None:
            return None
        this_day = date.today()
        birthday_day = date(this_day.year, birthday.value.month, birthday.value.day)
        if birthday_day < this_day:
            birthday_day = date(this_day.year + 1, birthday.value.month, birthday.value.day)
        return (birthday_day - this_day).days


class AddressBook(UserDict):
    def __init__(self, filename: str) -> None:
        super().__init__()  # виклик базового конструктора
        self.filename = Path(filename)
        if self.filename.exists():
            with open(self.filename, 'rb') as file:
                self.data = pickle.load(file)

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def iterator(self, func=None, days=0):
        index, print_block = 1, '-' * 50 + '\n'
        for record in self.data.values():
            if func is None or func(record):
                print_block += str(record) + '\n'
                if index < N:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, '-' * 50 + '\n'
        yield print_block

    def save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.data, file)

class PhoneUserAlreadyExists(Exception):
    """You cannot add an existing phone number to a user"""

class DateIsNotValid(Exception):
    """You cannot add an invalid date"""


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        except IndexError:
            return 'Error! Give me name and phone please!'
        except KeyError:
            return 'Error! User not found!'
        except ValueError:
            return 'Error! Phone number is incorrect'
        except PhoneUserAlreadyExists:
            return 'Error! You cannot add an existing phone number to a user'
        except DateIsNotValid:
            return 'Error! Date is not valid'

class InputError_for_birthday:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        except ValueError:
            return 'Error! Give me days for birthday contact'


def verify_phone(phone: str) -> str:
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-Zа-яА-Я]', '', phone)
    return new_phone


def hello(*args: tuple) -> str:
    return 'Hello! How can I help you?'


# add (Sasha)
@InputError
def add_contact(contacts: AddressBook, *args: tuple) -> str:
    name, phone = Name(args[0]), Phone(args[1])
    phone = verify_phone(phone.value)
    if name.value in contacts:
        if phone in contacts[name.value].phone_list:
            raise PhoneUserAlreadyExists
        else:
            contacts[name.value].add_phone(phone)
            return f'Add phone {phone} to user {name}'
    else:
        if len(args) > 2:
            birthday = Birthday(args[2])
        else:
            birthday = Birthday(None)
        contacts[name.value] = Record(name, [phone], birthday)
        return f'Add user {name} with phone number {phone}'


@InputError
def add_birthday(contacts, *args):
    name, birthday = args[0], args[1]
    contacts[name].birthday = Birthday(birthday)
    return f'Add/modify birthday: {contacts[name].birthday} to user {name}'


@InputError
def days_to_user_birthday(contacts, *args):
    name = args[0]
    if contacts[name].birthday.value is None:
        return 'User has no birthday'
    return f'{contacts[name].days_to_birthday(contacts[name].birthday)} days to user {name} birthday'


@InputError_for_birthday
def show_birthday(contacts: AddressBook, *args):
    days = int(args[0])
    result = f'List of users with birthday in {days} days: \n'
    print_list = contacts.iterator(days)
    for item in print_list:
        result += f'{item}'
    return result


@InputError
def change_contact(contacts, *args):
    name, old_phone, new_phone = args[0], args[1], args[2]
    new_phone = verify_phone(new_phone)
    contacts[name].edit_phone(old_phone, new_phone)
    return f"Change user's {name} phone number from {old_phone} to {new_phone}"


@InputError
def del_phone(contacts, *args):
    name, phone = args[0], args[1]
    contacts[name].del_phone(verify_phone(phone))
    return f'Delete phone {phone} from user {name}'


@InputError
def show_phone(contacts: dict, *args) -> str:
    name = args[0]
    return f'{contacts[name]}'


def show_all(contacts: AddressBook, *args) -> str:
    if not contacts:
        return 'AddressBook is empty'
    result = 'List of all users: \n'
    print_list = contacts.iterator()
    for item in print_list:
        result += f'{item}'
    return result


def goodbye(contacts, *args):
    contacts.save()
    return 'GoodBye!'


def help(*args) -> str:
    return """Command format:
help or ? - help
hello - greeting
add <name> <phone> - add user to dictionary
change <name> <old_phone> <new_phone> - change user's phone number
birthday <name> <birthday> - add/modify the user's birthday
days to birthday <name> - show how many days to user's birthday
show birthday days N - show the user's birthday in the next N days
del <name> <phone> - delete the user's phone number
phone <name> - show user
show all - all contacts
close or . or exit or stop - exit the program"""


def unknown_command(*args):
    return 'Unknown command!'


def search(contacts: AddressBook, *args):
    def func_sub(record):
        return substring.lower() in record.name.value.lower() or any(substring in phone.value for phone in record.phone_list) or (record.birthday.value is not None and substring in record.birthday.value.strftime("%d.%m.%Y"))
    substring = args[0]
    result = f'List of all users with "{substring.lower()}"\n'
    print_list = contacts.iterator(func_sub)
    for item in print_list:
        result += f'{item}\n'
    return result


@InputError
def del_user(contacts, *args):
    name = Name(args[0])
    yes_no = input(f'Are you sure, you want to delete the user {name.value}? (Y/n)')
    if yes_no == 'Y':
        del contacts[name.value]
        return f'Delete user {name.value}'
    return f'User not deleted'


def clear_all(contacts, *args):
    yes_no = input(f'Are you sure, you want to clear addressbook? (Y/n)')
    if yes_no == 'Y':
        contacts.clear()
        return f'AddressBook is empty'
    return f'Removal canceled'


COMMANDS = {hello: ['hello'], add_contact: ['add '], change_contact: ['change '], show_phone: ['phone '],
            help: ['?', 'help'], show_all: ['show all'], goodbye: ['good bye', 'close', 'exit', 'stop', '.'],
            del_phone: ['del '], add_birthday: ['birthday'], days_to_user_birthday: ['days to birthday'],
            show_birthday: ['show birthday days'], search: ['find', 'search'], del_user: ['delete'], clear_all: ['clear']}


def command_parser(user_command: str) -> (str, list):
    for key, values in COMMANDS.items():
        for value in values:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    contacts = AddressBook(filename='contacts.dat')
    while True:
        user_command = input('Enter command: ')
        command, data = command_parser(user_command)
        print(command(contacts, *data), '\n')
        if command is goodbye:
            break


if __name__ == "__main__":
    main()