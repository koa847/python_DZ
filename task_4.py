class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        msg = f'автомобиль {self.name} поехал'
        if self.speed == 0:
            self.speed = 40
        return msg
    def stop(self):
        msg = f'автомобиль {self.name} остановился'
        self.speed = 0
        return msg
    def turn(self, direction):
        if self.speed != 0:
            msg = f'автомобиль {self.name} повернул на {direction}'
        else: msg = f"автомобиль {self.name} не движется, поэтому не может поварачивать"
        return msg
    def show_speed (self):
        msg = f'автомобиль {self.name} движется со коростью: {self.speed} км/ч'
        print(msg)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Привышение скорости!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Привышение скорости!")

class PoliceCar (Car):
    pass

if __name__ == "__main__":
    car_1 = TownCar(70, "red", "Mazda", False)
    car_2 = SportCar(70, "blue", "BMW", False)

    car_1.show_speed()
    car_2.show_speed()
    print(car_1.stop())
    car_1.show_speed()
    print(car_1.turn("лево"))
    print(car_2.turn("право"))
    print(car_1.color)
    car_1.go()
    car_1.show_speed()
    car_1.speed = 70
    car_1.show_speed()