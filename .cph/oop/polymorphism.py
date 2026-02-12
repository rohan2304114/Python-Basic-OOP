""" poly --> many 
    morph -- shape 



"""

# class Animal:
#     def __init__(self,name)->None:
#         self.name=name


#     def makeSound(self):
#         print('Animal Making Some Sound')

# class Cat(Animal):
#     def __init__(self,name)->None:
#         super().__init__(name)
#     def makeSound (self):
#         print('Meow Meow')

# class Dog(Animal):
#      def __init__(self,name)->None:
#       super().__init__(name)
#      def makeSound(self):
#       print('Ghew Ghew')
  
# class Goat(Animal):
#    def __init__(self,name)->None:
#       super().__init__(name)
#    def makeSound(self):
#          print('Beh Beh')


# meow =Cat('Real Don')
# meow.makeSound()

# dogesh=Dog('Real Dogesh')
# dogesh.makeSound()

# messi=Goat('Real Goat')
# messi.makeSound()

# animals =[meow, dogesh, messi]
# for x in animals:
#     x.makeSound()



from math import pi

class Shape:
    def __init__(self,name)->None:
      self.name=name
    
class Rectangle(Shape):
    def __init__(self,name,length, width)->None:
     self.length=length
     self.width=width
     super().__init__(name)
    def getArea(self):
       return self.length*self.width
       

class Circle(Shape):
   def __init__(self,name,radius)->None:
      self.radius=radius
      super().__init__(name)
      def area(self):
         return pi*self.radius*self.radius
      