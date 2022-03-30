# 4. Определите новый класс speedTicket, который должен содержать информацию о превышении скорости, например. номер автомобиля, время, скорость и ограничение скорости.

class SpeedTicket():
    def __init__(self, reg_num, time, car_speed, speed_limit):
        self.reg_num = reg_num
        self.time = time
        self.car_speed = car_speed
        self.speed_limit = speed_limit

    # def is_allowed_speed(self):
    #     return self.car_speed <= 1.05 * self.get_speed_limit

    def __str__(self):
        return(f"Here is the speed_limit ticket:"
            f"\n\tRegistration number: {self.reg_num}."
            f"\n\tTime: {self.time}."
            f"\n\tCar speed: {self.car_speed}."
            f"\n\tSpeed limt: {self.speed_limit}.")