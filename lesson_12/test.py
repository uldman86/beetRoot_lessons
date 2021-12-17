class Product:
    def __init__(self, name, type_product, coast):
        self.name = name
        self.type_product = type_product
        self.coast = coast


class ProductStore(Product):
    stock = {}


    def add(self, product, amount):    # добавляет кол-во товаров с ценовой надбавкой (30%)
        self.stock.update()

    def set_discount(self, identifier, percent, identifier_type= 'name'):    # добавляет скидку на все товары, указанные в id скидка должна быть указана в %
        pass

    def sell_product(self, product_name, amount):  # удаляет определенное количество товаров из магазина, если доступно, в противном случае вызывает ошибку. Он также увеличивает доход, если метод sell_product завершается успешно.
        pass

    def get_income(self):   # возвращает сумму многих заработанных экземпляром ProductStore.
        pass

    def get_all_products(self):     # возвращает информацию обо всех доступных в магазине товарах.
        pass

    def get_product_info(self):     # возвращает кортеж с названием продукта и количеством товаров в магазине.
        pass

