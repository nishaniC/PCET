def object_counter(cls):
    # 1. Save the original __getattribute__ so we can still return real values later.
    cls.__getattr__orig = cls.__getattribute__

    # 2. Define a new __getattribute__ that logs specific attribute reads.
    def new_getattr(self, name):
        if name == "mileage":
            print("We noticed that the mileage attribute was read")
        # Forward the call to the original method so the actual attribute is returned.
        return cls.__getattr__orig(self, name)

    # 3. Replace the class's original __getattribute__ with our new version.
    cls.__getattribute__ = new_getattr
    return cls

@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car("ABC123")

# Because we replaced __getattribute__, reading car.mileage triggers our log.
print("The mileage is", car.mileage)
print("The VIN is", car.VIN)
