# Task 1
# School
# Make a class structure in python representing people at school. Make a base class called Person,
# a class called Student, and another one called Teacher. Try to find as many methods and attributes as you can
# which belong to different classes, and keep in mind which are common and which are not. For example,
# the name should be a Person attribute, while salary should only be available to the teacher.

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
# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
#     square_nums (takes a list of integers and returns the list of squares)
#     remove_positives (takes a list of integers and returns it without positive numbers
#     filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

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


# Task 3
# Product Store
# Write a class Product that has three attributes:
    #type
    #name
    #price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
if __name__ == '__main__':
    class Product:
        def __init__(self, type_product, name, coast):
            self.name = name
            self.type_product = type_product
            self.coast = coast
            print(f'Создание товара {self.name}, с базовой ценой {self.coast}')


    class ProductStore:
        id_product = 100000 - 1
        data = {}
        cash_register = 0

        def __init__(self, name_store):
            self.name_store = name_store
            print(f'Создание магазина {self.name_store}')

        def generate_identifier(self):  # генерируем id для товара
            self.id_product += 1
            return self.id_product

        def plus_percent(self, start_coast: int, percent: int):  # расчитываем стоимость с %
            return (start_coast * percent) / 100 + start_coast

        def add(self, product: Product, amount: int,
                percent=30):  # добавляет кол-во товаров с предустановленной ценовой надбавкой (30%)
            coast = self.plus_percent(product.coast, percent)
            self.data.update({self.generate_identifier(): [product, amount, coast]})
            print(f'Добавляем товар "{product.name}, в количестве {amount}, стоимость: {coast} цена + {percent}%')

        def set_discount(self, identifier,
                         percent: int):  # добавляет скидку на все товары, указанные в id скидка должна быть указана в %
            for item in self.data.keys():
                if item == identifier:
                    self.data.get(item)[2] -= self.data.get(item)[2] * percent / 100
                    print(
                        f'Применена скидка в {percent}% для товара "{self.data.get(item)[0].name}" теперь цена - {self.data.get(identifier)[2]}')

        def product_availability(self, product_name, amount):  # Проверка на наличие и количество
            product = self.get_product_info(product_name)  # проверяем наличие
            if product:  # проверяем количество
                if 0 < product[1] >= amount:
                    return product[2]
                else:
                    print(f'Наличие товаров в магазине ({product[1]}) ниже вашего запроса ({amount})')
            return False

        def cash_register_update(self, product_coast, amount):  # Добавление денег в кассу
            self.cash_register += product_coast * amount
            return True

        def remove_amount_product(self, product_id, amount):  # Списываем товар со склада
            self.data.get(product_id)[1] -= amount
            return True

        def sell_product(self, product_name,
                         amount):  # удаляет определенное количество товаров из магазина, если доступно, в противном случае вызывает ошибку. Он также увеличивает доход, если метод sell_product завершается успешно.
            product_id = self.product_availability(product_name,
                                                   amount)  # проверяем наличие товара и его кол-во, если есть возвращает id продукта
            if product_id:
                self.remove_amount_product(product_id, amount)  # списываем кол-вот товара со склада
                print(
                    f'Списание товара "{self.data.get(product_id)[0].name}" со склада в количестве - {amount}, остаток - {self.data.get(product_id)[1]}')
                print(f'В кассе до сделки {self.cash_register}')
                self.cash_register_update(self.data.get(product_id)[2],
                                          amount)  # заносим деньги в кассу и возвращаем True
                print(f'В кассе после сделки {self.cash_register}')

        def get_income(self):  # возвращает сумму многих заработанных экземпляром ProductStore.
            return self.cash_register

        def get_all_products(self):  # возвращает информацию обо всех доступных в магазине товарах.
            all_product = 'Артикул:     Наименование товара:\n'
            for key, value in self.data.items():
                all_product += ''.join(f'{key}       {value[0].name}    шт - {value[1]},  цена - {value[2]}\n')
            return all_product

        def get_product_info(self,
                             product):  # возвращает кортеж с названием продукта и количеством товаров в магазине и его id.
            try:
                product_tuple = tuple(
                    (value[0].name, value[1], key) for key, value in self.data.items() if value[0].name == product)
                print(product_tuple[0])
                return product_tuple[0]
            except IndexError:
                print('Такого продукта в базе не существует!')
                return False


    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore('New Shop')
    s.add(p, 10)
    s.add(p2, 300)
    s.sell_product('Ramen', 10)
    assert s.get_product_info('Ramen') == ('Ramen', 290, 100001)  # Добавил в проверку product_id,
    # так как на нем завязана логика продажи товара


# Task 4
# Custom exception
# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named` logs.txt`. Tips: Use __init__ method
# to extend functionality for saving messages to file

if __name__ == '__main__':
    class CustomException(Exception):
        def __init__(self, msg):
            with open('msg_error.txt', 'a', encoding='utf-8') as msg_error:
                msg_error.write(msg)


    def calculations_percent(persent, coast):
        if persent <= 0:
            raise CustomException('CustomException: Передваваемы процент или стоимость не могут быть '
                                  'меньше или равняться нулю\n')
        return persent * coast


    print(calculations_percent(2, 5))
    print(calculations_percent(0, 5))