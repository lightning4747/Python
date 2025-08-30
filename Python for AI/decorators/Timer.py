import time
import functools

def timer(func):
    """Decorator that prints the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # 1. Get start time (high precision)
        value = func(*args, **kwargs)    # 2. Execute the function
        end_time = time.perf_counter()   # 3. Get end time
        run_time = end_time - start_time # 4. Calculate elapsed time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# Using the timer decorator to profile a function
@timer
def waste_time(num_iterations):
    """A function that wastes some CPU time."""
    for _ in range(num_iterations):
        sum([i**2 for i in range(10000)])

waste_time(100)
# Output: Finished 'waste_time' in 0.1234 secs