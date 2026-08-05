class Student():
    university_name = "UTAS Muscat" #class attribute
    
    def __init__(self, name, major):
        self.name = name #object attribute > class attribute
        self.major = major
        print("adding a new student in database")

    def welcome(self):
        print("welcome",self.name,"from",self.university_name)

s1 = Student("Omar","IT")
s1.welcome()