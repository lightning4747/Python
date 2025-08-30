class Parent:
    def __init__ (self, lname, lage):
        self.name = lname
        self.age = lage
    def printname(self):
        print(f"{self.name} and their age is {self.age}")
class child(Parent):
    def __init__ (self, lname, lage, lgrade):
        super().__init__(lname,lage)
        self.grade = lgrade

    def __str__ (self):
        return f"the student name is {self.name} and their age is {self.age} and their grade is {self.grade}"
class student(child):
    def __init__(self,lname,lage,lgrade,lyear):
        super().__init__(lname,lage,lgrade)
        self.year = lyear

    def __str__(self) -> str:
        return f"{self.name} wt {self.age} et {self.grade} at {self.year}"    

x = child("bruce", 28,"A")
print(x)               

y = student("jin sakai", 234, "A", 4567)
print(y)
y.printname()
            