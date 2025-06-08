#define

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return(self.year, self.brand, self.model)
    
    def get_year (self):
        return(self.year)

    def get_brand (self):
        return(self.brand)
    
    def get_model (self):
        return(self.model)

#we need to make an object that uses the class's attributes

my_car = Car("toyota", "camry", "2023")
my_car2 = Car("honda", "civic", "1999")
print(my_car.get_brand())
