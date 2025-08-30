def smart_decorator(func):
    """A smarter decorator that handles functions with arguments and return values.
    Uses *args and **kwargs to accept any number of positional and keyword arguments.
    """

    def wrapper(*args, **kwargs):
        """A generic wrapper function.
        *args: captures all positional arguments as a tuple.
        **kwargs: captures all keyword arguments as a dictionary.
        """
        print(f"About to call {func.__name__} with args: {args}, kwargs: {kwargs}")

        # Pass the arguments through to the original function and capture its return value
        result = func(*args, **kwargs)  # Unpacks the arguments back into the function call

        print(f"{func.__name__} returned: {result}")
        return result  # It is CRUCIAL to return the original function's result

    return wrapper

# Decorate a function that has arguments and a return value
@smart_decorator
def greet(name, greeting="Hello", punctuation="!"):
    """A function that takes arguments and returns a value."""
    full_greeting = f"{greeting}, {name}{punctuation}"
    return full_greeting

# Call the decorated function
message = greet("Alice", greeting="Hi", punctuation="!!")
print("Final message:", message)
# Output:
# About to call greet with args: ('Alice',), kwargs: {'greeting': 'Hi', 'punctuation': '!!'}
# greet returned: Hi, Alice!!!
# Final message: Hi, Alice!!!