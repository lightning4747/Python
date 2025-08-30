import functools

def repeat(num_times):
    """This is a decorator factory. It returns a decorator.
    Args:
        num_times (int): The number of times to repeat the function call.
    Returns:
        decorator_repeat: The actual decorator function.
    """

    def decorator_repeat(func):
        """The actual decorator function. It takes the function to decorate."""

        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            """The wrapper that does the repetition."""
            results = []
            for _ in range(num_times):
                print(f"Repeating {func.__name__}...")
                result = func(*args, **kwargs)
                results.append(result)
            # For this example, let's just return the last result
            return result # Or you could return the list `results`

        return wrapper_repeat

    return decorator_repeat

# Using the decorator with arguments
@repeat(num_times=3)
def say_hello(name):
    """A simple greeting function."""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

# Calling the decorated function
output = say_hello("World")
print("Final output:", output)
# Output:
# Repeating say_hello...
# Hello, World!
# Repeating say_hello...
# Hello, World!
# Repeating say_hello...
# Hello, World!
# Final output: Greeted World