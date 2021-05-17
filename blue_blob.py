from blob import Blob
import random

class BlueBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__((0, 0, 225), x_boundary, y_boundary)
  
  def move(self):
    self.x += random.randrange(-5,6)
    self.y += random.randrange(-5,6)
    if self.stay_within_bounds:
      self.check_bounds()