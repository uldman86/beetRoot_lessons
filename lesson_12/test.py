import random


class Product:
    def __init__(self, name, type_product, coast):
        self.name = name
        self.type_product = type_product
        self.coast = coast


class ProductStore:
    id_product = 100000 - 1
    data = {}
    cash_register = 0

    def __init__(self, name_store):
        self.name_store = name_store

    def generate_identifier(self):  # генерируем id для товара
        self.id_product += 1
        return self.id_product

    def add(self, product, amount, extra_charge=1.3):  # добавляет кол-во товаров с ценовой надбавкой (30%)
        coast = int(product.coast * extra_charge)
        self.data.update({self.generate_identifier(): [product, amount, coast]})

    def set_discount(self, identifier, percent,
                     identifier_type='name'):  # добавляет скидку на все товары, указанные в id скидка должна быть указана в %
        pass

    def product_availability(self, product_name, amount):    # Проверка на наличие и количество
        product = self.get_product_info(product_name)
        if product:
            if 0 < product[1] >= amount:
                return product[2]
            else:
                print(f'Наличие товаров в магазине ({product[1]}) ниже вашего запроса ({amount})')
        return False

    def sell_product(self, product_name, amount):  # удаляет определенное количество товаров из магазина, если доступно, в противном случае вызывает ошибку. Он также увеличивает доход, если метод sell_product завершается успешно.
        product_id = self.product_availability(product_name, amount)
        self.data.get(product_id)[1] -= amount
        self.cash_register += self.data.get(product_id)[2]
        print(self.data.get(product_id))
        print(self.cash_register)


    def get_income(self):  # возвращает сумму многих заработанных экземпляром ProductStore.
        pass

    def get_all_products(self):  # возвращает информацию обо всех доступных в магазине товарах.
        all_product = 'Артикул:     Наименование товара:\n'
        for key, value in self.data.items():
            all_product += ''.join(f'{key}       {value[0].name}    шт - {value[1]},  цена - {value[2]}\n')
        return all_product

    def get_product_info(self, product):  # возвращает кортеж с названием продукта и количеством товаров в магазине.
        try:
            product_tuple = tuple(
                (value[0].name, value[1], key) for key, value in self.data.items() if value[0].name == product)
            return product_tuple[0]
        except IndexError:
            print('Такого продукта в базе не существует!')
            return False


samsung_qe55 = Product('Samsung QE55Q60AAUXUA', 'TV', 25000)
nokia_3310 = Product('Nokia 3310', 'Telephone', 3500)

foxtrot = ProductStore('Foxtrot')

foxtrot.add(samsung_qe55, 13)
foxtrot.add(nokia_3310, 5)

foxtrot.sell_product('Samsung QE55Q60AAUXUA', 12)
