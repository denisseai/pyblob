import pygame
import random
import math
import numpy as np
from blue_blob import BlueBlob
from red_blob import RedBlob
from green_blob import GreenBlob
from black_blob import BlackBlob

#constants
WIDTH = 400
HEIGHT = 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
RED = (255, 0 , 0)
STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 5
STARTING_BLACK_BLOBS = 5
# COLORS = [(139, 0, 0), 
#           (0, 100, 0),
#           (0, 0, 139)]

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def is_touching(b1, b2):
  # return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)
  return math.sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2) < (b1.size + b2.size)
  print(math.sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2) < (b1.size + b2.size))

def handle_collisions(blob_list):
  blues,reds,greens,blacks = blob_list
  for blue_id, blue_blob in blues.copy().items():
    for other_blobs in blues, reds, greens, blacks:
      for other_blob_id, other_blob in other_blobs.copy().items():
        if blue_blob == other_blob:
          pass
        else:
          if is_touching(blue_blob, other_blob):
            blue_blob + other_blob
            if other_blob.size <= 0:
              del other_blobs[other_blob_id]
            if blue_blob.size <= 0:
              del blues[blue_id]
                          
  return blues,reds,greens,blacks
  
def draw_environment(blob_list):
  game_display.fill(WHITE)
  blues,reds,greens,blacks = handle_collisions(blob_list)
  for blob_dict in blob_list:
    for blob_id in blob_dict:
      blob = blob_dict[blob_id]
      blob.draw(game_display)
      blob.move()
  pygame.display.update()
  return blues, reds, greens, blacks

def main():
  blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
  red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
  green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
  black_blobs = dict(enumerate([BlackBlob(WIDTH,HEIGHT) for i in range(STARTING_BLACK_BLOBS)]))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    blue_blobs,red_blobs,green_blobs,black_blobs = draw_environment([blue_blobs,red_blobs,green_blobs,black_blobs])
    clock.tick(60)

if __name__ == '__main__':
	main()
