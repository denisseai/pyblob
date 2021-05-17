from blob import Blob
import pygame

class BlackBlob(Blob):
  def __init__(self,x_boundary,y_boundary):
    super().__init__((0,0,0), x_boundary, y_boundary)

  def move(self):
    index = pygame.mouse.get_pos()
    self.x += index[0]
    self.y += index[1]

    if index[0] != self.x and index[1] != self.y:
      new_blob = pygame.mouse.get_rel()
      self.x = new_blob[0]
      self.y = new_blob[1]

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
