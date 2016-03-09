from grid import Grid
from dict_grid import DictGrid
from organism import Organism
from PIL import Image
from scipy.misc import toimage
import os

EPOCHS = 300
ORGAMISMS = 10000


class Pixelateit(object):
    """docstring for Pixelateit"""
    def __init__(self, image_file):
        super(Pixelateit, self).__init__()
        im = Image.open(image_file)
        image = Image.new('RGBA', im.size)
        image.paste(im)

        self.lower_grid = Grid(image)
        #self.upper_grid = DictGrid(image)
        self.upper_grid = Grid(image)
        self.lower_grid.load_image(image)
        self.organisms = Organism.generate(ORGAMISMS, image.size[1], image.size[0], self.lower_grid, self.upper_grid)

    def loop(self):
        toimage(self.upper_grid.array).save('first.jpg')
        for x in range(0, EPOCHS):
            for org in self.organisms:
                org.move()
                org.eat()
            print(x)
        toimage(self.upper_grid.array).save('outfile.png')
        toimage(self.lower_grid.array).save('outfile2.png')


def main():
    px = Pixelateit(os.path.join(os.path.dirname(__file__), 'images/scream.jpg'))
    px.loop()

if __name__ == "__main__":
    main()
