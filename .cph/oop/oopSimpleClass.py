""" oop - abstaction , encapsulation , inheritance , polymorphism """

# class Phone:
#     price = 10000
#     color = 'black'
#     brand ='samsung'

# myPhone = Phone()
# print(myPhone.price)
# print(myPhone.color)
# print(myPhone.brand)

# class Phone:
#     price = 10000
#     color ='blue'
#     brand ='samsung'
#     features = ['camera','bluetooth','wifi']

#     def call (self):
#        print('calling someone')
       
#     def sendSms(self, photo, sms):
#         text = f'sending sms to {photo} and message is {sms}'
#         print(text)
        


# myPhone =Phone()
# print(myPhone.price)
# print(myPhone.color)
# myPhone.call()


# """ Constructor  """
# class Phone:
#     origin ='China'
#     def __init__(self):
#         pass
#     def sendSms(self, phone, sms):
#         text = f'sending sms to {phone} and message is {sms}'


# class Phone:
#     manufactured = 'China'
#     def __init__(self,owner, brand , price):
#         self.owner= owner
#         self.brand=brand
#         self.price=price


 
#     def sendSms(self, phone, sms):
#         text =f'sending sms to {phone} and message is {sms}'
#         print(text)
         
   
# myPhone = Phone('Rohan', 'Samsung', 10000)
# print(myPhone.owner , myPhone.brand,myPhone.price)

# herPhone =Phone('Riya', 'Apple', 50000)
# print(herPhone.owner , herPhone.brand, herPhone.price)


# myPhone.sendSms('23243321', 'Hello Riya')
# herPhone.sendSms('23243322', 'Hello Rohan')


# """ Class Atttributes and instance attributes """
# class Shop:
   
#     def __init__(self, buyer):
#         self.buyer = buyer
#         self.cart = []

#     def addToCart(self, item):
#         self.cart.append(item)


# rohan =Shop('Rohan')
# rohan.addToCart('Laptop')
# rohan.addToCart('Mobile')
# print(rohan.cart)


# rana = Shop('Rana')
# rana.addToCart('noodles')
# rana.addToCart('sondesh')
# print(rana.cart)

# """ Bank System """
# class Bank:
#     def __init__(self, balence):
#        self.balence =balence
#        self.minWithdrawal= 1000
#        self.maxWithdrawal =5000
#     def getBalence(self):
#         return self.balence
#     def deposit(self,amount):
#         if amount>0:
#             self.balence+= amount
#     def withdraw(self, amount):
#         if amount< self.minWithdrawal:
#             return f' Denied'
#         elif amount> self.maxWithdrawal:
#             return f'Denied'
#         else:
#             self.balence -=amount
#             return f'withdrawal successful'


# BracBank =Bank(200000)
# BracBank.deposit(5000)
# BracBank.withdraw(2000)

# balance =BracBank.getBalence()
# print(balance)

# class Shoping:
#     def __init__(self,name):
#         self.name =name
#         self.cart =[]

#     def addToCart(self, item, price, quantity):
#         product = {'item': item, 'price': price, 'quantity': quantity}
#         self.cart.append(product)

#     def checkout(self, amount):
#         total =0
#         for  item in self.cart:
#             total += item['price']* item['quantity']
#             print('total price',total)
#             if amount <total:
#                 return f' {total - amount}'
#             else:
#                 extra = amount - total
#                 return extra
        



# Rohan = Shoping('Rohan')
# Rohan.addToCart('Potato',50,44)
# Rohan.addToCart('Onion', 80, 22)
# Rohan.addToCart('Tomato',60,33)
# print(Rohan.cart)
# Rohan.checkout(2000)


from traitlets import Any


from traitlets import Any


class Student:
    def __init__ (self,name, currentClass,id):
        self.name =name
        self.currentClass = currentClass
        self.id=id

    def __repr__(self)-> str:
        return f'Student with name: {self.name}, class: {self.currentClass} and id: {self.id}'
    
class Teacher:
   def __init__(self, name, subject, id):
         self.name = name
         self.subject = subject
         self.id =id
def __repr__(self) -> str:
       return f'Teacher with name: {self.name}, subject: {self.subject}'

class School:
     def __init__ (self, name)->None:
          self.name= name
          self.teachers = []
          
     def addTeacher(self,name, subject):

          id = len(self,teacher)+101
          teacher =Teacher(name,subject,id)
          self.teachers.append(teacher)

     def enroll(self, name, fee):
          if fee<6500:    
               return 'not enough fee' 
          else:
               id =len(self.students) + 1
               student = Student(name,'C',id )
               self.students.append(student)
               return f'{name} is enrolled with id: {id}, extra money {fee -6500}'

     def __repr__(self) ->str:
          print('Welcome to',self .name)
          print('------Our Teachers---------')
          for teacher in self.teachers:
               print(teacher)
     

          
         


phitron =School('phitron')
phitron.enroll('Rohan', 7000)
phitron.enroll('Riya',6000)
phitron.enroll('Rana',7000)
phitron.enroll('Rohit',5000)

phitron.addTeacher('Shuvo', 'CSS')

phitron.addTeacher('Nehal', 'JSS')





































