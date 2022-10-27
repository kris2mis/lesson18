#ENTITY, LIBRARY, TASK01

# class Account:
#     """class definition of Account"""
#     ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     number = 10
#     coefficient = 5.5
#     s = "this is a string"
#     flag = False
#
#     def tax(balance):
#         return balance * 0.16
#
#
# class SomeClass:
#     ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     number = 10
#     coefficient = 5.5
#     s = "this is a string"
#     flag = False
#
#     def tax(balance):
#         return balance * 0.1


import entity
from entity import Account


class SomeClass:

    def tax(account):
        if isinstance(account, Account):
            return account.balance * 0.1


a = Account()
a.balance = 1000
print(SomeClass.tax(a))
print(SomeClass.tax)
