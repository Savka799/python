class Transport():
    n = 0
    def __init__(self, color='black'):
        self.color=color
        Transport.n += 1

    def motion(self,g):
        self.vel = g
        print('я, кажется, двигаюсь', self.vel, sep=' ')

    def stop(self):
        print('я не двигаюсь')

car = Transport()
car.motion(50)
car.stop()
train = Transport('green')
train.motion(100)
print(Transport.n)
print(train.color)