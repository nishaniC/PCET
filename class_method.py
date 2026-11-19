class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1
        self.value = value

    @classmethod
    def get_internal(cls):
        return f'# of objects created: {cls.__internal_counter}'

print(Example.get_internal())      # Shows 0
ex1 = Example(10)
print(Example.get_internal())      # Shows 1
ex2 = Example(99)
print(Example.get_internal())      # Shows 2
