from Vehicles.vehicle import Vehicle

class SUV(Vehicle):
    def __init__(self, reg_num, make, model, millage, price, num_of_passengers):
        super().__init__(reg_num, make, model, millage, price)
        self.num_of_passengers = num_of_passengers

    def __str__(self):
        return super().__str__() + f"\n\tNumber of passengers: {self.num_of_passengers}."