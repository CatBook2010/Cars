from car import Car
from truck import Truck
from SUV import SUV
import pickle
from radars import listSpeeders


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


def write_car_info_to_text_file(text_file_name: str, vehicles_list: list) -> None:
    with open(text_file_name, "a") as text_file:
        for vehicle in vehicles_list:
            text_file.write(str(vehicle)+"\n")

def write_car_info_to_pickle_file(pickle_file_name: str, vehicles_list) -> None:
    with open(pickle_file_name, "wb") as pickle_file:
        for vehicle in vehicles_list:
            pickle.dump(vehicle, pickle_file)
            

def write_car_info_from_pickle_file(pickle_file_name: str) -> list:
    vehicle_list = []
    with open(pickle_file_name, "rb") as pickle_file:
        while True:
            try:
                vehicle = pickle.load(pickle_file)
                vehicle_list.append(vehicle)
            except EOFError:
                break

    return vehicle_list


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

def find_violate_vehicles():
    # Взяти всі види транспорту
    # Подивитися інформацію про їх реєстраційні номера
    # Якщо їх реєстраційні номера в radars.list_speeders, то створити квитки
    # Й вивести інформаціюі про квитки

    vehicle_list = write_car_info_from_pickle_file("vehicles.pickle")
    speed_tickets = write_car_info_from_pickle_file("speed_tickets.pickle")
    print(1)
    speed, speed_limit = 60, 5
    violators = listSpeeders("box_a.txt", "box_b.txt", speed, speed_limit)
    print(vehicle_list)

    
    for vehicle in vehicle_list:
        print(1.5)
        if vehicle.reg_num in violators.values():
            print(2)
            speed_ticket_found = False
            while not speed_ticket_found:
                print(3)
                for speed_ticket in speed_tickets:
                    print(4)
                    if vehicle.reg_num == speed_ticket.reg_num:
                        print(str(speed_ticket))
                        speed_ticket_found = True
                        print(5)
                        break
    
                if not speed_ticket_found:
                    print(4.5)
                    vehicle.registrate_violation(violators[vehicle.reg_num][1], speed, speed_limit)
