
from abc import ABC, abstractmethod 
class Animal(ABC) :
    @abstractmethod
    def eat(self):
        print("I eat food ")
    def move(self):
        pass 
class Monkey(Animal):
    def __init__(self,name)->None:
        self.category='Monkey'
        self.name=name
        super().__init__()
    def eat(self):
        print('Hey nana i am eating bananna')
ruru=Monkey('Lucky')        
ruru.eat()
 