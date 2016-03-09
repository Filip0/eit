class SuperSimpleEater(object):
    """docstring for SuperSimpleEater"""
    def __init__(self, organism):
        super(SuperSimpleEater, self).__init__()
        self.organism = organism

    def eat(self):
        self.organism.place_color()
