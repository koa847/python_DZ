from time import sleep

class TrafficLight ():
    __color = {"red": 7, "yellow": 2, "green": 5}

    def running(self):
        x = self.__color
        for k in x.keys():
            if k == "red": c = 31
            if k == "yellow": c = 33
            if k == "green": c = 32
            print(f'\033[{c}m{k}', end='')
            sleep(x[k])
            print("\r", end='')


traffic_light = TrafficLight()
traffic_light.running()
