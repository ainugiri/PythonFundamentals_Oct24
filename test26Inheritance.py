class Vehicles:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def info(self):
        print("This is a vehicle class")
    def print_info(self):
        print(self.year, self.make, self.model)

class Car(Vehicles):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    def welcome(self):
        print("Welcome to the car class")
        print("You have a car with", self.doors, "doors")

    def print_info(self):
        print(self.year, self.make, self.model, self.doors)
        
class Bike(Vehicles):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year)
        self.cc = cc

    def print_info(self):
        print(self.year, self.make, self.model, self.cc)
    
    def welcome(self):
        print("Welcome to the bike class")
        print("You have a bike with", self.cc, "cc")
        

c1  = Car("Toyota", "Corolla", 2016, 4)
c2 = Car("Suzuki", "Ciaz", 2017, 4)
b1 = Bike("Honda", "CBR", 2018, 250)
b2 = Bike("Yamaha", "R15", 2019, 150)
c1.info()
b1.info()  
c1.welcome()
b1.welcome()