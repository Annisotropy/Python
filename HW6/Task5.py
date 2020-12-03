class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Pen is on')


class Pencil(Stationery):
    def draw(self):
        print('Pencil is active')


class Handle(Stationery):
    def draw(self):
        print('Handle is ready')


handle_1 = Stationery('Handle')
handle_1.draw()

print('-----------------------')

handle_2 = Handle('Handle Red')
print(handle_2.title)
handle_2.draw()

print('-----------------------')

pen = Pen('Pen Green')
print(pen.title)
pen.draw()