from grid import Grid
from dict_grid import DictGrid
from organism import Organism
from PIL import Image
from scipy.misc import toimage
from gui import Window
import os

EPOCHS = 1000
ORGAMISMS = 1000


class Pixelateit(object):
    """docstring for Pixelateit"""
    def __init__(self):
        super(Pixelateit, self).__init__()
        self.image_loaded = False
        self.lower_grid = None
        self.upper_grid = None
        self.gui = Window(self)


    def load_image(self, image_file):
        print(image_file)
        im = Image.open(image_file)
        image = Image.new('RGBA', im.size)
        image.paste(im)


        self.lower_grid = Grid(image)
        self.upper_grid = Grid(image)
        self.lower_grid.load_image(image)
        #self.organisms = Organism.generate(self.gui.organisms, image.size[1], image.size[0], self)
        self.image_loaded = True

    def start(self, movers, eaters):
        self.eaters = eaters
        self.movers = movers
        self.organisms = Organism.generate(self.gui.organisms, self.lower_grid.max_x, self.lower_grid.max_y, self)

    def loop(self):
        toimage(self.upper_grid.array).save('first.jpg')
        for x in range(0, EPOCHS):
            for org in self.organisms:
                org.move()
                org.eat()
            print(x)
            #if x % 10 == 0:
            #    toimage(self.upper_grid.array).save('out/outfile{}.png'.format(x))
        toimage(self.upper_grid.array).save('outfile.png')
        toimage(self.lower_grid.array).save('outfile2.png')

    def update(self):
        for org in self.organisms:
            org.move()
            org.eat()

    def save_image(self, name):
        path = os.path.join(os.path.dirname(__file__), name)
        print(name)
        toimage(self.upper_grid.array).save(name)
        return path


def main():
    px = Pixelateit()
    px.gui.run()

if __name__ == "__main__":
    main()
