import numpy as np
from PIL import Image
from helper import add_tuples

class DictGrid(object):
    """docstring for Grid"""
    def __init__(self, image):
        super(DictGrid, self).__init__()
        self.max_x = image.size[1]
        self.max_y = image.size[0]
        self.array = np.zeros([image.size[1], image.size[0], 4], dtype=np.uint8)
        self.dict = {(x, y): self.array[x][y] for x, val in enumerate(self.array) for y, val2 in enumerate(val)}

    def get_pixel(self, x,y):
        #return self.array[x][y]
        return self.dict[(x,y)]

    def set_pixel(self,x,y, value, radius=1):
        for i in range(x-radius, x+radius):
            for j in range(y-radius, y+radius):
                if (0 <= i < self.max_x) and (0 <= j < self.max_y):
                    self.array[i][j] = value

    def add_color(self, x, y, color):
        #self.array[x][y] = add_tuples(self.array[x][y], color)
        self.dict[(x,y)] = add_tuples(self.dict[(x,y)], color)


    def load_image(self, image):
        self.array = np.array(image.getdata(), np.uint8).reshape(image.size[1], image.size[0], 4)
        self.dict = {(x, y): self.array[x][y] for x, val in enumerate(self.array) for y in range(len(val))}

    def __str__(self):
        return str(self.array[0][0])
