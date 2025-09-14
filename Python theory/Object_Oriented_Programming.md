# Object-Oriented Programming (OOP) in Python - Comprehensive Study Guide

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [Classes and Objects](#classes-and-objects)
3. [The __init__() Method](#the-init-method)
4. [Instance Methods](#instance-methods)
5. [Class and Static Methods](#class-and-static-methods)
6. [Inheritance](#inheritance)
7. [Encapsulation](#encapsulation)
8. [Polymorphism](#polymorphism)
9. [Abstraction](#abstraction)
10. [Special Methods (Magic/Dunder Methods)](#special-methods)
11. [Property Decorators](#property-decorators)
12. [Best Practices](#best-practices)

---

## Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

### Key Principles of OOP:
1. **Encapsulation**: Bundling of data with the methods that operate on that data
2. **Inheritance**: Mechanism to create a new class using properties of an existing class
3. **Polymorphism**: Ability to use a common interface for different data types
4. **Abstraction**: Hiding complex implementation details and showing only essential features

OOP helps in creating reusable code, organizing complex programs, and modeling real-world scenarios more effectively.

---

## Classes and Objects

### Class
A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that the objects will have.

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
```

### Object
An object is an instance of a class. When a class is defined, no memory is allocated until an object is created.

```python
# Creating objects (instances) of the Dog class
my_dog = Dog("Rex", 5)
your_dog = Dog("Buddy", 3)

print(my_dog.name)  # Output: Rex
print(your_dog.age) # Output: 3
print(my_dog.species) # Output: Canis familiaris
```

### Key Points:
- Classes are defined using the `class` keyword
- Class names should use CamelCase convention
- The `self` parameter refers to the current instance of the class
- Attributes can be class-level (shared by all instances) or instance-level (specific to each instance)

---

## The __init__() Method

The `__init__()` method is a special method that is automatically called when a new object is created. It's used to initialize the object's attributes.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value
        
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an instance
my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_descriptive_name())  # Output: 2022 Toyota Camry
```

### Key Points:
- `__init__()` is the constructor method in Python
- It must have at least one parameter, conventionally named `self`
- You can set default values for attributes in the `__init__()` method
- It's called automatically when creating a new instance

---

## Instance Methods

Instance methods are functions defined inside a class that operate on instances of that class. They always take `self` as the first parameter.

```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    # Instance method
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    # Instance method
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    # Instance method
    def get_balance(self):
        return f"Balance: ${self.balance}"

# Using instance methods
account = BankAccount("John Doe", 1000)
print(account.deposit(500))  # Output: Deposited $500. New balance: $1500
print(account.withdraw(200)) # Output: Withdrew $200. New balance: $1300
```

### Key Points:
- Instance methods can access and modify object attributes
- They must have `self` as their first parameter
- They are called on instances of the class

---

## Class and Static Methods

### Class Methods
Class methods are bound to the class rather than instances. They can modify class state that applies across all instances.

```python
class Employee:
    raise_amount = 1.04  # Class variable
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, float(pay))

# Using class methods
Employee.set_raise_amount(1.05)

emp_str = "John-Doe-70000"
new_employee = Employee.from_string(emp_str)
print(new_employee.pay)  # Output: 70000.0
```

### Static Methods
Static methods don't operate on instances or classes. They're utility functions that belong to the class.

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def is_workday(day):
        # Monday = 0, Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Using static methods
print(MathUtils.add(5, 3))  # Output: 8

import datetime
my_date = datetime.date(2023, 7, 10)  # A Monday
print(MathUtils.is_workday(my_date))  # Output: True
```

### Key Points:
- Class methods use the `@classmethod` decorator and take `cls` as first parameter
- Static methods use the `@staticmethod` decorator and don't take `self` or `cls`
- Class methods can be used as alternative constructors
- Static methods are used when the method doesn't need to access class or instance data

---

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class. The class being inherited from is called the parent or base class, and the class that inherits is called the child or derived class.

### Basic Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

### The super() Function
The `super()` function is used to call methods from the parent class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent's __init__
        self.student_id = student_id
    
    def display_info(self):
        # Extend parent method
        parent_info = super().display_info()
        return f"{parent_info}, Student ID: {self.student_id}"

# Using super()
student = Student("Alice", 20, "S12345")
print(student.display_info())  # Output: Name: Alice, Age: 20, Student ID: S12345
```

### Multiple Inheritance
Python supports multiple inheritance, where a class can inherit from multiple parent classes.

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return "Quack!"

# Multiple inheritance
duck = Duck("Donald")
print(duck.fly())   # Output: I can fly!
print(duck.swim())  # Output: I can swim!
print(duck.quack()) # Output: Quack!
```

### Method Resolution Order (MRO)
MRO determines the order in which methods are resolved in inheritance hierarchies.

```python
class A:
    def method(self):
        return "A method"

class B(A):
    def method(self):
        return "B method"

class C(A):
    def method(self):
        return "C method"

class D(B, C):
    pass

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

d = D()
print(d.method())  # Output: B method (because B comes before C in MRO)
```

### Key Points:
- Inheritance promotes code reusability
- Child classes can override parent methods
- `super()` is used to access parent class methods
- Multiple inheritance can be powerful but should be used carefully to avoid complexity
- MRO determines the order of method lookup in inheritance hierarchies

---

## Encapsulation

Encapsulation is the bundling of data with the methods that operate on that data. It restricts direct access to some of an object's components.

### Access Modifiers
Python uses naming conventions to indicate access levels:

1. **Public**: Accessible from anywhere (default)
2. **Protected**: Accessible within the class and its subclasses (prefix with `_`)
3. **Private**: Accessible only within the class (prefix with `__`)

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public
        self._account_number = "123456789"    # Protected
        self.__balance = balance              # Private
    
    # Public method to access private attribute
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private attribute with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    # Public method to modify private attribute with validation
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

# Using encapsulation
account = BankAccount("John Doe", 1000)
print(account.account_holder)  # Accessible: John Doe
print(account._account_number) # Accessible but should be treated as protected: 123456789
# print(account.__balance)     # Error: AttributeError (private attribute)

print(account.get_balance())   # Access through public method: 1000
account.deposit(500)
print(account.get_balance())   # 1500
```

### Name Mangling
Python uses name mangling to make private attributes harder to access accidentally.

```python
class Test:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

t = Test()
print(t.public)        # public
print(t._protected)    # protected
# print(t.__private)   # Error: AttributeError

# But private attributes can still be accessed with name mangling
print(t._Test__private)  # private (but you shouldn't do this!)
```

### Key Points:
- Encapsulation helps protect data integrity
- Use public methods to control access to private attributes
- Follow naming conventions to indicate access levels
- Name mangling makes private attributes harder to access accidentally

---

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common super class. It enables using a single interface for different data types.

### Method Overriding
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # Different implementations called
```

### Duck Typing
Python uses duck typing - "If it walks like a duck and quacks like a duck, then it must be a duck."

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Car:
    def speak(self):
        return "Vroom!"

# Duck typing - doesn't care about the type, just the method
def make_sound(obj):
    return obj.speak()

# All these work despite being different types
print(make_sound(Dog()))  # Output: Woof!
print(make_sound(Cat()))  # Output: Meow!
print(make_sound(Car()))  # Output: Vroom!
```

### Operator Overloading
Python allows operators to have different meanings based on context.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overload the * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Overload the string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Using operator overloading
v1 = Vector(2, 3)
v2 = Vector(1, 2)
v3 = v1 + v2  # Uses __add__
v4 = v1 * 3   # Uses __mul__

print(v3)  # Output: Vector(3, 5)
print(v4)  # Output: Vector(6, 9)
```

### Key Points:
- Polymorphism allows different classes to be used interchangeably
- Method overriding provides different implementations of the same method
- Duck typing focuses on what an object can do rather than what it is
- Operator overloading allows custom behavior for operators

---

## Abstraction

Abstraction focuses on hiding complex implementation details and showing only essential features.

### Abstract Base Classes (ABCs)
Python's `abc` module provides tools for creating abstract classes and methods.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    # Concrete method
    def honk(self):
        return "Honk honk!"

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
    def stop_engine(self):
        return "Motorcycle engine stopped"

# Using abstraction
car = Car()
print(car.start_engine())  # Output: Car engine started
print(car.honk())          # Output: Honk honk!

# motorcycle = Vehicle()  # Error: Can't instantiate abstract class
```

### Interfaces with ABCs
Abstract classes can be used to define interfaces.

```python
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLDatabase(DatabaseInterface):
    def connect(self):
        return "Connected to MySQL database"
    
    def disconnect(self):
        return "Disconnected from MySQL database"
    
    def execute_query(self, query):
        return f"Executing '{query}' on MySQL database"

class PostgreSQLDatabase(DatabaseInterface):
    def connect(self):
        return "Connected to PostgreSQL database"
    
    def disconnect(self):
        return "Disconnected from PostgreSQL database"
    
    def execute_query(self, query):
        return f"Executing '{query}' on PostgreSQL database"

# Using the interface
def database_operations(db: DatabaseInterface, query):
    print(db.connect())
    print(db.execute_query(query))
    print(db.disconnect())

mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

database_operations(mysql_db, "SELECT * FROM users")
database_operations(postgresql_db, "INSERT INTO products VALUES (1, 'Laptop')")
```

### Key Points:
- Abstraction hides complex implementation details
- Abstract classes cannot be instantiated
- Abstract methods must be implemented by concrete subclasses
- ABCs help define interfaces and enforce method implementation

---

## Special Methods (Magic/Dunder Methods)

Special methods (also called magic or dunder methods) allow classes to define behavior for built-in operations.

### Common Special Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Formal string representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Length of book
    def __len__(self):
        return self.pages
    
    # Comparison (equality)
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                    self.author == other.author and 
                    self.pages == other.pages)
        return False
    
    # Comparison (less than)
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    # Callable object
    def __call__(self):
        return f"Reading '{self.title}'..."

# Using special methods
book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 500)

print(str(book1))     # Uses __str__: 'Python Basics' by John Doe
print(repr(book1))    # Uses __repr__: Book('Python Basics', 'John Doe', 300)
print(len(book1))     # Uses __len__: 300
print(book1 == book2) # Uses __eq__: False
print(book1 < book2)  # Uses __lt__: True
print(book1())        # Uses __call__: Reading 'Python Basics'...
```

### Context Managers with __enter__ and __exit__
Special methods for creating context managers (used with `with` statement).

```python
class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name
    
    def __enter__(self):
        print(f"Connecting to {self.database_name} database")
        # Simulate connection
        self.connection = f"Connection to {self.database_name}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.database_name} database")
        # Simulate disconnection
        self.connection = None
    
    def execute_query(self, query):
        print(f"Executing: {query}")
        return "Query results"

# Using as context manager
with DatabaseConnection("MyDB") as db:
    result = db.execute_query("SELECT * FROM users")
    print(result)

# Output:
# Connecting to MyDB database
# Executing: SELECT * FROM users
# Query results
# Closing connection to MyDB database
```

### Key Points:
- Special methods allow custom behavior for built-in operations
- They are surrounded by double underscores (e.g., `__init__`, `__str__`)
- Context managers use `__enter__` and `__exit__` for resource management
- Implementing special methods makes classes more Pythonic

---

## Property Decorators

Property decorators provide a way to customize attribute access.

### The @property Decorator
Turns a method into a "getter" for a read-only attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return 2 * self._radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.radius)    # Output: 5 (accessed like attribute)
print(circle.diameter)  # Output: 10
print(circle.area)      # Output: 78.53975

# circle.radius = 10    # Error: can't set attribute (read-only)
```

### Setters and Deleters
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self):
        print("Deleting temperature value")
        self._celsius = 0
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Using property decorators
temp = Temperature(25)
print(temp.celsius)     # Output: 25
print(temp.fahrenheit)  # Output: 77.0

temp.celsius = 30
print(temp.fahrenheit)  # Output: 86.0

temp.fahrenheit = 100
print(temp.celsius)     # Output: 37.777...

# temp.celsius = -300   # ValueError: Temperature below absolute zero

del temp.celsius        # Output: Deleting temperature value
print(temp.celsius)     # Output: 0
```

### Key Points:
- `@property` creates read-only attributes from methods
- Setters (`@attr.setter`) allow controlled attribute modification
- Deleters (`@attr.deleter`) define behavior when attributes are deleted
- Property decorators enable validation and computed attributes

---

## Best Practices

### 1. Follow Naming Conventions
- Class names: `CamelCase`
- Method and function names: `snake_case`
- Constants: `UPPER_CASE`
- Private members: `_single_leading_underscore`
- Strongly private members: `__double_leading_underscore`

### 2. Use Composition Over Inheritance
```python
# Instead of deep inheritance hierarchies, use composition
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def rotate(self):
        return "Wheels rotating"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()
    
    def drive(self):
        return f"{self.engine.start()} and {self.wheels.rotate()}"

car = Car()
print(car.drive())  # Output: Engine started and Wheels rotating
```

### 3. Use Type Hints
```python
from typing import List, Optional

class Employee:
    def __init__(self, name: str, age: int, skills: Optional[List[str]] = None):
        self.name = name
        self.age = age
        self.skills = skills or []
    
    def add_skill(self, skill: str) -> None:
        self.skills.append(skill)
    
    def get_skills(self) -> List[str]:
        return self.skills
```

### 4. Implement __str__ and __repr__
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(str(p))   # Output: Point(3, 4)
print(repr(p))  # Output: Point(x=3, y=4)
```

### 5. Use Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # Default value

# Dataclass automatically generates __init__, __repr__, __eq__, etc.
person = Person("Alice", 30, "alice@example.com")
print(person)  # Output: Person(name='Alice', age=30, email='alice@example.com')
```

### 6. Follow the Single Responsibility Principle
Each class should have a single responsibility.

```python
# Good - separate classes for different responsibilities
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserDatabase:
    def save(self, user):
        # Save user to database
        pass
    
    def load(self, username):
        # Load user from database
        pass

class EmailService:
    def send_welcome_email(self, user):
        # Send welcome email
        pass
```

### 7. Use Exceptions Appropriately
```python
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")  # Output: Error: Not enough funds
```

---

## Conclusion

Object-Oriented Programming in Python provides a powerful way to structure code, promote reusability, and model real-world concepts. By understanding and applying the concepts covered in this guide - classes, inheritance, encapsulation, polymorphism, abstraction, special methods, and property decorators - you can write more organized, maintainable, and Pythonic code.

Remember that OOP is a tool, not a goal in itself. Use it where it makes sense, and don't force OOP patterns where simpler approaches would work better. Happy coding!
