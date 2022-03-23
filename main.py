import functions

going = True
while going:
    print("        MENU\n1) New car\n2) New truck\n3) New SUV\n4) Find vehicles by make\n5) Show all vehicles\n6) Check vehicles for speed violation\n7) Quit")

    num = int(input("Enter your choice: "))

    if num == 1:
        functions.new_car()
    elif num == 2:
        functions.new_truck()
    elif num == 3:
        functions.new_SUV()
    elif num == 4:
        functions.find_vehicles_by_make()
    elif num == 5:
        vehicle_in_dict = functions.print_all_vehicles()
    elif num == 6:
        print("No cars violated speed rules")
    elif num == 7:
        print("Exiting the program...")
        going = False
    else:
        print("Please, write a nummber from 1 to 7.")

    print()