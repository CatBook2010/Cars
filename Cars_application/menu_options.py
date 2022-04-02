from Modules.create_vehicle_object import create_vehicle_object
from Modules.radars import listSpeeders
from Modules.file_handler import FileHandler
from Vehicles.speed_ticket import SpeedTicket
import pickle

class MenuOptions:

    def __init__(self):
        pass

    def update_data(vehicle_type: str, vehicles_list: list) -> None:
        vehicle = create_vehicle_object(vehicle_type)
        vehicles_list.append(vehicle)
        vehicles_list.sort(key = lambda x: x.make)
        FileHandler.write_car_info_to_pickle_file("vehicles.pickle", vehicles_list)
        FileHandler.write_car_info_to_text_file("vehicles.txt", vehicles_list)
        
    def find_vehicles_by_make() -> None:
        print("Find vehicle by name")
        
        make_to_find = input("Enter the name of the brand you are looking for: ")
    
        make_list = []
        vehicles_list = FileHandler.write_car_info_from_pickle_file("vehicles.pickle")
        for vehicle in vehicles_list:
            if make_to_find in vehicle.make:
                make_list.append(vehicle)
    
        if not make_list:
            print(f"Not found, try other request, but {make_to_find}.")
        else:
            print(f"Vehicles with make {make_to_find} found: {len(make_list)}")
            for vehicle in make_list:
                print(vehicle.make)
        
    def print_all_vehicles(vehicles_list) -> None:

        if vehicles_list:
            print("The following vehicles are in inventory: ")
            for vehicle in vehicles_list:
                print()
                print(vehicle)
        else:
            print("There are no cars in the inventory yet.")
            
    def registrate_violation(vehicle, time, car_speed, speed_limit, vehicle_list, vehicle_index, speed_tickets) -> None:
        new_speed_ticket = SpeedTicket(vehicle.reg_num, time, car_speed, speed_limit)
        if new_speed_ticket not in speed_tickets:
            vehicle_list[vehicle_index].add_speed_ticket(new_speed_ticket)
            print(new_speed_ticket)
            with open("Cars_application/Output/" + "speed_tickets.pickle", "wb+") as speed_tickets_pickle:
                pickle.dump(new_speed_ticket, speed_tickets_pickle)

    @classmethod 
    def find_violate_vehicles(self) -> None:
        
        speed_limit = 60
        distance = 5
        
        vehicle_list = FileHandler.write_car_info_from_pickle_file("vehicles.pickle")
        speed_tickets = FileHandler.write_car_info_from_pickle_file("speed_tickets.pickle")
        violators = listSpeeders("box_a.txt", "box_b.txt", speed_limit, distance)

        violation_found = False
        for vehicle_index, vehicle in enumerate(vehicle_list):
            if vehicle.reg_num in violators:
                violation_found = True
                car_speed, time = violators[vehicle.reg_num]
                self.registrate_violation(vehicle, time, car_speed, speed_limit, vehicle_list, vehicle_index, speed_tickets)

    
        FileHandler.write_car_info_to_pickle_file("vehicles.pickle", vehicle_list)
    
        if not violation_found:
            print("No cars violated speed rules.")