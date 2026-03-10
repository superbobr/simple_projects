class PhoneBook:
    def __init__(self):
        try:
            with open('phonebook.txt', 'r+', encoding='utf-8') as f:
                data = f.readlines()
                self.contacts = {}
                for contact in data:
                    user_data = contact.strip().split()
                    self.contacts[user_data[0]] = user_data[1]
        except FileNotFoundError:
            self.contacts = {}

    def add(self, user, phone_number):
        self.contacts[user] = phone_number

    def get(self, user):
        print(self.contacts.get(user), 'Контакт не найден')

    def delete(self, user):
        del self.contacts[user]


phonebook = PhoneBook()

for _ in range(4):
    temp = input().split()
    if len(temp) == 2:
        phonebook.delete(temp[1])
    else:
        getattr(phonebook, temp[0])(temp[1], temp[2])

with open('phonebook.txt', 'w+', encoding='utf-8') as file:
    phb_data = dict(sorted(phonebook.contacts.items()))
    for key, value in phb_data.items():
        file.write(f'{key} {value}\n')
    file.seek(0)
    result = file.read()
    print(result)