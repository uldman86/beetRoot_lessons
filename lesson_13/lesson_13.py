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

class Fraction():
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('cal __add__ ')
        if not isinstance(other.val, type(self.val)):
            print('not int or float')
        return Fraction(self.val + other.val)
        #    raise ValueError('error')
        #if isinstance(other, int or float):
            #return 1
        #return Fraction(self.val - other.val)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    #def __truediv__(self, other):
    #    pass

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return self.__str__()


x = Fraction(123)
print(x)
y = Fraction(31)
print(y)
print(type(x))
print(type(y))
x+'x'

#print(f'{x + y} result')
