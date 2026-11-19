def sample_decorator(func):
    print("Decorator function called with:", func.__name__)
    return func

def greet():
    print("Greetings from the greet function!")

wrapped_func = sample_decorator(greet)
#wrapped_func()
#greet()
