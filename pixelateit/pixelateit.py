from grid import Grid
from organism import Organism
from PIL import Image
from scipy.misc import toimage

EPOCHS = 200

class Pixelateit(object):
    """docstring for Pixelateit"""
    def __init__(self, image_file):
        super(Pixelateit, self).__init__()
        im = Image.open(image_file)
        image = Image.new('RGBA', im.size)
        image.paste(im)

        self.lower_grid = Grid(image)
        self.upper_grid = Grid(image)
        self.lower_grid.load_image(image)
        self.organisms = Organism.generate(10000, 701, 1024, self.lower_grid, self.upper_grid)

    def loop(self):
        toimage(self.upper_grid.array).save('first.jpg')
        for x in range(0, EPOCHS):
            for org in self.organisms:
                org.move()
            print(x)
        toimage(self.upper_grid.array).save('outfile.jpg')




def main():
    px = Pixelateit("/home/filip/face.jpg")
    px.loop()

if __name__ == "__main__":
    main()
