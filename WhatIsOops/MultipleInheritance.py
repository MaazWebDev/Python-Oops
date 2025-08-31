# Multiple Inheritance

# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_discription():
        return 'Car Are Means Of Transport'
    
    @property
    def model(self):
        return self.__model

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:   

class electricCar(car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



# car('Toyota','Corolla')
# print(carDetail.brand)
# print(carDetail.model)
# print(carDetail.full_name())

# car('Suzuki','Mehran')
# print(carDetailNew.brand)
# print(carDetailNew.model)

# my_car = car('Honda','City')
# my_car.model = 'Tata'
# print(my_car.model)
# print(carDetailNew.brand)
# print(carDetailNew2.model)
# print(carDetailNew2.fuel_type())


myElectricCar = electricCar('Tesla','Model S','85KWH')
# print(isinstance(myElectricCar,car))
# print(isinstance(myElectricCar,electricCar))

myElectricCar2 = electricCar('Tesla','Model Z','100KWH')
# print(myElectricCar.full_name())
# print(myElectricCar.fuel_type())

print(car.total_car)
print(car.general_discription())

class Battery:
    def battery_info(self):
        return 'This is Battery'

class Engine:
    def engine_info(self):
        return 'This is Engine'

class NewElectricCar2(Battery,Engine,car):
    pass

my_new_tesla = NewElectricCar2('Tesla','Model S')
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())