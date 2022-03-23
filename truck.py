from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, reg_num, make, model, millage, price, drive_type):
        super().__init__(reg_num, make, model, millage, price)
        self.drive_type = drive_type

    def __str__(self):
        return super().__str__() + f"\n\tDrivetype: {self.drive_type}."