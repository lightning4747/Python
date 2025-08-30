import functools

def metadata_preserving_decorator(func):
    """A decorator that uses functools.wraps to preserve the original function's metadata."""

    @functools.wraps(func) # This decorator copies metadata from `func` to `wrapper`
    def wrapper(*args, **kwargs):
        """Wrapper function's docstring. This will be hidden by @functools.wraps."""
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished calling {func.__name__}.")
        return result
    return wrapper

@metadata_preserving_decorator
def calculate_sum(a, b):
    """This function adds two numbers together."""
    return a + b

# Test the decorated function
result = calculate_sum(5, 3)
print("Result:", result)

# Check if metadata is preserved (THIS IS THE CRITICAL TEST)
print("Function name:", calculate_sum.__name__)  # Output: 'calculate_sum' (NOT 'wrapper')
print("Function docstring:", calculate_sum.__doc__) # Output: 'This function adds two numbers together.'