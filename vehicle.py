from speed_ticket import SpeedTicket
import pickle
from file_handler import write_car_info_from_pickle_file

# 3. Внесите изменения в класс Vehicle из предыдущей отправки, добавьте поле для регистрационного номера.

# 5. класс Vehicle должен иметь возможность зарегистрировать одно или несколько нарушений скорости, использовать соответствующую структуру данных для их хранения.

class Vehicle:
    def __init__(self, reg_num, make, model, millage, price):
        self.reg_num = reg_num
        self.make = make
        self.model = model
        self.millage = millage
        self.price = price
        self.speed_tickets = []

    def __str__(self):
        return (f"Here are all properties of the {type(self).__name__}:"
            f"\n\tRegistration number: {self.reg_num}."
            f"\n\tMake: {self.make}."
            f"\n\tModel: {self.model}."
            f"\n\tMillage: {self.millage}."
            f"\n\tPrice: {self.price}.")

    def add_speed_ticket(self, speed_ticket: SpeedTicket) -> None:
        self.speed_tickets.append(speed_ticket)
    
    