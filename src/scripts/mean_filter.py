from PIL import Image
import numpy as np
from os import getcwd

class MeanFilter:
  def __init__(self, image_path):
    self.image = np.array(Image.open(image_path), dtype=float)

  def apply_mean_filter(self, filter_dimension, result_path):
    image_width, image_height, image_channel = self.image.shape
    padding_value = filter_dimension // 2
    for row in range(padding_value, image_width - padding_value):
      for column in range(padding_value, image_height - padding_value):
        for channel in range(image_channel):
          image_part = self.image[row - padding_value: row + padding_value + 1, column - padding_value: column + padding_value + 1, channel]
          self.image[row][column][channel] = np.mean(image_part)
   
    Image.fromarray(self.image.astype(np.uint8)).save(result_path)

for img in range(5):
  kuwahara = MeanFilter( getcwd() + "\\src\\images\\img" + str(img) + ".jpg")
  for kernel_dimension in [3, 5, 7, 9]:
    kuwahara.apply_mean_filter(5, getcwd() + "\\src\\mean_results\\img" + str(img) + "_" + str(kernel_dimension) + ".jpg")

