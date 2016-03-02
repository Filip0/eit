import helper
import numpy as np

class SimpleEater(object):
    """docstring for SimpleEater"""
    def __init__(self, organism):
        super(SimpleEater, self).__init__()
        self.organism = organism

    def eat(self):
        o = self.organism
        lower_grid_color = o.lower_grid.get_pixel(o.x, o.y)
        eaten_color = lower_grid_color*0.3
        o.color = np.add(o.color, eaten_color)
        o.lower_grid.set_pixel(o.x, o.y, lower_grid_color*0.9)

        placing_color = o.color*0.6
        remove_color = o.color*0.7
        placing_color[3] = 255
        o.upper_grid.add_color(o.x, o.y, placing_color)
        o.color = np.subtract(o.color, remove_color)





