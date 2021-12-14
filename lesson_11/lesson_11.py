# Task 1
# A Person class
# Make a class called Person. Make the __init__() method take firstname, lastname,
# and age as parameters and add them as attributes. Make another method called talk() which makes
# prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

if __name__ == '__main__':
    class Person:
        def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

        def talk(self):
            print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old")


    man_1 = Person('Sergey', 'Kruychko', 28)
    man_1.talk()

# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

if __name__ == '__main__':
    class Dog:
        age_factor = 7

        def __init__(self, age):
            self.age = age

        def human_age(self):
            return self.age * self.age_factor


    dog = Dog(3)
    print(dog.human_age())

# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

if __name__ == '__main__':
    class TVController:
        list_channel = {1: 'BBC', 2: 'Discovery', 3: 'TV1000', 4: 'Animal planet'}
        current_channel = list_channel[1]

        def turn_channel(self, channel):
            self.current_channel = self.list_channel[channel]
            print(self.current_channel)

        def first_channel(self):
            self.turn_channel(1)

        def last_channel(self):
            self.turn_channel(len(self.list_channel))

        def next_channel(self):
            for key, value in self.list_channel.items():
                if value == self.current_channel:
                    if key < len(self.list_channel):
                        self.turn_channel(key + 1)
                    else:
                        self.turn_channel(1)
                    break

        def previos_channel(self):
            for key, value in self.list_channel.items():
                if value == self.current_channel:
                    if key > 1:
                        self.turn_channel(key - 1)
                    else:
                        self.turn_channel(len(self.list_channel))
                    break

        def current_channel_now(self):
            return self.current_channel


    print("""
    Menu:
    цифры    - выбор канала
    first    - первый канал в списке
    last     - последний канал в списке
    next     - следующий канал
    previos  - предыдущий канал
    current  - текущий канал
    exit     - выход
    """)

    controller = TVController()

    while True:
        user_type = input('Выберите канал ')
        if user_type.isdigit() and 0 < int(user_type) <= len(controller.list_channel):
            controller.turn_channel(int(user_type))
        elif user_type == 'first':
            controller.first_channel()
        elif user_type == 'last':
            controller.last_channel()
        elif user_type == 'next':
            controller.next_channel()
        elif user_type == 'previos':
            controller.previos_channel()
        elif user_type == 'current':
            print(controller.current_channel_now())
        elif user_type == 'exit':
            break

