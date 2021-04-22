class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return f"{self.name} went"

    def stop(self):
        return f"{self.name} stopped"

    def turn_right(self):
        return f"{self.name} turn right"

    def turn_left(self):
        return f"{self.name} turn left"

    def show_speed(self):
        return f"Speed of your car {self.name}: {self.speed} km/h"


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f"Speed of your car {self.name}: {self.speed} km/h. You are exceeding the speed limit!"
        else:
            return f"Speed of your car {self.name}: {self.speed} km/h"


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return f"Speed of your car {self.name}: {self.speed} km/h. You are exceeding the speed limit!"
        else:
            return f"Speed of your car {self.name}: {self.speed} km/h"


class PoliceCar(Car):
    is_police = True
    pass


class SportCar(Car):
    pass


land_rover = TownCar(90, "Black", "Land_Rover_Discovery_4",)
print(f'1:{land_rover.go()}, {land_rover.show_speed()}, {land_rover.turn_right()}, {land_rover.is_police}')
print()

kamaz = WorkCar(20, "Orange", "Kamaz_65207")
print(f'2:{kamaz.go()}, {kamaz.show_speed()}, {kamaz.stop()}, {kamaz.is_police}')
print()

police = PoliceCar(95, "Blue", "Dodge_Charger")
print(f'3:{police.go()}, {police.show_speed()}, {police.turn_left()}, {police.is_police}')
print()

lamborghini = SportCar(250, "Yellow", "Lamborghini_Aventador_S")
print(f'4:{lamborghini.go()}, {lamborghini.show_speed()}, {lamborghini.stop()}, {lamborghini.is_police}')
