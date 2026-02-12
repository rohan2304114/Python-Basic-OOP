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
        if item:
            self.cart.addItem(item)
        else:
            print("Item Not Found")

    def viewCart(self):
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print("Total Price:", self.cart.totalPrice())

class Order:
    def __init__(self):
        self.items={}

    def addItem(self,item):
        if item in self.items:
            self.items[item]+=1
        else:
            self.items[item]=1

    def totalPrice(self):
        return sum(item.price*qty for item,qty in self.items.items())

    def clear(self):
        self.items={}

# -------- TEST --------
rest=Restaurant("KFC")
admin=Admin("Rohan",1818122744,"rohan@gmail.com","Dhaka")

emp=Employee("Nehal",49545459045,"nehal@gmail.com","Ctg",23,"CEO",377453)
admin.addEmployee(rest,emp)
admin.viewEmployee(rest)

item1=FoodItem("Pizza",120,10)
item2=FoodItem("Burger",120,40)
admin.addNewItem(rest,item1)
admin.addNewItem(rest,item2)

rest.menu.showMenu()
