from collections import UserDict
from datetime import datetime, date


class Field:
    def __init__(self, value=None):
        self.value = value

    def validate(self, value):
        return value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = self.validate(new_value)


    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        super().validate(new_value)
        self._value = new_value

    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format.")
        return value

class Birthday(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        super().validate(new_value)
        self._value = new_value

    def validate(self, value):
        try:
            if value:
                datetime.strptime(str(value), '%Y-%m-%d')
            return value
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def days_until_birthday(self):
        today = datetime.now().date()
        birthday_date = datetime.strptime(str(self.value), '%Y-%m-%d').date().replace(year=today.year)

        if today > birthday_date:
            birthday_date = birthday_date.replace(year=today.year + 1)

        days_until_birthday = (birthday_date - today).days
        return days_until_birthday

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        phone_exists = any(p.value == old_phone for p in self.phones)
        if not phone_exists:
            raise ValueError(f"Phone number {old_phone} not found in the record.")

        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def days_to_birthday(self):
        if self.birthday.value:
            return self.birthday.days_until_birthday()
        else:
            return None

    def __str__(self):
        phone_info = '; '.join(p.value for p in self.phones)
        birthday_info = f"birthday: {self.birthday}, days until birthday: {self.days_to_birthday()}" if self.birthday.value else ""
        return f"Contact name: {self.name.value}, phones: {phone_info}, {birthday_info}"

class RecordIterator:
    def __init__(self, records, page_size):
        self.records = records
        self.page_size = page_size
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size

        if start_index >= len(self.records):
            raise StopIteration

        page_records = list(self.records.values())[start_index:end_index]
        self.current_page += 1
        return page_records
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterate_records(self, page_size):
        return RecordIterator(self.data, page_size)


if __name__ == "__main__":
    book = AddressBook()
    john_record = Record("John", birthday=date(1990, 1, 1))
    print(john_record, ' ****')

    john_record = Record("John", "1990-01-01")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    print(f"Days until John's next birthday: {john.days_to_birthday()}")

    book.delete("Jane")

    page_size = 2
    for page in book.iterate_records(page_size):
        for record in page:
            print(record)
        print("\n--- Next Page ---\n")