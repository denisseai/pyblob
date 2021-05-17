from blob import Blob

class RedBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__((255, 0 , 0), x_boundary, y_boundary)