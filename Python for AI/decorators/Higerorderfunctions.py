def greeter(name):
    """A simple function that returns a greeting."""
    return f"Hello, {name}!"

def loud_greeter(func, name):
    """A higher-order function.
    It takes a function `func` and a string `name` as arguments.
    It calls `func` and modifies its result.
    """
    # 1. Call the passed function
    greeting = func(name)
    # 2. Modify the result
    new_greeting = greeting.upper() + "!!!"
    # 3. Return the modified result (a string, not a function)
    return new_greeting

# Using the higher-order function
result = loud_greeter(greeter, "Alice") # Notice: greeter, not greeter()
print(result) # Output: HELLO, ALICE!!!!