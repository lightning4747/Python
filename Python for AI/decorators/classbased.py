import functools

class CountCalls:
    """A class-based decorator that counts how many times a function is called.
    This demonstrates how decorators can also maintain state.
    """

    def __init__(self, func):
        """The initializer is called when the decorator is applied (@CountCalls).
        It receives the function to be decorated.
        """
        functools.wraps(self)(func) # Helps preserve metadata
        self.func = func
        self.num_calls = 0 # This is the state we are maintaining

    def __call__(self, *args, **kwargs):
        """The __call__ method is called when the decorated function is called.
        This is where the wrapping logic goes.
        """
        self.num_calls += 1 # Update state
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs) # Call the original function

# Using the class-based decorator
@CountCalls
def say_hello():
    print("Hello!")

say_hello() # Output: Call 1 of 'say_hello' \n Hello!
say_hello() # Output: Call 2 of 'say_hello' \n Hello!
print(f"Total calls: {say_hello.num_calls}") # Output: Total calls: 2