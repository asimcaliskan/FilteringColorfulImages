from PIL import Image
import numpy as np
from os import getcwd

class GaussianFilter:
  def __init__(self, image_path):
    self.image = np.array(Image.open(image_path), dtype=float)

  def get_gaussian_filter(self, size, sigma):
    x_axis, y_axis = np.mgrid[-size//2 + 1: size//2 + 1, -size//2 + 1: size//2 + 1]
    gaussian_filter = np.exp(-((x_axis**2 + y_axis**2)/(2.0*sigma**2)))
    return gaussian_filter/gaussian_filter.sum()

  def apply_gaussian_filter(self, filter_dimension, sigma, result_path):
    image_width, image_height, image_channel = self.image.shape
    filter = self.get_gaussian_filter(filter_dimension, sigma)
    padding_value = filter_dimension // 2
    for row in range(padding_value, image_height - padding_value):
      for column in range(padding_value, image_width - padding_value):
        for channel in range(image_channel):
          image_part = self.image[row - padding_value: row + padding_value + 1, column - padding_value: column + padding_value + 1, channel]
          self.image[row][column][channel] = np.sum(np.multiply(image_part, filter))
    Image.fromarray(self.image.astype(np.uint8)).save(result_path)


for img in range(5):
  kuwahara = GaussianFilter( getcwd() + "\\src\\images\\img" + str(img) + ".jpg")
  for kernel_dimension in [3, 5, 7, 9]:
    for sigma in [0.5, 1, 1.5, 2]:
      kuwahara.apply_gaussian_filter(kernel_dimension, sigma, getcwd() + "\\src\\gaussian_results\\img" + str(img) + "_" + str(kernel_dimension) + "_" + str(sigma) + ".jpg")
