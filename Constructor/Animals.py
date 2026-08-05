class Cat():

    #default constructor
    def __init__(self):
        pass
        #parameterized constructor
    def __init__(self, name, color): #Constructor with a self, name, color parameters
        self.name = name 
        self.color = color
        print("adding a new cat")

cat1 = Cat("Lucy","brown")
print("First cat\ncat's name:",cat1.name,"\ncat's color:",cat1.color)

cat2 = Cat("Tom","white and blue")
print("\nSecond cat\ncat's name:",cat2.name,"\ncat's color:",cat2.color)