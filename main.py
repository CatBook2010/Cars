import functions
from pprint import pprint

going = True
while going:
    vehicles_list = functions.write_car_info_from_pickle_file("vehicles.pickle")
    print("        MENU\n1) New car\n2) New truck\n3) New SUV\n4) Find vehicles by make\n5) Show all vehicles\n6) Check vehicles for speed violation\n7) Quit")

    num = int(input("Enter your choice: "))

    if num == 1:
        functions.update_data("car", vehicles_list)
    elif num == 2:
        functions.update_data("truck", vehicles_list)
    elif num == 3:
        functions.update_data("SUV", vehicles_list)
    elif num == 4:
        functions.find_vehicles_by_make()
    elif num == 5:
        vehicle_in_dict = functions.print_all_vehicles(vehicles_list)
        # vehicle_list = functions.write_car_info_from_pickle_file("vehicles.pickle")
        # pprint(vehicle_list)
    elif num == 6:
        functions.find_violate_vehicles()
    elif num == 7:
        going = False
    else:
        print("Please, write a nummber from 1 to 7.")

    print()

print("Exiting the program...")