def simple_hello():
    print('Hello from a simple function!')

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

decorated = simple_decorator(simple_hello)
decorated()

#
def simple_decoratorv2(function):
    print('in v2 We are about to call "{}"'.format(function.__name__))
    return function

@simple_decoratorv2
def simple_hellov2():
    print('in v2 Hello from a simple function!')

simple_hellov2()

def simple_decoratorv3(own_function):
    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')
    return internal_wrapper

@simple_decoratorv3
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

print("===========")
combiner('a', 'b', exec='yes')

@simple_decoratorv3
def combiner2():
    print('in combiner2 no argument function!')

print("===========")
combiner2()

print("===========")

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')

