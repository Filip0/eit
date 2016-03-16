import movers.mover
import random

MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
SMOVES = [
            [(1, 0), (0, 1), (1, 1)],
            [(-1, 0), (0, 1), (-1, 1)],
            [(1, 0), (0, -1), (1, -1)],
            [(-1, 0), (0, -1), (-1, -1)]
            ]
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


class RandomMover(object):
    """docstring for RandomMover"""
    def __init__(self, organism):
        super(RandomMover, self).__init__()
        self.organism = organism

    def move(self):
        o = self.organism
        o.direction = random.randrange(0, len(MOVES))
        if 0 <= o.x + MOVES[o.direction][0] < len(o.lower_grid.array):
            o.x = o.x + MOVES[o.direction][0]
        if 0 <= o.y + MOVES[o.direction][1] < len(o.lower_grid.array[0]):
            o.y = o.y + MOVES[o.direction][1]


class ZigMover(object):
    """docstring for CircleMover"""
    def __init__(self, organism):
        super(ZigMover, self).__init__()
        self.organism = organism
        
        self.moves = random.choice(SMOVES)

    def move(self):
        o = self.organism
        o.direction = random.randrange(0, len(self.moves))
        if 0 <= o.x + self.moves[o.direction][0] < len(o.lower_grid.array):
            o.x = o.x + self.moves[o.direction][0]
        if 0 <= o.y + self.moves[o.direction][1] < len(o.lower_grid.array[0]):
            o.y = o.y + self.moves[o.direction][1]

class ZagMover(object):
    """docstring for CircleMover"""
    def __init__(self, organism):
        super(ZagMover, self).__init__()
        self.organism = organism
        self.counter = 0
        self.moves = random.choice(SMOVES)

    def move(self):
        self.counter += 1
        if self.counter > 50:
            self.moves = random.choice(SMOVES)
            self.counter = 0
        o = self.organism
        o.direction = random.randrange(0, len(self.moves))
        if 0 <= o.x + self.moves[o.direction][0] < len(o.lower_grid.array):
            o.x = o.x + self.moves[o.direction][0]
        if 0 <= o.y + self.moves[o.direction][1] < len(o.lower_grid.array[0]):
            o.y = o.y + self.moves[o.direction][1]

class CircleMover(object):
    """docstring for CircleMover"""
    def __init__(self, organism):
        super(CircleMover, self).__init__()
        self.organism = organism
        self.radius = random.randint(10,100)
        self.origin_x = organism.x
        self.origin_y = organism.y

    def move(self):
        o = self.organism
        o.direction = random.randrange(0, len(self.moves))
        if 0 <= o.x + self.moves[o.direction][0] < len(o.lower_grid.array):
            o.x = o.x + self.moves[o.direction][0]
        if 0 <= o.y + self.moves[o.direction][1] < len(o.lower_grid.array[0]):
            o.y = o.y + self.moves[o.direction][1]

