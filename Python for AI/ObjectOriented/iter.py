class myclass:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Mynumber :
    def __iter__(self):
        return self.age
    def __next__(self):
        if self.a<21:
            x = self.a
            self.a +=1
            return x
        else :
            print("nah uh")
            raise StopIteration
        

p1 = myclass("bruce", 28)   
print(p1)    
p1.name = "jin"
print(p1)            
n = Mynumber()
i = iter(n)
for a in i :
    print(a, sep =",")
