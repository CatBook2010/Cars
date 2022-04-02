from Vehicles.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, reg_num, make, year, millage, price, num_of_doors):
        super().__init__(reg_num, make, year, millage, price)
        self.num_of_doors = num_of_doors

    def __str__(self):
        return super().__str__() + f"\n\tDoors: {self.num_of_doors}."