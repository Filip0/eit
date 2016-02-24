from grid import Grid
from organism import Organism
from PIL import Image
import time
from scipy.misc import toimage

EPOCHS = 10

class Pixelateit(object):
    """docstring for Pixelateit"""
    def __init__(self, image_file):
        super(Pixelateit, self).__init__()
        image = Image.open(image_file)

        self.lower_grid = Grid(image)
        self.upper_grid = Grid(image)
        self.lower_grid.load_image(image)
        self.organisms = Organism.generate(500, 1024, 701, self.lower_grid, self.upper_grid)

        print(self.lower_grid.array[0][0])
        print(self.upper_grid.array[0][0])

    def loop(self):
        toimage(self.upper_grid.array).save('first.jpg')
        for x in range(0, EPOCHS):
            for org in self.organisms:
                org.move()
            #time.sleep(1)
            print(self.upper_grid)
        toimage(self.upper_grid.array).save('outfile.jpg')




def main():
    px = Pixelateit("/home/filip/face.jpg")
    px.loop()

if __name__ == "__main__":
    main()
