class Dog :
    year = 2025
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def firstyear(self) -> None:
        return f"{self.name} is brought on {self.year}"
    
    def __str__(self):
        return f"{self.name} is {self.color} colored dog"

d = Dog("jimmy", "Red")

print(d.firstyear())

        
        