#ACCOUNT, MAIN1, BANK



class Account:
    # constructor
    def __init__(self, id, balance, name, cofficient=0.01):
        self.id = id
        self.balance = balance
        self.name = name
        self.cofficient = cofficient


    # destructor (он 1 в отличие от конструктора)
    # def __del__(self):
    #     pass

    def get_info(self):
        return (f"{self.id}: "
                f"balance = {self.balance}"
                f"name = {self.name}"
                f"cofficient = {self.cofficient}")
