import json
from datetime import datetime, date
from collections import UserDict

class Field:
    def __init__(self, value=None):
        self._value = self.validate(value)

    def validate(self, value):
        return value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = self.validate(new_value)

    def __str__(self):
        return str(self._value)

class Name(Field):
    pass

class Phone(Field):
    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format.")
        return value

class Birthday(Field):
    def validate(self, value):
        if value is not None:
            try:
                datetime.strptime(str(value), '%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        return value

    def days_until_birthday(self):
        today = datetime.now().date()
        if self._value:
            birthday_date = datetime.strptime(str(self._value), '%Y-%m-%d').date().replace(year=today.year)

            if today > birthday_date:
                birthday_date = birthday_date.replace(year=today.year + 1)

            days_until_birthday = (birthday_date - today).days
            return days_until_birthday

class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
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

def record_encoder(record):
    if isinstance(record, Record):
        return {
            "name": record.name.value,
            "phones": [phone.value for phone in record.phones],
            "birthday": record.birthday.value.strftime('%Y-%m-%d') if record.birthday.value else None
        }
    return record.__dict__

class AddressBook(UserDict):
    def add_record(self, record):
        existing_record = self.data.get(record.name.value)
        if existing_record:
            existing_record.phones.extend(record.phones)
            existing_record.birthday = record.birthday
        else:
            self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterate_records(self, page_size):
        return RecordIterator(self.data, page_size)

    def save_to_disk(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file, default=record_encoder, indent=2)

    def load_from_disk(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.data = {name: Record(**record_data) for name, record_data in data.items()}

    def search(self, query):
        results = []
        for record in self.data.values():
            if query.lower() in record.name.value.lower():
                results.append(record)
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
        return results

if __name__ == "__main__":
    # Створюємо адресну книгу
    book = AddressBook()

    # Створюємо запис для John з днем народження
    john_record = Record("John", birthday=date(1990, 1, 1))
    john_record.add_phone("1234567890")
    john_record.add_phone("9876543210")

    den_record = Record("Den", birthday=date(1995, 10, 13))
    den_record.add_phone("0676475005")

    # Додаємо запис до адресної книги
    book.add_record(john_record)
    book.add_record(den_record)


    # Зберігаємо адрес
    book.save_to_disk("address_book.json")

    # Зчитуємо адрес
    new_book = AddressBook()
    new_book.load_from_disk("address_book.json")

    # пошук контакту
    query = "9876543210"
    results = new_book.search(query)

    for result in results:
        print(result, ' result ***--***')
