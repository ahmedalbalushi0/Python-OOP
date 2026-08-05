class Student():
    university_name = "UTAS Muscat" #class attribute
    # name = "anonymous" #class attribute
    def __init__(self, name, major):
        self.name = name #object attribute > class attribute
        self.major = major
        print("adding a new student in database")

s1 = Student("Omar","IT")
print("Student name:",s1.name,"major:",s1.major)
print(Student.university_name)