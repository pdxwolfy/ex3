class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        return super().start_engine() + f" Drive {speed}, please!"

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'
