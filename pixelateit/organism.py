import random
import helper
from movers.simple_mover import SimpleMover
from eaters.simple_eater import SimpleEater



class Organism(object):
    """docstring for Organism"""
    def __init__(self, x, y, lower_grid, upper_grid):
        super(Organism, self).__init__()
        self.color = (0, 0, 0, 0)
        self.mass = random.randint(1, 2)
        self.x = x
        self.y = y
        self.lower_grid = lower_grid
        self.upper_grid = upper_grid
        self.speed = 0  # calculated
        self.direction = 0
        self.mover = SimpleMover(self)
        self.eater = SimpleEater(self)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    def get_color(self):
        return self.color

    def set_color(self, r, b, g, a):
        self.color = (r,b,g,a)

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



