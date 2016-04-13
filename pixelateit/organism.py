import random
import helper
from movers.simple_mover import *
from eaters.simple_eater import SimpleEater, CalcEater, AvgEater, SimpleEater2
from eaters.super_simple_eater import SuperSimpleEater
import sys

COLORS = [
        [110,281,40, 255],
        [86,139,142, 255],
        [114,166,160,255],
        [207,219,208,255],
        [240,235,210,255],
        [50, 45, 52, 255],
        [78, 72, 68, 255],
        [44, 50, 49, 255]
    ]

class Organism(object):
    """docstring for Organism"""
    def __init__(self, x, y, px):
        super(Organism, self).__init__()
        self.color = px.lower_grid.get_pixel(x, y)#random.choice(COLORS)
        self.mass = px.stroke #random.randint(1, 10)
        self.x = x
        self.y = y
        self.lower_grid = px.lower_grid
        self.upper_grid = px.upper_grid
        self.speed = 0  # calculated
        self.direction = 0
        class_ = random.choice(px.movers)
        self.mover = getattr(sys.modules[__name__], class_)(self)
        class_ = random.choice(px.eaters)
        self.eater = getattr(sys.modules[__name__], class_)(self)


    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    def get_color(self):
        return self.color

    def set_color(self, r, b, g, a):
        self.color = (r,b,g,a)

    def place_color(self):
        #self.color = random.choice(COLORS)
        self.upper_grid.set_pixel(self.x, self.y, self.color, self.mass)

    def move(self):
        self.mover.move()

    def eat(self):
        self.eater.eat()

    @classmethod
    def generate(cls, num, x, y, px):
        orgs = []
        for z in range(1, num):
            orgs.append(Organism(random.randint(0, x-1), random.randint(0,y-1), px))
        return orgs




