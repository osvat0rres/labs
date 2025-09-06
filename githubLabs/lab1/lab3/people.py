

class Person:
    def __init__(self,first_name,last_name):
        self.firstname = first_name
        self.lastname = last_name

# Faculty class
class Faculty(Person):
    def __init__(self,first_name,last_name,department):
        Person.__init__(self,first_name,last_name)
        self.department = department

# Student class
class Student(Person):
    def __init__(self,first_name,last_name):
        Person.__init__(self,first_name,last_name)

    def set_class(self,classyear):
        self.classyear = classyear
    
    def set_major(self,major):
        self.major = major
    
    def set_advisor(self,faculty):
        self.advisor = faculty