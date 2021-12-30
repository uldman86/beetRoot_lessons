# Task 1
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.

# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings;
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.

if __name__ == '__main__':
    with open('myfile.txt', 'w') as file:
        file.write('Hello file world!\n')


# Task 2
# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
#    Search by first name
#    Search by last name
#    Search by full name
#    Search by telephone number
#    Search by city or state
#    Delete a record for a given telephone number
#    Update a record for a given telephone number
#    An option to exit the program

# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application, else raise an error.
# After the user exits, all data should be saved to loaded JSON.

if __name__ == '__main__':
    import json

    if __name__ == '__main__':
        class Phonebook:
            def __init__(self):
                self.user_id = 0
                self.phonebook_data = []
                with open('phonebook.json', 'w', encoding='utf8') as self.phonebook_file:
                    json.dump(self.phonebook_data, self.phonebook_file, indent=4)

            def add_new_entries(self, first_name, last_name, telephone, address):  # Добавить новую запись
                self.phonebook_data.append(
                    {'first_name': first_name, 'last_name': last_name, 'telephone': telephone, 'address': address})
                with open('phonebook.json', 'w', encoding='utf8') as self.phonebook_file:
                    json.dump(self.phonebook_data, self.phonebook_file, indent=4)

            def delete_telephone_number(self, telephone):  # Удалить номер телефона
                person = self.search_by_telephone_number(telephone)
                print(person)
                for key in person:
                    self.phonebook_data.pop(key)
                with open('phonebook.json', 'w', encoding='utf8') as self.phonebook_file:
                    json.dump(self.phonebook_data, self.phonebook_file, indent=4)

            def update_telephone_number(self, person: dict, first_name='', last_name='', telephone='',
                                        address=''):  # Изменить запись
                for value in person:
                    if value == 'first_name' and first_name != '':
                        person[value] = first_name
                    elif value == 'last_name' and last_name != '':
                        person[value] = last_name
                    elif value == 'telephone' and telephone != '':
                        person[value] = telephone
                    elif value == 'address' and address != '':
                        person[value] = address
                with open('phonebook.json', 'w', encoding='utf8') as self.phonebook_file:
                    json.dump(self.phonebook_data, self.phonebook_file, indent=4)
                return person

            def search_by_first_name(self, search_name):  # Поиск по имени
                return self.search_essence(search_name, 'first_name')

            def search_by_last_name(self, search_last_name):  # Поиск по фамилии
                return self.search_essence(search_last_name, 'last_name')

            def search_by_full_name(self, search_name, search_last_name):  # Поиск по ФИО
                peoples_find = {}  # Словарь который будет возвращен с найдеными совпадениями
                i = -1  # Используется для формирования ключа в словаре
                people_dict = self.search_essence(search_name, 'first_name')
                for person in people_dict:
                    person_iter = people_dict.get(person)
                    [peoples_find.update({i + 1: person_iter}) for key in person_iter if
                     person_iter.get(key) == search_last_name]
                people_dict = self.search_essence(search_name, 'last_name')
                for person in people_dict:
                    person_iter = people_dict.get(person)
                    [peoples_find.update({i + 1: person_iter}) for key in person_iter if
                     person_iter.get(key) == search_name]
                return peoples_find

            def search_by_telephone_number(self, search_telephone):  # Поиск по номеру
                return self.search_essence(search_telephone, 'telephone')

            def search_essence(self, search_info='', search_key=''):
                data_dict = {}
                for person in self.phonebook_data:
                    for key in person:
                        if search_info == person.get(key) and search_key == key:
                            data_dict.update({self.phonebook_data.index(person): person})
                return data_dict

            def search_by_location(self, search_address):  # Поиск по стране или городу
                return self.search_essence(search_address, 'address')

        phonebook = Phonebook()
        phonebook.add_new_entries('Sergey', 'Uldman', '+380111222333', 'Mariupol')
        phonebook.add_new_entries('Sergey', 'Uldman', '+380111222333', 'Mariupol')
        phonebook.add_new_entries('Alex', 'Ivanov', '+380222333444', 'Minsk')
        phonebook.add_new_entries('Sergey', 'Gromov', '', 'Odessa')

        # print(phonebook.phonebook_data)
        # phonebook.delete_telephone_number('+380222333444')
        # print(phonebook.phonebook_data)
        # print(phonebook.search_by_first_name('Sergey'))
        # print(phonebook.search_by_last_name('Ivanov'))
        # print(phonebook.search_by_telephone_number('+380222333444'))
        # print(phonebook.search_by_location('Odessa'))
        # print(phonebook.search_by_full_name('Sergey', 'Uldman'))
        # print(phonebook.update_telephone_number(phonebook.phonebook_data[0], 'Bobby', 'Egorov'))