import numpy as np
from PIL import Image

class Grid(object):
    """docstring for Grid"""
    def __init__(self, image, upper=False):
        super(Grid, self).__init__()
        if upper:
            self.array = np.zeros([image.size[1], image.size[0], 3], dtype=np.uint8)
        else:
            self.load_image(image)

    def get_pixel(x,y):
        return self.array[x][y]

    def set_pixel(x,y, value):
        self.array[x][y] = value

    def load_image(self, image):
        self.array = np.array(image.getdata(), np.uint8).reshape(image.size[1], image.size[0], 3)
