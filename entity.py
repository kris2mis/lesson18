#ENTITY, LIBRARY, TASK01

class Account:

    def tax(account):
        return account.balance * 0.1


#вызов функции
a = Account() # экземпляр класса
a.balance = 1000
print(Account.tax(a))
print(Account.tax) # описание

#вызов метода
print(a.tax())
print(a.tax)  # описание



# Account.name = "123456789"
#
# a1 = Account()
# a1.name = "qwerty"
# a2 = Account()
# a3 = Account()
# a4 = Account()
# print(a1.name)
# print(a2.name)
# print(a3.name)
# print(a4.name)
