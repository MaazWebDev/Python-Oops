# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:   

class electricCar(car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size



carDetail = car('Toyota','Corolla')
# print(carDetail.brand)
print(carDetail.model)
print(carDetail.full_name())

carDetailNew = car('Suzuki','Mehran')
# print(carDetailNew.brand)
print(carDetailNew.model)


myElectricCar = electricCar('Tesla','Model S','85KWH')
print(myElectricCar.full_name())
print(myElectricCar.get_brand())