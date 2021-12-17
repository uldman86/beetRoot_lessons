# Task 1
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.

# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings;
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.

if __name__ == '__main__':
    file = open('myfile.txt', 'w')
    file.write('Hello file world!\n')
    file.close()


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

import json

if __name__ == '__main__':
    def create_new_phonebook():  # Создать телефонную книгу
        phonebook = {'name': '', 'age': ''}
        with open('phonebook.json', 'w', encoding='utf8') as write_file:
            json.dump(phonebook, write_file)


    create_new_phonebook()
    menu = ['Выход', 'Добавить новую запись', 'Удалить запись', 'Изменить запись', 'Поиск контакта']




    def valid_user_input():
        if input() == str(range(10)):
            print(100500)
        #user_input = input('Выберите меню')

    valid_user_input()

    def exit_program():  # Выход из программы
        pass


    def add_new_entries():  # Добавить новую запись
        pass


    def delete_telephone_number():  # Удалить номер телефона
        pass


    def update_telephone_number():  # Изменить запись
        pass


    def search_by_first_name():  # Поиск по имени
        pass


    def search_by_last_name():  # Поиск по фамилии
        pass


    def search_by_full_name():  # Поиск по ФИО
        pass


    def search_by_telephone_number():  # Поиск по номеру
        pass


    def search_by_location():  # Поиск по стране или городу
        pass

#    data = {'name': 'Sergey', 'age': 17}
