# Task 1
# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter
# is a valid email string.

if __name__ == '__main__':
    class Account:
        def __init__(self, email: str):
            self.email = Account.validate(email)

        @classmethod
        def validate(cls, email: str):
            lower_char_set = set(range(ord('a'),ord('z')+1))
            if '@' in email:
                email_split_list = email.lower().split('@')
                if len(email_split_list) == 2 and len(email_split_list[0]) > 1 and len(email_split_list[1]) > 1:
                    if email_split_list[0][0].isalnum() and email_split_list[0][-1].isalnum() and email_split_list[1][0].isalnum() and email_split_list[1][-1].isalnum():
                        for value in email_split_list[0]:
                            if value.isdigit() or ord(value) in lower_char_set or value == '.' or value == '_' or value == '-':
                                pass
                            else:
                                raise ValueError('Адрес содержит некоректные символы')
                        for value in email_split_list[1]:
                            if value.isdigit() or ord(value) in lower_char_set or value == '.' or value == '-':
                                pass
                            else:
                                raise ValueError('Адрес содержит некоректные символы')
                        if '.' in email_split_list[1]:
                            suf = email_split_list[1].split('.')
                            if len(suf) > 2 or len(suf[1]) < 2:
                                raise ValueError('Неверный формат домена')
                        else:
                            raise ValueError('Неверный формат домена')
                    else:
                        raise ValueError('Префикс не должен начинатся и заканчиватся на ". _ - "')
                else:
                    raise ValueError('Неверный формат адреса')
                return '@'.join(email_split_list)
            else:
                raise ValueError('Адрес не содержит @')
    account = Account('abc@mail.com')
    print(account.email)


# Task 2
# Task 2
#Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!

if __name__ == '__main__':
    class Boss:

        def __init__(self):
            self._worker_list = []

        @property
        def worker_list(self):
            return self._worker_list

        @worker_list.setter
        def worker_list(self, new_worker):
            if new_worker not in self._worker_list:
                self.worker_list.append(new_worker)

        @worker_list.deleter
        def worker_list(self):
            self.worker_list.clear()


    class Worker:
        @classmethod
        def is_boss(cls, new_boss):
            if isinstance(new_boss, Boss):
                return True
            else:
                return False

        def __init__(self, name, boss: Boss):
            self.boss = boss
            self.name = name

        def new_boss(self, new_boss):
            if Worker.is_boss(new_boss):
                self.boss = new_boss

        def __repr__(self):
            return self.name


    boss1 = Boss()
    worker1 = Worker('a', boss1)
    worker2 = Worker('b', boss1)

    boss1.worker_list = worker2
    boss1.worker_list = worker1
    boss1.worker_list = worker1


