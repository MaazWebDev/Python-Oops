# What Are Classes And Object

# Classes and objects are the two core concepts in object-oriented programming.
# A class defines what an object should look like, and an object is created based on that class. For example:

# Class	 Objects
# Fruit	 Apple, Banana, Mango
# Car	 Volvo, Audi, Toyota

# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class car:
    brand : None
    model : None

My_car = car()
print(My_car)


# __init__ method()

# To understand the meaning of classes we have to understand the built-in __init__() method.
# All classes have a method called __init__(), which is always executed when the class is being initiated.
# Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Self keyword
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class employee:
    def __init__(self,email,password):
        self.email = email
        self.password = password


employeeDetail = employee('abc@gmail.com','abc123')
print(employeeDetail.email)
print(employeeDetail.password)

employeeDetailNew = employee('xyz@gmail.com','xyz123')
print(employeeDetailNew.email)
print(employeeDetailNew.password)

# Delete Object Property

# del employeeDetail.email

# Delete Object

# del employeeDetail