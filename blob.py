import random
import pygame 
import numpy as np

class Blob:
    
  def __init__(self, color, x_boundary, y_boundary, size_range=(4,8), movement_range=(-1,2), stay_within_bounds=True):
    self.x_boundary = x_boundary
    self.y_boundary = y_boundary
    self.x = random.randrange(0, self.x_boundary)
    self.y = random.randrange(0, self.y_boundary)
    self.size = random.randrange(size_range[0], size_range[1])
    self.color = color
    self.movement_range = movement_range
    self.stay_within_bounds = stay_within_bounds

  def __add__(self, other_blob):
    if other_blob.color == (255, 0, 0):
        self.size -= other_blob.size
        other_blob.size -= self.size
        
    elif other_blob.color == (0, 255, 0):
        self.size += other_blob.size
        other_blob.size += 1
        
    elif other_blob.color == (0, 0, 255):
        pass
    else:
      other_blob.color = list(np.random.choice(range(256), size=3))
      other_blob.size += 1

  def move(self):
    self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
    self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
    self.x += self.move_x
    self.y += self.move_y
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

  def draw(self, game_display):
    pygame.draw.circle(game_display, self.color, [self.x, self.y], self.size)