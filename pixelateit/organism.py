class Organism(object):
    """docstring for Organism"""
    def __init__(self, arg):
        super(Organism, self).__init__()
        self.color = (0,0,0,0)
        self.mass = 0
        self.x = 0
        self.y = 0
        self.speed = 0 # calculated

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return (x,y)

    def get_color(self):
        return self.color
#test
    def set_color(r,b,g,a):
        self.color = (r,b,g,a)



