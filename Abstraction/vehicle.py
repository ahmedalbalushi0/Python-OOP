class Car:

    def __init__(self):
        self.acc = False #accelerator
        self.brk = False #break
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()