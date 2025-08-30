def outer_function(msg):
    """An outer function that takes an argument."""

    def inner_function():
        """An inner function that 'remembers' the `msg` argument.
        This is a CLOSURE: it captures and remembers the `msg` variable
        from the outer scope, even after `outer_function` has finished running.
        """
        print(f"Message from outer function: {msg}")

    # Return the inner function *without executing it* (no parentheses)
    return inner_function

# Call outer_function. It returns the inner_function definition.
my_func = outer_function("Hello, Closure!")
print(my_func)   # Output: <function outer_function.<locals>.inner_function at 0x...>

# Now call the returned inner function
my_func()        # Output: Message from outer function: Hello, Closure!
# The inner function still has access to the `msg` variable ("Hello, Closure!")
# even though `outer_function` has already finished execution.