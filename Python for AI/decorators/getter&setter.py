class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # "Private" variable
    
    @property
    def celsius(self):  # Getter
        print("Getting value...")
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):  # Setter
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible.")
        self._celsius = value
    
    @property
    def fahrenheit(self):  # A read-only property (no setter defined)
        return (self._celsius * 9/5) + 32

# Usage
temp = Temperature(25)
print(temp.celsius)    # Uses the getter
temp.celsius = 30      # Uses the setter
print(temp.fahrenheit) # 86.0
# temp.fahrenheit = 100  # AttributeError: can't set attribute