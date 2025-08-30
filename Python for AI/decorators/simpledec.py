def my_decorator(func):
    """A simple decorator function.
    Args:
        func: The function to be decorated (wrapped).
    Returns:
        wrapper_function: The new function with added behavior.
    """

    def wrapper_function():
        """The wrapper function that 'wraps' the original function.
        This is what will be executed when the decorated function is called.
        """
        # 1. Do something BEFORE calling the original function
        print("Something is happening before the function is called.")

        # 2. Call the original function
        func()

        # 3. Do something AFTER calling the original function
        print("Something is happening after the function is called.\n")

    # Return the wrapper function, ready to be called later
    return wrapper_function

# Let's apply the decorator manually to see how it works
def say_hello():
    """A simple function we want to decorate."""
    print("Hello!")

# Applying the decorator using @ syntax
@my_decorator  # This is the same as saying: say_goodbye = my_decorator(say_goodbye)
def say_goodbye():
    """This function is now decorated by `my_decorator`."""
    print("Goodbye!")


# Apply the decorator: pass `say_hello` to `my_decorator`
decorated_hello = my_decorator(say_hello)
# `decorated_hello` is now the `wrapper_function` from inside `my_decorator`
print(decorated_hello) # Output: <function my_decorator.<locals>.wrapper_function at 0x...>

# Call the decorated function
decorated_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
say_goodbye()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.