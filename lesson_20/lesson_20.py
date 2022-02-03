# Task 1
# Make a directory with 2 modules; make a function in one of them; then import this function in the other
# module and use that in your script of choice.

# from modul_2 import user
#
# if __name__ == '__main__':
#     user_info = user('Sergey', 28, '+380999111222')
#     print(user_info)

# Task 2
# The “sys.path” list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
# Run some interactive tests to find it out.

# Так как sys.path является списком, его можно изменять изнутри Python. Так же изменяя  sys.path можно добавлять пути
# для импорта необходимых модулей

if __name__ == '__main__':
    #from my_modul import my_func # функция из модуля my_modul.py не находится в области видимости

    import sys
    sys.path.append('C:\example')  # добавляем путь нашего модуля в sys.path)
    import my_modul
    my_modul.my_func()
