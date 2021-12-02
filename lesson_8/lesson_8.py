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

# Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as
# the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

#    the call make_operation(‘+’, 7, 7, 2) should return 16
#    the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#    the call make_operation(‘*’, 7, 6) should return 42

if __name__ == '__main__':
    def make_operation(operator, *args):
        nums_list = list(args)

        if operator == '+':
            return sum(nums_list)

        elif operator == '-':
            num = nums_list[0]
            nums_list.remove(num)
            print(nums_list)
            for item in nums_list:
                num = num - item
            return num

        elif operator == '*':
            num = 1
            for item in args:
                num = num * item
            return num

        elif operator == '/':
            num = args[0]**2
            for item in args:
                num = num / item
            return num

    print(make_operation('*', 8, 6))
