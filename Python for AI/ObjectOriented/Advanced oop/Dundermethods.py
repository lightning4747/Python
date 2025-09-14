class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation for humans (used by print(), str())
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Unambiguous representation for developers
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"
    
    # Define behavior for the len() function
    def __len__(self):
        return self.pages
    
    # Define behavior for the + operator
    def __add__(self, other):
        return self.pages + other.pages

# Using the class
b1 = Book("Python 101", "John Doe", 300)
b2 = Book("OOP Deep Dive", "Jane Doe", 450)

print(str(b1))   # Output: 'Python 101' by John Doe
print(repr(b1))  # Output: Book('Python 101', 'John Doe', 300)
print(len(b1))   # Output: 300
print(b1 + b2)   # Output: 750 (300 + 450)