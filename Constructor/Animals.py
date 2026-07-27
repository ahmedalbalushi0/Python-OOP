class Cat():
    name = "Tommy"
    color = "While and gray"
    def __init__(self): #Constructor with a self parameter
        print(self) #the default parameter of the constructor 
        print("My first cat")

cat1 = Cat()
print("cat's name: ",cat1.name,"\ncat's color: ",cat1.color)