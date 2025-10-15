class Car:
    def __init__(self, make, model, year):
        self.make = make     
        self.model = model    
        self.year = year      

    def start(self):
        print(f"The {self.year} {self.make} {self.model} has started.")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} has stopped.")

my_car = Car("Toyota", "Corolla", 2022)

my_car.start()
my_car.stop()
