class Student:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        pass

class Engineer(Student):
    def __init__(self,_name,_age,_courses):
        super().__init__(_name,_age)
        self.courses = _courses
    
    def displayEngineer(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCourses: {self.courses}")

class Doctor(Student):
    def __init__(self,_name,_age,_hospital):
        super().__init__(_name,_age)
        self.hospital = _hospital
    
    def displayDoctor(self):
        print(f"Name: {self.name}\nAge: {self.age}\nHospital: {self.hospital}")

if __name__=="__main__":
    student1 = Student("Mike Diamond", "42")
    student1.display()
    student2 = Engineer("Adam Horowitz", "43", "Foundations in Programming")
    student2.displayEngineer()
    student3 = Doctor("Adam Yaught", "44", "Massachusetts General")
    student3.displayDoctor()

