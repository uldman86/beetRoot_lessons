# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique
# words as keys and the number of occurrences as values.

if __name__ == '__main__':
    input_sentence = input('Введите предложение ').split()  # Получаем ввод и разбиваем на подстроки
    new_dict = {}
    if input_sentence:
        for value in input_sentence:
            new_dict.update({value: input_sentence.count(value)})
        print(new_dict)
    else:
        print('Ошибка ввода')

# Task 2
# Input data:
# stock = {
#    "banana": 6,
#    "apple": 0,
#    "orange": 32,
#    "pear": 15
# }
# prices = {
#    "banana": 4,
#    "apple": 2,
#    "orange": 1.5,
#    "pear": 3
# }
# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.

if __name__ == '__main__':
    stock = {
        'banana': 6,
        'apple': 0,
        'orange': 32,
        'pear': 15
    }
    prices = {
        'banana': 4,
        'apple': 2,
        'orange': 1.5,
        'pear': 3
    }

    def total(stock_fun, prices_fun):  # Функция подсчета суммы товаров
        total_price = {}
        for item in stock:
            total_price.update({item: int(stock_fun.get(item) * prices_fun.get(
                item))})  # Получаем начение по ключу, умножаем кол-во на цену и добавляем в новый словарь
        print(total_price)

    total(stock, prices)


# Task 3

# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

if __name__ == '__main__':
    my_list = [(item, item * item) for item in range(1, 10)]
    print(my_list)
