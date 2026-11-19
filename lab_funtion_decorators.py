# Step 1: Define the decorator function
def announce_call(function):
    print(f'About to call "{function.__name__}"')
    return function

# Step 2: Define a simple function to decorate
def say_hi():
    print('Hi from a decorated function!')

# Step 3: Apply the decorator manually
decorated = announce_call(say_hi)
decorated()

# Step 4: Use the @ syntax
@announce_call
def say_hello():
    print('Hello from a decorated function!')

say_hello()