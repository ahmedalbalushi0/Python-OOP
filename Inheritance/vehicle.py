class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car): #inheritance
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Supra")
car2 = ToyotaCar("4Runner")
print(car1.name)
print(car1.start())
print(car1.color)