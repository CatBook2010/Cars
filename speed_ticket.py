""# 4. Определите новый класс SpeedTicket, который должен содержать информацию о превышении скорости, например. номер автомобиля, время, скорость и ограничение скорости.

class SpeedTicket():
    def __init__(self, reg_num, time, speed, speed_limit):
        self.reg_num = reg_num
        self.time = time
        self.speed = speed
        self.speed_limit = speed_limit

    def __str__(self):
        return(f" Here is the speed ticket:"
            f"Registration number: {self.reg_num}."
            f"Time: {self.time}."
            f"Speed: {self.speed}."
            f"Speed limit: {self.speed_limit}.")