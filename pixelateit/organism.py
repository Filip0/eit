import random
import helper
from movers.simple_mover import *
from eaters.simple_eater import SimpleEater
from eaters.super_simple_eater import SuperSimpleEater

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
    def __init__(self, x, y, lower_grid, upper_grid):
        super(Organism, self).__init__()
        self.color = lower_grid.get_pixel(x, y)#random.choice(COLORS)
        self.mass = random.randint(1, 2)
        self.x = x
        self.y = y
        self.lower_grid = lower_grid
        self.upper_grid = upper_grid
        self.speed = 0  # calculated
        self.direction = 0
        movers = [SimpleMover, ZagMover, ZigMover, RandomMover]
        class_ = random.choice(movers)
        self.mover = class_(self)
        #self.mover = ZagMover(self)
        #self.mover = RandomMover(self)
        self.eater = SuperSimpleEater(self)

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
    def generate(cls, num, x, y, lower_grid, upper_grid):
        orgs = []
        for z in range(1, num):
            orgs.append(Organism(random.randint(0, x-1), random.randint(0,y-1), lower_grid, upper_grid))
        return orgs



