from Modules.file_handler import FileHandler
from menu_options import MenuOptions

class MenuChoices:

    def display_menu():
        print('\n        MENU')
        print('1) New car')
        print('2) New truck')
        print('3) New SUV')
        print('4) Find vehicles by make')
        print('5) Show all vehicles')
        print('6) Check vehicles for speed violation')
        print('7) Quit')

    @classmethod # Конструктор / Constructor - надстройка (методу)
    def process_choice(self):
        NEW_CAR_CHOICE = 1
        NEW_TRUCK_CHOICE = 2
        NEW_SUV_CHOICE = 3
        FIND_VEHICLE_CHOICE = 4
        SHOW_VEHICLES_CHOICE = 5
        CHECK_SPEED_VIOLATION_CHOICE = 6
        QUIT_CHOICE = 7
        
        choice = 0
        
        while choice != QUIT_CHOICE:
            vehicles_list = FileHandler.write_car_info_from_pickle_file("vehicles.pickle")

            self.display_menu()
            choice = int(input("Enter your choice: "))
            print()
        
            if choice == NEW_CAR_CHOICE:
                MenuOptions.update_data("car", vehicles_list)
                
            elif choice == NEW_TRUCK_CHOICE:
                MenuOptions.update_data("truck", vehicles_list)
                
            elif choice == NEW_SUV_CHOICE:
                MenuOptions.update_data("SUV", vehicles_list)
                
            elif choice == FIND_VEHICLE_CHOICE:
                MenuOptions.find_vehicles_by_make()
                
            elif choice == SHOW_VEHICLES_CHOICE:
                MenuOptions.print_all_vehicles(vehicles_list)
                
            elif choice == CHECK_SPEED_VIOLATION_CHOICE:
                MenuOptions.find_violate_vehicles()
                
            elif choice == QUIT_CHOICE:
                choice = 7
                
            else:
                print("Please, write a choicember from 1 to 7.")
        
            print()
        
        print("Exiting the program...")