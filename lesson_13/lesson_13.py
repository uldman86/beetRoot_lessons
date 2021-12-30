# Task 1
# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different. For instance,
# Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk
# method on input parameter.

if __name__ == '__main__':
    class Animal:
        def talk(self):
            pass


    class Dog(Animal):
        def talk(self):
            return 'Woof Woof'


    class Cat(Animal):
        def talk(self):
            return 'Meow meow'


    def talk_animal(animal):
        print(animal.talk())


    c = Cat()
    d = Dog()
    talk_animal(c)
    talk_animal(d)

# Task 2
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books
# list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

if __name__ == '__main__':
    class Author:
        def __init__(self, name_author: str, country: str, birthday: str):
            self.name_author = name_author
            self.country = country
            self.birthday = birthday
            self.books = []

        def __repr__(self):
            return f'The object Author - {self.name_author}'

        def __str__(self):
            return f'Author - {self.name_author}'

        def get_name(self):
            return self.name_author

        def add_book(self, book_name: str):
            self.books.append(book_name)


    class Library:
        def __init__(self, name_library: str):
            self.name_library = name_library
            self.authors = []
            self.books = []

        def __repr__(self):
            return f'The object Library - {self.name_library}'

        def __str__(self):
            return f'Library - {self.name_library}'

        def new_book(self, name: str, year: int,
                     author: Author):  # возвращает экземпляр класса Book и добавляет книгу в список книг для текущей библиотеки.
            book = Book(name, year, author)
            self.books.append(book)
            if book.author not in self.authors:
                self.authors.append(book.author)
            return book

        def group_by_author(self, author: Author):  # возвращает список всех книг, сгруппированных по указанному автору
            list_books = []
            for value in self.books:
                if value.author == author.name_author:
                    list_books.append(value)
            return list_books

        def group_by_year(self, year: int):  # возвращает список всех книг, сгруппированных по указанному году
            list_books = []
            for value in self.books:
                if value.year == year:
                    list_books.append(value)
            return list_books


    class Book:
        books_count = 0

        def __init__(self, name_book: str, year: int, author: Author):
            self.name_book = name_book
            self.year = year
            self.author = author.get_name()
            author.add_book(self.name_book)
            self.__class__.books_count += 1

        def __repr__(self):
            return f'The object Book - {self.name_book}'

        def __str__(self):
            return f'Book - {self.name_book}'


    central_library = Library('Центральная библиотека')
    london = Author('Джек Лондон', 'США', '12.01.1876')
    pushkin = Author('А.С. Пушкин', 'Россия', '06.06.1799')
    central_library.new_book('Мартин Иден', 1909, london)
    central_library.new_book('Белый клык', 1906, london)
    central_library.new_book('Пиковая дама', 1834, pushkin)

# Task 3
#Fraction
# Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
# checking and error handling
# x = Fraction(1/2)
# y = Fraction(1/4)
# x + y == Fraction(3/4)

if __name__ == '__main__':
    class Fraction:
        def __init__(self, val):
            self.val = val

        def check_val(self, other):
            if not isinstance(self, type(other)):
                raise ValueError('Неподходящий тип')

        def __add__(self, other):
            self.check_val(other)
            return self.val + other.val

        def __sub__(self, other):
            self.check_val(other)
            return self.val - other.val

        def __mul__(self, other):
            self.check_val(other)
            return self.val * other.val

        def __truediv__(self, other):
            self.check_val(other)
            if other.val == 0:
                raise ZeroDivisionError('делить на 0 нельзя!')
            return self.val / other.val

        def __eq__(self, other):
            if self.val == other:
                return True
            else:
                return False


    x = Fraction(1 / 2)
    y = Fraction(1 / 4)
    print(x + y == Fraction(1 / 2))
