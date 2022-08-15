import math


class Parameters:
    def __init__(self, side_length):
        self.figure_instance = None
        self.side_length = side_length

    def choose_figure(self, figure_obj):
        self.figure_instance = figure_obj

    def perimeter(self):
        return self.figure_instance.perimeter(self.side_length)

    def area(self):
        return self.figure_instance.area(self.side_length)

    def volume(self):
        return self.figure_instance.volume(self.side_length)


class BaseFigure:
    @staticmethod
    def format_number(n):
        if (n * 100) % 100 == 0:
            return int(n)
        else:
            rounded = round(n, 2)
            return rounded

    def perimeter(self, a):
        pass

    def area(self, a):
        pass

    def volume(self, a):
        return 0


class Circle(BaseFigure):
    def perimeter(self, a):
        c = 2 * math.pi * a
        res = self.format_number(c)
        return res

    def area(self, a):
        s = math.pi * a**2
        res = self.format_number(s)
        return res


class Triangle(BaseFigure):
    def perimeter(self, a):
        p = a * 3
        res = self.format_number(p)
        return res

    def area(self, a):
        s = (a**2 * math.sqrt(3))/4
        res = self.format_number(s)
        return res


class Square(BaseFigure):
    def perimeter(self, a):
        p = a * 4
        res = self.format_number(p)
        return res

    def area(self, a):
        s = a ** 2
        res = self.format_number(s)
        return res


class Pentagon(BaseFigure):
    def perimeter(self, a):
        p = a * 5
        res = self.format_number(p)
        return res

    def area(self, a):
        s = (5 * a**2)/(4 * math.sqrt(5 - 2 * math.sqrt(5)))
        res = self.format_number(s)
        return res


class Hexagon(BaseFigure):
    def perimeter(self, a):
        p = a * 6
        res = self.format_number(p)
        return res

    def area(self, a):
        s = (3 * a**2 * math.sqrt(3)) / 2
        res = self.format_number(s)
        return res


class Cube(BaseFigure):
    def perimeter(self, a):
        p = a * 12
        res = self.format_number(p)
        return res

    def area(self, a):
        s = a * a * 6
        res = self.format_number(s)
        return res

    def volume(self, a):
        v = a ** 3
        res = self.format_number(v)
        return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    # figure.choose_figure(Circle())
    # assert figure.area() == 314.16
    #
    # figure.choose_figure(Triangle())
    # assert figure.perimeter() == 30
    #
    # figure.choose_figure(Square())
    # assert figure.area() == 100
    #
    # figure.choose_figure(Pentagon())
    # assert figure.perimeter() == 50
    #
    # figure.choose_figure(Hexagon())
    # assert figure.perimeter() == 60
    #
    # figure.choose_figure(Cube())
    # assert figure.volume() == 1000

    figure.choose_figure(Pentagon())
    assert figure.area() == 172.05

    print("Coding complete? Let's try tests!")
