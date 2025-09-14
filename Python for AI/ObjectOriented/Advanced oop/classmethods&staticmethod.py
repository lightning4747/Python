class MyClass:
    class_attribute = "I am a class attribute"
    
    def __init__(self, value):
        self.instance_attribute = value
    
    # Instance Method: takes 'self' as first arg, operates on instance data
    def instance_method(self):
        return f"Instance: {self.instance_attribute}, Class: {self.class_attribute}"
    
    @classmethod
    def class_method(cls):  # takes 'cls' as first arg, operates on the class itself
        return f"Accessing class attribute: {cls.class_attribute}"
    
    @staticmethod
    def static_method():  # takes neither self nor cls
        return "I am just a utility function"

# Usage
obj = MyClass("Hello")
print(obj.instance_method())  # Needs an instance
print(MyClass.class_method())  # Can be called on the class itself
print(MyClass.static_method())  # Called on the class