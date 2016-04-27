import helper
import numpy as np
import random

class ObscureEater(object):
    """docstring for SimpleEater"""
    def __init__(self, organism):
        super(ObscureEater, self).__init__()
        self.organism = organism

    def eat(self):
        o = self.organism
        lower_grid_color = o.lower_grid.get_pixel(o.x, o.y)
        eaten_color = lower_grid_color*0.3
        o.color = np.add(o.color, eaten_color)
        o.lower_grid.set_pixel(o.x, o.y, lower_grid_color*0.7)

        placing_color = o.color*0.9
        remove_color = o.color*0.3
        placing_color[3] = 255#*random.uniform(0.7,1)
        # Better place color function, some areas will get no color and some full color (black/white)
        # Maybe use 

        if bool(random.getrandbits(1)):
            o.upper_grid.set_color(o.x, o.y, placing_color)
        else:
            o.upper_grid.add_color(o.x, o.y, placing_color)
        o.color = np.subtract(o.color, remove_color)

class SimpleEater(object):
    """docstring for SimpleEater"""
    def __init__(self, organism):
        super(SimpleEater, self).__init__()
        self.organism = organism

    def eat(self):
        o = self.organism
        lower_grid_color = o.lower_grid.get_pixel(o.x, o.y)
        eaten_color = lower_grid_color*0.05
        color = o.color*0.95
        o.color = np.add(color, eaten_color)

        o.place_color()

class CalcEater(object):
    """docstring for CalcEater"""
    def __init__(self, organism):
        super(CalcEater, self).__init__()
        self.organism = organism

    def eat(self):
        o = self.organism
        lower_grid_color = o.lower_grid.get_pixel(o.x, o.y)

        o.color = list(map(lambda x: (x*x)%255, lower_grid_color))
        o.color[3] = 255

        o.place_color()

class AvgEater(object):
    """docstring for AvgEater"""
    def __init__(self, organism):
        super(AvgEater, self).__init__()
        self.organism = organism

    def eat(self):
        o = self.organism
        lower_grid_color = o.lower_grid.get_pixel(o.x, o.y)

        o.color = (o.color+lower_grid_color)/2
        o.color[3] = 255

        o.place_color()





