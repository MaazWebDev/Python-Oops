# Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:   

class electricCar(car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size



carDetail = car('Toyota','Corolla')
print(carDetail.brand)
print(carDetail.model)
print(carDetail.full_name())

carDetailNew = car('Suzuki','Mehran')
print(carDetailNew.brand)
print(carDetailNew.model)


myElectricCar = electricCar('Tesla','Model S','85KWH')
print(myElectricCar.full_name())