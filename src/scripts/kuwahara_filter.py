from PIL import Image
import numpy as np
from os import getcwd
from cv2 import GaussianBlur

IMAGE_PATH = getcwd() + "\\src\\images\\rose.jpeg"

class KuwaharaFilter:
  def __init__(self, image_path):
    self.RGB_image = np.array(Image.open(image_path), dtype=float)
    self.HSV_image = np.array(Image.open(image_path).convert("HSV"), dtype=float)

  
  def apply_kuwahara_filter(self, filter_dimension):
    image_width, image_height, image_channel = self.HSV_image.shape
    padding_value = filter_dimension // 2
    for row in range(padding_value, image_width - padding_value):
      for column in range(padding_value, image_height - padding_value):
        image_part = self.HSV_image[row - padding_value: row + padding_value + 1, column - padding_value: column + padding_value + 1, 2]
        self.filter_operation(image_part, row, column)

    Image.fromarray(self.RGB_image.astype(np.uint8)).show()


  def filter_operation(self, image_part, row, column):
    width, height = image_part.shape
    Q1 = image_part[0: height // 2 + 1, width // 2: width]
    Q2 = image_part[0: height // 2 + 1, 0: width // 2 + 1]
    Q3 = image_part[height // 2: height, 0: width // 2 + 1]
    Q4 = image_part[height // 2: height, width // 2: width]
    stds  = np.array([np.std(Q1), np.std(Q2), np.std(Q3), np.std(Q4)])
    min_std = stds.argmin()

    if min_std == 0:
      self.update_image(row, column, row - height // 2,  row + 1, column, column + width // 2 + 1)

    elif min_std == 1:
      self.update_image(row, column,row - height // 2, row + 1, column - width // 2, column + 1)

    elif min_std == 2:
      self.update_image(row, column, row, row + height // 2 + 1, column - width // 2, column + 1)

    elif min_std == 3:
      self.update_image(row, column, row, row + height // 2 + 1, column, column + height // 2 + 1)

  def update_image(self, row, column, row_start, row_end, column_start, column_end):
    self.RGB_image[row][column][0] = np.mean(self.RGB_image[row_start : row_end, column_start : column_end, 0])
    self.RGB_image[row][column][1] = np.mean(self.RGB_image[row_start : row_end, column_start : column_end, 1])
    self.RGB_image[row][column][2] = np.mean(self.RGB_image[row_start : row_end, column_start : column_end, 2])

kuwahara = KuwaharaFilter(IMAGE_PATH)
kuwahara.apply_kuwahara_filter(3)