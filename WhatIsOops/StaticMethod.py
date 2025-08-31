# Static Method

# Problem: Add a static method to the Car class that returns a general description of a car.


class car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_discription():
        return 'Car Are Means Of Transport'

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:   

class electricCar(car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



car('Toyota','Corolla')
# print(carDetail.brand)
# print(carDetail.model)
# print(carDetail.full_name())

car('Suzuki','Mehran')
# print(carDetailNew.brand)
# print(carDetailNew.model)

my_car = car('Honda','City')
# print(carDetailNew.brand)
# print(carDetailNew2.model)
# print(carDetailNew2.fuel_type())


# myElectricCar = electricCar('Tesla','Model S','85KWH')
# myElectricCar2 = electricCar('Tesla','Model Z','100KWH')
# print(myElectricCar.full_name())
# print(myElectricCar.fuel_type())

print(car.total_car)
print(my_car.general_discription())
print(car.general_discription())