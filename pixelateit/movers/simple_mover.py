import movers.mover
import random

MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

class SimpleMover(object):
    """docstring for SimpleMover"""
    def __init__(self, organism):
        super(SimpleMover, self).__init__()
        self.organism = organism

    def move(self):
        o = self.organism
        o.direction = (o.direction+random.randrange(-1, 2)) % len(MOVES)
        if 0 <= o.x + MOVES[o.direction][0] < len(o.lower_grid.array):
            o.x = o.x + MOVES[o.direction][0]
        if 0 <= o.y + MOVES[o.direction][1] < len(o.lower_grid.array[0]):
            o.y = o.y + MOVES[o.direction][1]

