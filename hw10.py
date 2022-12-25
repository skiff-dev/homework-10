from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        new_phone = ''
        for i in filter(lambda x: x.isnumeric(), phone):
            new_phone += i
        self.phones.append(new_phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(old_phone)] = new_phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
