class Student:
    """
    Creates an instance of the Student Class. Takes in a name and age
    with a method to display the studen's name and age.

    Parameters: 
        name(string): name of student.
        age(string): age of student

    Returns:
        An instance of the Student Class. 
    """
    def __init__(self, _name, _age):
        '''
        Initializes the Student class

        Parameters:
            name(String):The name of the student.
            age(String):The age of the student.

        Sets the properties for name and age. 
        '''
        self.name = _name
        self.age = _age

    def display(self):
        """
        Prints the display output for the name and age of the Student.
        """
        print(f"Name: {self.name}\nAge: {self.age}")
        pass


class Engineer(Student):
    '''
    Creates the instance of the Engineer class from a name, age, and courses parameter.
    Engineer is a sub class of Student.

    Parameters:
        name(string): name of engineer.
        age(string): age of engineer
        courses(string): course of engineer

    Returns:
        An instance of the Engineer class  

    '''
    def __init__(self, _name, _age, _courses):
        '''
        Initializes the Engineer class

        Parameters:
            name(String):The name of the Engineer.
            age(String):The age of the Engineer.
            course(String):The age of the Engineer.

        Sets the properties for name, age, and courses. 
        '''
        super().__init__(_name, _age)
        self.courses = _courses

    def displayEngineer(self):
        """
        Prints the display output for the name, age, and courses of the Engineer.
        """
        print(f"Name: {self.name}\nAge: {self.age}\nCourses: {self.courses}")


class Doctor(Student):
    '''
    Creates the instance of the Doctor class from a name, age, and hospital parameter.
    Doctor is a sub class of Student.

    Parameters:
        name(string): name of doctor.
        age(string): age of doctor
        hospital(string): hostpital of doctor

    Returns:
        An instance of the Doctor class  

    '''
    def __init__(self, _name, _age, _hospital):
        '''
        Initializes the Doctor class

        Parameters:
            name(String):The name of the Doctor.
            age(String):The age of the Doctor.
            hospital(String):The age of the Doctor.

        Sets the properties for name, age, and hospital. 
        '''
        super().__init__(_name, _age)
        self.hospital = _hospital

    def displayDoctor(self):
        """
        Prints the display output for the name, age and hospital of the Doctor.
        """
        print(f"Name: {self.name}\nAge: {self.age}\nHospital: {self.hospital}")


if __name__ == "__main__":
    student1 = Student("Mike Diamond", "42")
    student1.display()
    student2 = Engineer("Adam Horowitz", "43", "Foundations in Programming")
    student2.displayEngineer()
    student3 = Doctor("Adam Yaught", "44", "Massachusetts General")
    student3.displayDoctor()
