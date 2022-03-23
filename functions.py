from car import Car
from truck import Truck
from SUV import SUV

def read_vehicle(vehicle):
    vehicle = vehicle.strip("{").strip("}")
    # vehicle = vehicle.strip("}")
        
    vehicle_in_list = vehicle.split(", ")
    vehicle_in_dict = {}
        
    for element in vehicle_in_list:
        element_in_list = element.split(": ")
        key, value = element_in_list
        vehicle_in_dict[key] = value
        
    output = ""
    for key, value in vehicle_in_dict.items():
        key = key.strip("'")
        value = value.strip("'")
        output += f"{key}: {value} "
    return output, vehicle_in_dict



def new_car():
    print("Add a new car")
    print("Input car data: ")

    reg_num = input("\tRegistration number: ")
    make = input("\tMake: ")
    model = int(input("\tModel: "))
    millage = int(input("\tMillage: "))
    price = int(input("\tPrice: "))
    doors = int(input("\tDoors: "))
    
    new_car = Car(reg_num, make, model, millage, price, doors)
    
    # car_dict = {
    #     "Registration number" : reg_num,
    #     "Make" : make,
    #     "Model" : model,
    #     "Millage" : millage,
    #     "Price" : price,
    #     "Doors" : doors
    # }
    
    with open("vehicles.txt", "a") as vehicles:
        vehicles.write(str(new_car)+"\n")



def new_truck():
    print("Add a new truck")
    print("Input truck data: ")
    
    reg_num = input("\tRegistration number: ")
    make = input("\tMake: ")
    model = int(input("\tModel: "))
    millage = int(input("\tMillage: "))
    price = int(input("\tPrice: "))
    drivetype = str(input("\tDrivetype: "))
    
    new_truck = Truck(reg_num, make, model, millage, price, drivetype)

    truck_dict = {
        "Registration number" : reg_num,
        "Make" : make,
        "Model" : model,
        "Millage" : millage,
        "Price" : price,
        "Drivetype" : drivetype
    }

    with open("vehicles.txt", "a") as vehicles:
        vehicles.write(str(new_truck) + "\n")



def new_SUV():
    print("Add a new SUV")
    print("Input SUV data: ")
    
    reg_num = input("\tRegistration number: ")
    make = input("\tMake: ")
    model = int(input("\tModel: "))
    millage = int(input("\tMillage: "))
    price = int(input("\tPrice: "))
    num_of_passengers = int(input("\tNumber of passengers: "))

    new_SUV = SUV(reg_num, make, model, millage, price, num_of_passengers)

    SUV_dict = {
        "Registration number" : reg_num,
        "Make" : make,
        "Model" : model,
        "Millage" : millage,
        "Price" : price,
        "Number of passengers" : num_of_passengers
    }

    with open("vehicles.txt", "a") as vehicles:
        vehicles.write(str(new_SUV) + "\n")



def print_all_vehicles():
    print("The following cars are in inventory: ")

    with open("vehicles.txt", "r") as vehicles:
        vehicles_list = vehicles.readlines()
        for line in vehicles_list:
            if "Here are all properties" in line:
                print()
            # output, vehicle_in_dict = read_vehicle(vehicle)
            print(line.strip())
            # print(output)



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