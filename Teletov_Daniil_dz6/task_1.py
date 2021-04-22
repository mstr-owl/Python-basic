from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = "Green"

    def __str__(self):
        return self.__color

    def run(self, switch=60):
        try:
            while switch:
                self.show_trafficlight()
                self.switch_light()
                switch -= 1
        except ValueError:
            print("Traffic lights do not work")

    def switch_light(self):
        if self.__color == "Green":
            sleep(10)
            self.__color = "Yellow"
        elif self.__color == "Yellow":
            sleep(2)
            self.__color = "Red"
        elif self.__color == "Red":
            sleep(7)
            self.__color = "Green"
        else:
            raise ValueError

    def show_trafficlight(self):
        print(self)


Tra_li = TrafficLight()
Tra_li.run()
