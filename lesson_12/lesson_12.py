# Task 1

if __name__ == '__main__':
    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def go_to_school(self):
            print("Идти в школу")


    class Student(Person):
        def __init__(self, visit, progress, name, age):
            super().__init__(name, age)
            self.visit = visit
            self.progress = progress

        def do_homework(self):
            print('Делать домашнее задание')


    class Teacher(Person):
        def __init__(self, skills, salary, name, age):
            super().__init__(name, age)
            self.skills = skills
            self.salary = salary

        def teach(self):
            print('преподавать предмет')


    man_1 = Student(True, 'A+', 'Ivan', 15)
    man_2 = Teacher('Hight', 15000, 'Peter', 30)
    print(man_1.name, man_1.age, man_1.progress, man_1.visit)
    man_1.do_homework()
    man_1.go_to_school()
    print(man_2.name, man_2.age, man_2.skills, man_2.salary)
    man_2.go_to_school()
    man_2.teach()


# Task 2

if __name__ == '__main__':
    class Mathematician:

        def square_nums(self, number_list):
            result = [value ** 2 for value in number_list if type(value) == int]
            return result

        def remove_positives(self, number_list):
            result = [value for value in number_list if type(value) == int and value < 0]
            return result

        def filter_leaps(self, number_list):
            result = [value for value in number_list if type(value) == int and value % 4 == 0]
            return result

    m = Mathematician()
    assert m.square_nums([7,11,5,4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

