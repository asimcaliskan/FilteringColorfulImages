from PIL import Image
import numpy as np
from os import getcwd

IMAGE_PATH = getcwd() + "\\src\\images\\apples.jpg"
FILTER_SIZE = 3 #It can be 3, 5, 7, 9
PADDING_VALUE = FILTER_SIZE // 2 #PLEASE DON'T CHANGE IT!

input_image = Image.open(IMAGE_PATH)
input_image = np.array(input_image)
input_image = np.pad(input_image, pad_width=[(PADDING_VALUE, PADDING_VALUE), (PADDING_VALUE, PADDING_VALUE), (0, 0)], mode="constant")

def mean_filter(image):
  width, height, channels = image.shape
  for row in range(PADDING_VALUE, height - PADDING_VALUE):
    for column in range(PADDING_VALUE, width - PADDING_VALUE):
      mean_of_3_channel = np.mean(image[row - PADDING_VALUE : row + PADDING_VALUE + 1, column - PADDING_VALUE : column + PADDING_VALUE + 1], axis=(0, 1)) 
      image[row - PADDING_VALUE : row + PADDING_VALUE + 1, column - PADDING_VALUE : column + PADDING_VALUE + 1] = mean_of_3_channel

mean_filter(input_image)
width, height, channels = input_image.shape
result_image = Image.fromarray(input_image[PADDING_VALUE: width - PADDING_VALUE, PADDING_VALUE: height - PADDING_VALUE])
result_image.show()