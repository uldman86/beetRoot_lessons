# Task 1
#Make a program that has some sentence (a string) on input and returns a dict containing all unique
# words as keys and the number of occurrences as values.

if __name__ == '__main__':
    input_sentence = input('Введите предложение ').split() # Получаем ввод и разбиваем на подстроки
    new_dict = {}
    if input_sentence:
        for value in input_sentence:
            new_dict.update({value: input_sentence.count(value)})
        print(new_dict)
    else:
        print('Ошибка ввода')






