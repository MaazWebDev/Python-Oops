# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


carDetail = car('Toyota','Corolla')
print(carDetail.brand)
print(carDetail.model)
print(carDetail.full_name())

carDetailNew = car('Suzuki','Mehran')
print(carDetailNew.brand)
print(carDetailNew.model)