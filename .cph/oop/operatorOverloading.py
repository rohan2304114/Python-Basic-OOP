# class Person:
#     def __init__(self,name,age,height,weight)->None:
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#     def eat(self):
#         print('if i win i will eat')
#     def exercise(self):
#         raise NotImplementedError

# class Cricketer(Person):
#     def __init__ (self, name, age, height,weight,team)->None:
#         self.team=team
#         super().__init__(name,age,height,weight)
#     def eat(self):
#         print('I will Not i have to do it')
#     def exercise(self):
#      print('Gym jabo')
#      def __add__(self,other):
#         return self.age+other.age
         

# sakib =Cricketer('Sakib',39,68,91,'BD')
# rakib =Cricketer('Rakib', 50, 49,75,'BD')
# # sakib.eat()
# # sakib.exercise()

# """ Method - overriding 
#     operataor - overloading
#  """

# print(45+50)
# print('sakib + safwan')
# print([1,2,3,4,5]+[6,2,4,5,2])
# print(sakib+rakib)




# class Shopping:
#     cart=[]
#     origin ='China'
#     def __init__(self,name,location)->None:
#         self.name=name
#         self.location='rayans'
#     def purchase(self,item, price, amount):
#         remaining= amount -price
#         print(f'buying:{item} \nfor price  :{price} \nand reaminig: {remaining}')

# bashundara=Shopping("Rohan","Not a location")

# bashundara.purchase('a',2,4)

# class User:
#     def __init__(self, name, age, money):
#         self._name=name
#         self._age=age
#         self.__money=money
#     @property
#     def age(self):
#         return self._age
#     @property
#     def salary(self):
#         return self.__money
    
# rohan=User('Rohan',10,40000)
# print(rohan.age)
# print(rohan.salary)

# def double_decker():
#     print('start the double docker')
#     def inner_fun():
#         print('inside the inner ')
#     return inner_fun

# print(double_decker()())

# class Animal:
#     pass
# class Dog(Animal):
#     pass
# class Tiger(Animal):
#     pass
# class Furniture:
#     pass

# class Chair(Furniture):
#     pass
# class Table(Furniture):
#     pass


# class Engine:
#     def __init__(self)->None:
#         pass 
#     def start(self):
#         return 'Engine start'
# class Driver:
#     def __init__(self)->None:
#         pass
    
# class Car:
#     def __init__(self) ->None:
#         self.engine=Engine()
#         self.driver=Driver()


#     def start()


# class Singleton:
#     _instance = None
#     def __init__(self)->None:
#         if Singleton._instance is None:
#             Singleton._instance =self
#         else:
#             raise Exception('This is sigleton. Already have an instance, use that one by calling get instance method')
        
#     @staticmethod 
#     def get_instance():
#      if Singleton._instance is None:
#         Singleton()
#      return Singleton.__instance 
    
#     first = Singleton.get_instance()
#     second= Singleton.get_instance()
#  print(first)
#  print(second)
#  print(third)
        


    







