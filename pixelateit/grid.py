import numpy as np
from PIL import Image

class Grid(object):
    """docstring for Grid"""
    def __init__(self, image):
        super(Grid, self).__init__()
        print(image.size[1])
        print(image.size[0])
        print(len(image.getdata()))
        self.array = np.zeros([image.size[1], image.size[0], 3], dtype=np.uint8)

    def get_pixel(self, x,y):
        return self.array[x][y]

    def set_pixel(self,x,y, value):
        self.array[x][y] = value

    def load_image(self, image):
        self.array = np.array(image.getdata(), np.uint8).reshape(image.size[1], image.size[0], 3)

    def __str__(self):
        return str(self.array[0][0])
