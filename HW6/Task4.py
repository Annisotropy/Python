class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Car starts')

    def stop(self):
        print('Car stops')

    def turn(self, direction):
        if direction.lower() == 'left':
            print('Car turns left')
        else:
            print('Car turns right')

    def show_speed(self):
        print(f'Speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 60:
            print('Speed exceeded')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 40:
            print('Speed exceeded')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


Audi = Car(80, 'red', 'Audi')
print(Audi.name)
Audi.show_speed()
print(Audi.is_police)
Audi.go()
Audi.turn('right')
Audi.stop()

print('-----------------')

Renault = TownCar(90, 'blue', 'Renault')
print(Renault.name)
print(Renault.color)
Renault.show_speed()
print(Renault.is_police)
Renault.go()
Renault.turn('left')
Renault.stop()

print('-----------------')

Volga = PoliceCar(110, 'black', 'Volga')
print(Volga.name)
print(Volga.color)
Volga.show_speed()
print(Volga.is_police)
Volga.go()
Volga.turn('left')
Volga.stop()
