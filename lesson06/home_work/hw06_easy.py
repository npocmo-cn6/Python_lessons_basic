import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, first: object, second: object, third: object) -> object:
        self.first = {'x': int(first.split(',')[0]),
                      'y': int(first.split(',')[1])}
        self.second = {'x': int(second.split(',')[0]),
                       'y': int(second.split(',')[1])}
        self.third = {'x': int(third.split(',')[0]),
                      'y': int(third.split(',')[1])}
        self.a = math.hypot(self.second['x'] - self.first['x'], self.second['y'] - self.first['y'])
        self.b = math.hypot(self.second['x'] - self.third['x'], self.second['y'] - self.third['y'])
        self.c = math.hypot(self.first['x'] - self.third['x'], self.first['y'] - self.third['y'])

    @property
    def calc_perimeter(self):
        return math.fabs(self.a) + math.fabs(self.b) + math.fabs(self.c)

    @property
    def calc_height(self):
        p = self.calc_perimeter / 2
        return (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a

    @property
    def calc_square(self):
        s = 0.5 * self.a * self.calc_height
        return math.fabs(s)


t = Triangle('1,1', '3,4', '4,1')
print(t.calc_perimeter)
print(t.calc_height)
print(t.calc_square)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium:
    def __init__(self, first: object, second: object, third: object, four: object) -> object:
        self.first = {'x': int(first.split(',')[0]),
                      'y': int(first.split(',')[1])}
        self.second = {'x': int(second.split(',')[0]),
                       'y': int(second.split(',')[1])}
        self.third = {'x': int(third.split(',')[0]),
                      'y': int(third.split(',')[1])}
        self.four = {'x': int(four.split(',')[0]),
                     'y': int(four.split(',')[1])}
        self.ab = math.hypot(self.first['x'] - self.second['x'], self.first['y'] - self.second['y'])
        self.cd = math.hypot(self.third['x'] - self.four['x'], self.third['y'] - self.four['y'])
        self.ac = math.hypot(self.first['x'] - self.third['x'], self.first['y'] - self.third['y'])
        self.db = math.hypot(self.four['x'] - self.second['x'], self.four['y'] - self.second['y'])
        self.h = math.sqrt(math.fabs((self.ac * self.ac) - (
                    ((self.ab - self.cd) * (self.ab - self.cd)) + (self.ac * self.ac) - (self.db * self.db) / (
                        2 * (self.ab - self.cd)))))
        self.ad = math.sqrt((self.ab * self.ab) + (self.db * self.db))
        self.cb = math.sqrt((self.ac * self.ac) + (self.ab * self.ab))
    @property
    def get_type(self):
        if self.ad == self.cb:
            return True
        else:
            return False

    @property
    def calc_square(self):
        return ((self.ab + self.cd) / 2) * self.h

    @property
    def get_sides_lenght(self):
        return {'ab': self.ab, 'cd': self.cd, 'ac': self.ac, 'db': self.db}

    @property
    def calc_perimeter(self):
        return math.fabs(self.ab) + math.fabs(self.cd) + math.fabs(self.ac) + math.fabs(self.db)


def t_func(t):
    if t.get_type:
        print('Trapezium is isosceles')
    else:
        print('Trapezium is not isosceles')
    print('Trapezium square: ', t.calc_square)
    print('Trapezium sides: ', t.get_sides_lenght)
    print('Trapezium perimeter: ', t.calc_perimeter)

t = Trapezium('3,2', '5,2', '9,6', '6,6')
t_func(t)
t = Trapezium('2,4', '2,5', '0,2', '0,7')
t_func(t)