import pickle

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