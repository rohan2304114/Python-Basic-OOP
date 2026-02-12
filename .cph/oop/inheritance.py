# """ Base class """
        

# from turtle import color


# class Device:
#     def __init__(self, brand, price,color) -> None:
         
#            self.brand=brand
#            self.price=price
#            self.color=color
#     def run(self):
#        return f"Running Device : {self.brand}"

    
# class Laptop(Device):
#        def __init__(self, brand, price, color, memory) ->None:
#             super().__init__(brand, price, color)
#             self.memory=memory
#        def coding(self):
#          return f'Learning python Programing'
       

# class Phone(Device):
#    def __init__(self, brand, price, color, dualsim)->None:
#        super().__init__(brand,price,color)
#        self.dualsim=dualsim
#    def __repr__(self)->str:
#         return f'phone: {self.dualsim}'
              
               

#    def phonecall(self,number,text):
#        return f'Sending sms t {number} with text: {text}'
   

# class Camera(Device):
#      def __init__(self, brand, price, color, pixels)->None:
#           super().__init__(brand,price,color)
#           self.pixels=pixels
#      def changeLens(self):
#         pass


# myPhone= Phone('Samsung', 20000, 'black', True)
# print(myPhone.brand ,myPhone.price, myPhone.color, myPhone.dualsim)


                                           

# class BaseClass:
#     pass
# class DerivedClass(BaseClass):
#     pass                                           

# class Vehicle:
#     def __init__(self, name, price) -> None:
#        self.name=name
#        self.price=price
    
# def move(self):
#     pass

# class Bus(Vehicle):
#     def __init__(self,name,price,seat)->None:
#         super().__init__(name,price)
#         self.seat=seat

# class Truck(Vehicle):
#     def __init__(self,name,price,capacity)->None:
#         super().__init__(name,price)
#         self.capacity=capacity

# class MiniTruck(Truck):
#     def __init__(self,name,price,capacity, size)->None:
#          super().__init__(name,price,capacity)
#          self.size=size
# class AcBus(Bus):
#     def __init__(self,name,price,seat,ac)->None:
#         super().__init__(name,price,seat)
#         self.ac=ac

# Hanif= AcBus('Hanif', 500,50, True)

# print(Hanif.ac)

""" oop - inheritance , polymorphism, encapsulation, abstraction  """




