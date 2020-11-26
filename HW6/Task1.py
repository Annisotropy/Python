import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            print('red')
            self.__color = 'red'
            time.sleep(7)
            print('yellow')
            self.__color = 'yellow'
            time.sleep(2)
            print('green')
            self.__color = 'green'
            time.sleep(4)


light = TrafficLight()
light.running()

