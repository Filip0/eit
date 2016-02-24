import random
import helper

MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

class Organism(object):
    """docstring for Organism"""
    def __init__(self, x, y, lower_grid, upper_grid):
        super(Organism, self).__init__()
        self.color = (0,0,0,0)
        self.mass = 1#random.randint(0, 2)
        self.x = x
        self.y = y
        self.lower_grid = lower_grid
        self.upper_grid = upper_grid
        self.speed = 0 # calculated
        self.direction = random.randint(0, len(MOVES))

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
        self.direction = (self.direction+random.randrange(-1,2))%len(MOVES)
        if 0 <= self.x + MOVES[self.direction][0] < len(self.lower_grid.array):
            self.x = self.x + MOVES[self.direction][0]
        if 0 <= self.y + MOVES[self.direction][1] < len(self.lower_grid.array[0]):
            self.y = self.y + MOVES[self.direction][1]
        self.eat()

    def eat(self):
        lower_grid_color = self.lower_grid.get_pixel(self.x, self.y)
        eaten_color = tuple(x*0.3 for x in lower_grid_color)
        self.color = helper.add_tuples(self.color, eaten_color)
        self.lower_grid.set_pixel(self.x, self.y, helper.subtract_tuples(lower_grid_color, eaten_color))
        upper_grid_color = self.upper_grid.get_pixel(self.x, self.y)
        placing_color = tuple(x*1 for x in self.color)
        #remaining_color = tuple(x*0.8 for x in self.color)
        self.upper_grid.set_pixel(self.x, self.y, placing_color, self.mass)
        self.color = helper.subtract_tuples(self.color, placing_color)
        #print("Eat grid {} {}".format(self.x, self.y))

    @classmethod
    def generate(cls, num, x, y, lower_grid, upper_grid):
        orgs = []
        for z in range(1, num):
            orgs.append(Organism(random.randint(0, x-1), random.randint(0,y-1), lower_grid, upper_grid))
        return orgs



