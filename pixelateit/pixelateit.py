from grid import Grid
from PIL import Image

EPOCHS = 10

class Pixelateit(object):
    """docstring for Pixelateit"""
    def __init__(self, image_file):
        super(Pixelateit, self).__init__()
        image = Image.open(image_file)

        self.lower_grid = Grid(image)
        self.upper_grid = Grid(image, upper=True)
        self.organisms = []

        print(self.lower_grid.array[0][0])
        print(self.upper_grid.array[0][0])

    def loop(self):
        for x in range(0, EPOCHS):
            print(x)




def main():
    px = Pixelateit("/home/filip/face.png")
    px.loop()

if __name__ == "__main__":
    main()
