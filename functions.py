from car import Car
from truck import Truck
from SUV import SUV
import pickle
from radars import listSpeeders
from pprint import pprint
from file_handler import *
from speed_ticket import SpeedTicket


def create_vehicle_object(vehicle_type: str):
    vehicle_argument_object = {
        "car" : {
            "argument" : "Doors",
            "class"    : Car
        },
        "truck" : {
            "argument" : "Drivetype",
            "class"    : Truck
        },
        "SUV" : {
            "argument" : "Number of passengers",
            "class"    : SUV
        }
    }

    last_argument = vehicle_argument_object[vehicle_type]["argument"]
    vehicle_class = vehicle_argument_object[vehicle_type]["class"]
    print(f"Input {vehicle_class.__name__} data: ")
    attributes = (
            input("\tRegistration number: "),
            input("\tMake: "),
            int(input("\tModel: ")),
            int(input("\tMillage: ")),
            int(input("\tPrice: ")),
            int(input(f"\t{last_argument}: "))
    )

    return vehicle_class(*attributes)


# def write_car_info_to_text_file(text_file_name: str, vehicles_list: list) -> None:
#     with open(text_file_name, "a") as text_file:
#         for vehicle in vehicles_list:
#             text_file.write(str(vehicle)+"\n")

# def write_car_info_to_pickle_file(pickle_file_name: str, vehicles_list) -> None:
#     with open(pickle_file_name, "wb") as pickle_file:
#         for vehicle in vehicles_list:
#             pickle.dump(vehicle, pickle_file)
            

# def write_car_info_from_pickle_file(pickle_file_name: str) -> list:
#     vehicle_list = []
#     with open(pickle_file_name, "rb") as pickle_file:
#         while True:
#             try:
#                 vehicle = pickle.load(pickle_file)
#                 vehicle_list.append(vehicle)
#             except EOFError:
#                 break

#     return vehicle_list


def update_data(vehicle_type: str, vehicles_list: list) -> None:
    vehicle = create_vehicle_object(vehicle_type)
    vehicles_list.append(vehicle)
    write_car_info_to_pickle_file("vehicles.pickle", vehicles_list)
    write_car_info_to_text_file("vehicles.txt", vehicles_list)
    

def print_all_vehicles(vehicles_list):
    print("The following vehicles are in inventory: ")

    for vehicle in vehicles_list:
        print()
        print(vehicle)


def find_vehicles_by_make():
    print("Find vehicle by name")
    
    make_to_find = input("Enter the name of the brand you are looking for: ")

    make_list = []
    with open("vehicles.txt", "r") as vehicles:
        vehicles_list = vehicles.readlines()
        for line in vehicles_list:
            if "Make" in line.strip():
                make = line.split(": ")[-1].strip()[:-1]
                make_list.append(make)
    
    if make_to_find not in make_list:
        print(f"Not found, try other request, but {make_to_find}.")
    else:
        print(f"Vehicles with make {make_to_find} found: {make_list.count(make_to_find)}")


def registrate_violation(self, time, car_speed, speed_limit):
    speed_tickets = write_car_info_from_pickle_file("speed_tickets.pickle")
    with open("speed_tickets.pickle", "a+") as speed_tickets_pickle:
        for speed_ticket in self.speed_tickets:
            new_speed_ticket = SpeedTicket(self.reg_num, time, car_speed, speed_limit)
            if new_speed_ticket not in speed_tickets:
                self.add_speed_ticket(new_speed_ticket)
                pickle.dump(new_speed_ticket, speed_tickets_pickle)


def find_violate_vehicles():
    
    speed_limit = 60
    distance = 5
    
    vehicle_list = write_car_info_from_pickle_file("vehicles.pickle")
    speed_tickets = write_car_info_from_pickle_file("speed_tickets.pickle")
    violators = listSpeeders("box_a.txt", "box_b.txt", speed_limit, distance)
    # pprint(violators)
    
    violation_found = False
    for vehicle_index, vehicle in enumerate(vehicle_list):
        if vehicle.reg_num in violators:
            violation_found = True
            car_speed, time = violators[vehicle.reg_num]
            new_speed_ticket = SpeedTicket(vehicle.reg_num, time, car_speed, speed_limit)
            if new_speed_ticket not in speed_tickets:
                vehicle_list[vehicle_index].add_speed_ticket(new_speed_ticket)
                print(new_speed_ticket)
                with open("speed_tickets.pickle", "ab+") as speed_tickets_pickle:
                    pickle.dump(new_speed_ticket, speed_tickets_pickle)

                # print(True, vehicle_index)

    write_car_info_to_pickle_file("vehicles.pickle", vehicle_list)

    if not violation_found:
        print("No cars violated speed rules.")