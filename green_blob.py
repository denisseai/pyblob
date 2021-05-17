from blob import Blob
import random

class GreenBlob(Blob):
  def __init__(self,x_boundary,y_boundary):
    super().__init__((0,225,0), x_boundary, y_boundary)

  def move(self):
    self.x += random.randrange(-5,6)
    self.y += random.randrange(-5,6)
    if self.stay_within_bounds:
      self.check_bounds()

  def check_bounds(self):
    if self.x < 0: 
      self.x = 0
    elif self.x > self.x_boundary: 
      self.x = self.x_boundary
    
    if self.y < 0: 
      self.y = 0
    elif self.y > self.y_boundary: 
      self.y = self.y_boundary
