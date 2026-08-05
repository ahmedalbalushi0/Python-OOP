class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Welcome",self.name)

    def Average(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("Hi",self.name,"your average score is",sum/3)    
        
s1 = Student("Mohammed", [89,91,78])
print("\nName:",s1.name,"\nMarks:",s1.marks)
s1.Average()