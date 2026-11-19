# Step 1: Create a decorator that logs when sensitive attributes are accessed
def watch_attributes(cls):
    """Log access to sensitive attributes like 'email' and 'access_level'."""
    cls.__getattr__orig = cls.__getattribute__
    original_setattr = cls.__setattr__

    def new_getattr(self, name):
        if name in( "email" , "access_level"):
            print(f"[SECURITY] Accessed sensitive attribute: {name} ")
        # Forward the call to the original method so the actual attribute is returned.
        return cls.__getattr__orig(self, name)

#How could you extend the watch_attributes decorator to log write operations (attribute changes) as well as reads?
#A common way is to do for writes what you did for reads:
#Save the original __setattr__.
#Replace it with a wrapper.
#Log the change if the attribute is sensitive.
#Forward the operation to the original method.
    def new_setattr(self, name, value):
        if name in ("email", "access_level"):
            print(
                f"[SECURITY] Changed sensitive attribute: "
                f"{name} -> {value}"
            )

        return original_setattr(self, name, value)

    # 3. Replace the class's original __getattribute__ with our new version.
    cls.__getattribute__ = new_getattr
    # Replace the class's original __setattr__ with our new version.
    cls.__setattr__ = new_setattr
    return cls


# Step 2: Create a decorator that adds a reporting method to the class
def add_report_method(cls):
    """Add a report() method that prints all user information."""
    def report(self  ):
        print("User Report:")
        for item in self.__dict__.items():
            print(f"{item[0]}: {item[1]}")

    cls.report = report
    return cls

# Step 3: Define and decorate the User class

@add_report_method
@watch_attributes
class User:
    def __init__(self, name, email, department, access_level):
        self.name = name
        self.email = email
        self.department = department
        self.access_level = access_level



# Manual test
if __name__ == "__main__":
    user = User("Alice", "alice@company.com", "Engineering", "admin")

    # Access some attributes to trigger logging
    print("Department:", user.department)
    print("Email:", user.email)
    print("Access Level:", user.access_level)

    print()
    # Generate a full user report
    user.report()

