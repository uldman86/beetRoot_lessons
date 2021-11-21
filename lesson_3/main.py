#  Math
# 1
total = 44
rez = total * 80 // 100
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez == 35

# 2
x1 = 1
x2 = 5
y1 = 2
y2 = 4
print('Расстояние между точками', ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

# 3
height = 9
width = 8
depth = 15
diag = (width ** 2 + depth ** 2) ** 0.5  # диагональ
area = diag * height  # Площадь дигонального сечения

area_slate = 3 * 4  # Площадь шифера
amount_slate = area / area_slate  # Кол-во шифера
cost_slate = round(amount_slate + 0.4) * 600  # Сумма с округлением в +1 ед.

print('Листов нужно купить', amount_slate)
print(cost_slate, 'грн за', amount_slate, 'штук шифера')
print('Остаток шифера = ', round(amount_slate + 0.4) - amount_slate, 'штук')

# String
# 1
var1 = 'pyThoN'
# ваш код
var1 = var1.lower().capitalize()
assert var1 == 'Python'
# ваш код
var1 = var1.upper()
assert var1 == 'PYTHON'
# ваш код
var1 = var1.lower()
assert var1 == 'python'
var1 = ' python '
# ваш код
var1 = var1.strip()
assert var1 == 'python'
print(var1)

# 2
name = 'Остап'
print('Привет ' + name)
print(f'Привет {name}')
print('Привет {}'.format(name))
print('Привет %s.' % (name))

# 3
price = 12
weight = 3.4121
rez = 0
# ваш код
rez = 'Итого: ' + str(round(price * weight, 2))
print(rez)
assert rez == 'Итого: 40.95'

# 4
number = 12
username = "ираклий"
access_mask = 54
hour_price = 15.321
rez = 0
# ваш код
rez = str(number).rjust(6, '0') + ' ' + username.capitalize() + ' ' + str(bin(access_mask))[2:] + ' ' + str(
    round(hour_price, 2))
print(rez)
assert rez == '000012 Ираклий 110110 15.32'

# 5
base_str = 'Корова'
rez = 0
# ваш код
rez = chr(ord(base_str[0]) - 8) + base_str[1:4] + chr(ord(base_str[1]) - 1) + base_str[-1]
print(rez)
assert rez == 'Ворона'

# 6
a = 10
b = 55
# ваш код
a, b = b, a
assert a == 55 and b == 10, "Не поменялось. :("