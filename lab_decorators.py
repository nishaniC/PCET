from functools import wraps

# Step 1: implement log_calls(func)
def log_calls(func):
    """Print the function name and its *args/**kwargs, then call and return the result."""
    # TODO:
    # 1) Wrap 'func' with an inner function named 'wrapper' that accepts (*args, **kwargs).
    # 2) Print the function name (func.__name__) and the exact args/kwargs received.
    # 3) Forward the call with func(*args, **kwargs) and return the result.
    # 4) (Optional) decorate 'wrapper' with @wraps(func) to preserve metadata.
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling "{func.__name__}" with:')
        print(f'  args = {args}')
        print(f'  kwargs = {kwargs}')
        return func(*args, **kwargs)
    return wrapper

# Demo targets for Step 1 (you may edit or add your own)
@log_calls
def adder(a, b):
    return a + b

@log_calls
def make_user(*, name, age):
    return {"name": name, "age": age}

adder(1,2)
make_user(name="John", age=20)


# Step 2: implement tagged_logger(tag) -> decorator
def tagged_logger(tag):
    """Return a decorator that prints [tag] before calling the function, supporting any arguments."""
    # TODO:
    # 1) Return an inner 'decorator(func)'.
    # 2) Inside it, define 'wrapper(*args, **kwargs)' that logs: [tag], func.__name__, args, kwargs.
    # 3) Call func(*args, **kwargs) and return the result.
    # 4) Use @wraps(func) on the wrapper to preserve function metadata.
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'[{tag}] "{func.__name__}" args={args}, kwargs={kwargs}')
            return func(*args, **kwargs)
        return wrapper
    return decorator



@tagged_logger("INVENTORY")
def pack_items(*args, fragile=False, **kwargs):
    print("Packing:", args, "fragile:", fragile, "meta:", kwargs)
    return len(args)


if __name__ == "__main__":
    # Manual checks (no testing framework)
    print("adder result:", adder(2, 3))
    print("make_user result:", make_user(name="Ann", age=31))
    count = pack_items("book", "toy", fragile=True, box="M1", location="A-12")
    print("packed count:", count)

