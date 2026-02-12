class Bank:
    def __init__(self, holderName, balance)-> None:
        self.holderName=holderName #public attribute
        self.__balance=balance #private attribute
    def deposit(self,amount):
        self.__balance += amount
        return self.__balance
rohan = Bank('Rohan', 2000)
print(rohan.holderName, rohan.__balance)  # This will raise an AttributeError because __balance is private