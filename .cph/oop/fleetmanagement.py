class Company:
    def __init__ (self, name, address) -> None:
        self.name =name
        self.bus=[]
        self.routes= []
        self.drivers =[]
        self.counter=[]
        self.manager=[]
        self.supervisor=[]

class Driver:
      def __inint__(self,name, lisence, age)-> None:
           self.name=name
           self.lisence=lisence
           self.age=age

class Counter:
     def __init__(self)->None:
          pass
     def purchaseTicket(self,start,destination):
          pass
     
class Passanger:
     pass
class Supervisor:
     pass

redMia= Driver('a',123, 132)
     
