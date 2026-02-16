from abc import ABC

#Parent class
class User (ABC):
    def __init__(self, name, phone, email ,address):
        self.name=name
        self.phone=phone 
        self.email=email 
        self.address=address
    
# Employee Class 
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation, salary):
        super().__init__(name,phone,email,address)
        self.age=age
        self.designation=designation
        self.salary=salary

#Admin Class
class Admin(User):
    def __init__(self,name,phone, email,address):
        super().__init__(name,phone,email,address)

    def addEmployee(self,restaurant,employee):
        restaurant.addEmployee(employee)
    def viewEmployee(self,restaurant):
        restaurant.viewEmployee()


#Restaurant Class
class Restaurant:
    def __init__(self,name):
        self.employees=[]
        self.name=name

    def addEmployee(self , employee):
        self.employees.append(employee)
        print(f"{employee.name} is adder")
    
    def viewEmployee(self):
        print("--Employee List--")
        for x in self.employees:
            print(f"{x.name} || {x.phone} ||{x.email} || {x.address}")

class Menu:
    def __init__(self):
        self.items=[]
    def addItemInMenu(self,item):
        self.items.append(item)
    def findItem(self,itemName):
        for x in self.items:
            if x.name.lower()==itemName.lower():
                return x
            else:
                return None
    def removeItem(self,itemName):
        item=self.findItem(itemName)
        if item:
            self.items.remove(item)
            print(f"Item is Deleted")
        else:
            print("Item is not present")
    def showMenu(self):
        print("Name || Price || Quantity")
        for x in self.items:
            print(f"{x.name} || {x.price} ||{x.quantity}")

            
            
class FoodItem:
    def __init__(self, name, price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Order:
    def __init(self):
        self.items={}
    def addItem(self,item,qty):
        if item.name.lower()==self.items.lower():
            self.items[item.name][1] +=qty
        else:
            self.items[item.name]=[item.price,qty]
    
    def totalPrice(self):
        total=0;
        for price ,qty in self.items.values():
            total+=price*qty            
                   

class Customer:
     def __inti__ (self,name, phone,email,address):
         super().__init__(name,phone,email,address)
     def ViewMenu(self,restaurant):
         restaurant.menu.showMenu()
     def addToCart(self,restaurant,itemName,quantity):
         item= restaurant.menu.findItem(itemName)
         
         if not item:
             print("item Not fond")
             return
         if item.quantity< quantity:
             print("Not enough stock")
             return 
         self.cart.addItem(item,quantity)
         item.quantity-=quantity
         print(f"{itemName} is added to cart")

         def viewCart(self):
             print("-------CART------")
             print("Name || price || Quantity")
             for name,(price,qty) in self.cart.items.items():
            print{f"{name}  {price} {qty}"}


     
    
    


    

KFC=Restaurant("KFC")
masud=Admin("Masud Rana"," 046718239","masud@gmail.com","CTG")

nehal=Employee("Nehal ahmed","0123456789","nehal@gmal.com","Chandpur",23,"Chef",12000)
rohan=Employee('Rohan','138769424657',"rohan@gmail.com","Cumilla",23,"Co Chef",10000)
masud.addEmployee(KFC,nehal)
masud.addEmployee(KFC,rohan)
masud.viewEmployee(KFC)
print("Ur code is done now u can do it ")
        


