# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes

class car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:   

class electricCar(car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



carDetail = car('Toyota','Corolla')
# print(carDetail.brand)
print(carDetail.model)
print(carDetail.full_name())

carDetailNew = car('Suzuki','Mehran')
# print(carDetailNew.brand)
print(carDetailNew.model)

carDetailNew2 = car('Honda','City')
# print(carDetailNew.brand)
print(carDetailNew2.model)
print(carDetailNew2.fuel_type())


myElectricCar = electricCar('Tesla','Model S','85KWH')
print(myElectricCar.full_name())
print(myElectricCar.fuel_type())