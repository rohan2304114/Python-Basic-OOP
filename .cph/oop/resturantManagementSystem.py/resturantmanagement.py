from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone

class Employee(User):
    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age=age
        self.salary=salary
        self.designation=designation

class Admin(User):
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)

    def addEmployee(self,restaurant,employee):
        restaurant.addEmployee(employee)

    def viewEmployee(self,restaurant):
        restaurant.viewEmployee()

    def addNewItem(self,restaurant,item):
        restaurant.menu.addMenuItem(item)

    def removeItem(self,restaurant,itemName):
        restaurant.menu.removeItem(itemName)

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()

    def addEmployee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} is added")

    def viewEmployee(self):
        print("Employee List")
        for x in self.employees:
            print(x.name, x.email, x.phone, x.address)

class Menu:
    def __init__(self):
        self.items=[]

    def addMenuItem(self,item):
        self.items.append(item)

    def findItem(self,itemName):
        for item in self.items:
            if item.name.lower()==itemName.lower():
                return item
        return None

    def removeItem(self,itemName):
        item=self.findItem(itemName)
        if item:
            self.items.remove(item)
            print("Item Deleted")
        else:
            print("Item not found")

    def showMenu(self):
        print("##### MENU #####")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Customer(User):
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)
        self.cart=Order()

    def viewMenu(self,restaurant):
        restaurant.menu.showMenu()

    def addToCart(self,restaurant,itemName):
        item=restaurant.menu.findItem(itemName)
        if not item:
            print("Item Not Found")
            return

        if item.quantity <= 0:
            print("Item Out of Stock")
            return

        self.cart.addItem(item)
        item.quantity -= 1
        print(f"{item.name} added to cart")

    def viewCart(self):
        print("Name\tPrice\tQuantity")
        for name,(price,qty) in self.cart.items.items():
            print(f"{name}\t{price}\t{qty}")
        print("Total Price:", self.cart.totalPrice())

class Order:
    def __init__(self):
        self.items={}  # {name: (price, quantity)}

    def addItem(self,item):
        if item.name in self.items:
            price,qty=self.items[item.name]
            self.items[item.name]=(price,qty+1)
        else:
            self.items[item.name]=(item.price,1)

    def totalPrice(self):
        return sum(price*qty for price,qty in self.items.values())

    def clear(self):
        self.items={}

# -------- TEST --------
rest=Restaurant("KFC")
admin=Admin("Rohan",1818122744,"rohan@gmail.com","Dhaka")

emp=Employee("Nehal",49545459045,"nehal@gmail.com","Ctg",23,"CEO",377453)
admin.addEmployee(rest,emp)
admin.viewEmployee(rest)

item1=FoodItem("Pizza",120,2)
item2=FoodItem("Burger",100,1)

admin.addNewItem(rest,item1)
admin.addNewItem(rest,item2)

customer=Customer("Alex",9999,"alex@gmail.com","Dhaka")

customer.viewMenu(rest)
customer.addToCart(rest,"Pizza")
customer.addToCart(rest,"Pizza")
customer.addToCart(rest,"Pizza")  # out of stock

customer.viewCart()

itemName = input('Enter Item Name')
itemQuantity= int(input('Enter item Quantity'))
customer.addToCart(rest,itemName,itemQuantity)
customer.viewCart()



