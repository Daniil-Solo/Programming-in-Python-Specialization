"""
Задача - реализовать механизм комиссии с помощью дескриптора
для класса Аккаунт. У аккаунта будет атрибут commission.
Именно эту коммиссию и нужно вычитать при присваивании значений в amount.

Тесты
1.
new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
90.0

2.
account = Account(0.1)
account2 = Account(0.1)
account.amount = 100
account2.amount = 200
print(str(account.amount), str(account2.amount))
90.0 180.0
"""


class Value:
    def __init__(self):
        self.__value = None

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        commission = instance.__dict__['commission']
        self.__value = value - value * commission
        instance.__dict__[self.__name] = self.__value

    def __set_name__(self, owner, name):
        self.__name = name


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


account = Account(0.1)
account2 = Account(0.1)
account.amount = 100
account2.amount = 200
print(str(account.amount), str(account2.amount))
