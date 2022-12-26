from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        if isinstance(phone, Phone):
            self.phones.append(phone)
            return f'{phone.value} add success to contact {self.name.value}'
        return f'Sorry, phone must be a Phone instance'

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        self.phones[self.phones.index(old_phone)] = new_phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('123457')
    rec = Record(name, phone)
    phone2 = Phone('0987654')
    print(rec.add_phone(phone2))
    phone3 = '555555555'
    print(rec.add_phone(phone3))

    print(rec.phones)

    rec.edit_phone(phone2, Phone('6788989'))

    print(rec.phones)