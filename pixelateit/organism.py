import random
import helper

class Organism(object):
    """docstring for Organism"""
    def __init__(self, x, y, lower_grid, upper_grid):
        super(Organism, self).__init__()
        self.color = (0,0,0,0)
        self.mass = 0
        self.x = x
        self.y = y
        self.lower_grid = lower_grid
        self.upper_grid = upper_grid
        self.speed = 0 # calculated

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
        t = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        temp = t[random.randint(0,8)]
        if 0 <= self.x + temp[0] < len(self.lower_grid.array):
            self.x = self.x + temp[0]
        if 0 <= self.y + temp[1] < len(self.lower_grid.array):
            self.y = self.y + temp[1]
        self.eat()

    def eat(self):
        lower_grid_color = self.lower_grid.get_pixel(self.x, self.y)
        eaten_color = tuple(x*0.3 for x in lower_grid_color)
        self.color = helper.add_tuples(self.color, eaten_color)
        self.lower_grid.set_pixel(self.x, self.y, helper.subtract_tuples(lower_grid_color, eaten_color))
        upper_grid_color = self.upper_grid.get_pixel(self.x, self.y)
        remaining_color = tuple(x*0.7 for x in self.color)
        self.upper_grid.set_pixel(self.x, self.y, self.color)
        self.color = remaining_color
        print("Eat grid {} {}".format(self.x, self.y))

    @classmethod
    def generate(cls, num, x, y, lower_grid, upper_grid):
        orgs = []
        for z in range(1, num):
            orgs.append(Organism(random.randint(0, x-1), random.randint(0,y-1), lower_grid, upper_grid))
        return orgs



