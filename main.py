from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        value = str(value)
        if not value.isdigit():
            raise ValueError("Phone must contain only digits")
        if len(value) != 10:
            raise ValueError("Phone must be 10 digits")
        super().__init__(value)
            
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, value):
        phone = Phone(value)
        self.phones.append(phone)
        
    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item
    
    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone is not None:
            self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        new_valid_phone = Phone(new_phone)
        if found_phone:
            found_phone.value = new_valid_phone.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass

