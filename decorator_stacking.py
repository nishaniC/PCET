def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print("The whole order is packed with", collective_material)
        return internal_wrapper
    return wrapper

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print("* Wrapping items with", material)
        return internal_wrapper
    return wrapper

@big_container("plain cardboard")
@warehouse_decorator("bubble foil")
def pack_books(*args):
    print("Packing books:", args)

@big_container("colorful cardboard")
@warehouse_decorator("foil")
def pack_toys(*args):
    print("Packing toys:", args)

@big_container("strong cardboard")
@warehouse_decorator("cardboard")
def pack_fruits(*args):
    print("Packing fruits:", args)

pack_books("Alice in Wonderland", "Winnie the Pooh")
pack_toys("doll", "car")
pack_fruits("plum", "pear")