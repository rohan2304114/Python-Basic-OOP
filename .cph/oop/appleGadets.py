class Laptop:
    def __init__(self,brand,model,price,color,memory)->None:
        self.brand=brand
        self.model=model
        self.price=price
        self.color=color
        self.memory=memory
    
    def run(self):
        return f'Running  Laptop :{self.brand}'
    def coding(self):
        return f'learning python and practicing'  

class Phone:
    def __init__(self,brand,price,color,dualsim)->None:
        self.brand=brand
        self.price=price
        self.color=color
        self.dualsim=dualsim

    def run(self):
        return f'phoen is running'

    def phonecall(self,number, text):
        return f'Sending sms to {number} with {text}' 

class Camera:
    def __init__(self, brand, price, color, pixels)->None:
        self.brand=brand
        self.price=price
        self.color=color
        self.pixels=pixels

