from Vehicles.car import Car
from Vehicles.truck import Truck
from Vehicles.SUV import SUV

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