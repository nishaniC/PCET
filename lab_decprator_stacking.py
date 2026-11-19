#Your time-stamping decorator and test functions go here.
# Follow the numbered steps in the lesson. You can use this starter scaffold.

from datetime import datetime
from functools import wraps

# === Step 1: Implement the decorator ===
def time_stamping_machine(func):
    """Print a timestamp before calling 'func', then return func's result."""
    # TODO:
    # 1) Define a wrapper(*args, **kwargs)
    # 2) Format current time with datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 3) print(f'[{formatted}] Calling "{func.__name__}"')
    # 4) Call func(*args, **kwargs) and return the result
    # 5) (Optional) Use @wraps(func) to preserve metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{ts}] Calling "{func.__name__}"')
        return func(*args, **kwargs)
    return wrapper


# === Step 2: Apply the decorator to a few functions ===
@time_stamping_machine
def say_hello():
    print("Hello from a simple function!")

@time_stamping_machine
def add_two(n1, n2):
    return n1 + n2

@time_stamping_machine
def multiply_two(n1, n2):
    return n1 * n2

# === Step 3: Test your functions ===
if __name__ == "__main__":
    # Expect a timestamp before each call, and correct results printed below.
    say_hello()
    print("Result (add ints):", add_two(10, 5))
    print("Result (add strings):", add_two("Hello", " Python"))
    print("Result (multiply):", multiply_two(7, 6))
