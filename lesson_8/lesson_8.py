# Task 1
# A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.
if __name__ == '__main__':
    def favorite_movie(input_string):
        print(f'My favorite movie is named {input_string}')


    favorite_movie(input('Введите название вашего любимого фильма '))

# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.
if __name__ == '__main__':
    countrys_dict = {}


    def make_country(name_input, capital_input):
        countrys_dict.update({'name': name_input, 'capital': capital_input})
        print(countrys_dict)


    user_input = [input('Введите страну '), input('Введите введите столицу ')]
    make_country(user_input[0], user_input[1])


# Задачку №3 не успел доделать, завтра доделаю)