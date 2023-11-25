import math


class Punto:
    def __int__(self, x, y):
        #atri
        self.x_axis = x
        self.y_axis = y

    def __str__(self):
        return str((self.x_axis, self.y_axis))

    def distance(self, p2):
        delta_x = (p2.x_axis - self.x_axis)
        delta_y = (p2.y_axis - self.y_axis)
        return math.sqrt(delta_x ** 2 + delta_y ** 2)


def main():
    p1 = Punto(3.5, 4.6)
    print(p1)
    print(p1.distance(Punto(1.2, 1.4)))
    print(p1.x_axis, p1.y_axis)


main()
