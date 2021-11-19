from PIL import Image
import numpy as np
from os import getcwd
from cv2 import GaussianBlur

IMAGE_PATH = getcwd() + "\\src\\images\\apples.jpg"
FILTER_SIZE = (9, 9)
SIGMA = 10.

input_image = Image.open(IMAGE_PATH)
input_image = np.array(input_image)
input_image = GaussianBlur(input_image, FILTER_SIZE, SIGMA)
result_image = Image.fromarray(input_image)
result_image.show()

