class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car): #inheritance
    def __init__(self, brand):
        self.brand = brand

class Supra(ToyotaCar):
    def __init__(self,type):
        super().__init__("Toyota")
        self.type = type

car1 = Supra("Petrol")
print(car1.brand)
print(car1.start())
print(car1.color)