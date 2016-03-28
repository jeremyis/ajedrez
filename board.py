import window
import piece
from config import CONFIG

BLACK = 'black'
WHITE = 'white'

class Board:
  def __init__(self):
    self.spaces = [range(CONFIG.BOARD_HEIGHT) for x in range(CONFIG.BOARD_WIDTH)]

  def get_pixels(self, i):
    return i*CONFIG.SQUARE_SIZE

  def flip_color(self, color):
    (light, dark) = (CONFIG.BOARD_LIGHT_COLOR, CONFIG.BOARD_DARK_COLOR)
    return dark if color is light else light

  def draw(self):
    color = CONFIG.BOARD_LIGHT_COLOR
    for row in range(0, CONFIG.BOARD_HEIGHT):
      for col in range(0, CONFIG.BOARD_WIDTH):
        space = self.draw_space(row, col, color)
        color = self.flip_color(color)

        # TODO: better piece placement.
      color = self.flip_color(color)

    self.place_pieces()

  def draw_space(self, x, y, color):
    space = Space(x, y, color)
    space.draw()
    self.spaces[x][y] = space
    return space

  def place_pieces(self):
    for p in CONFIG.PIECES:
      new = piece.create(p[0], p[1])
      new.draw()
      self.get_space_from_notation(p[2]).place_piece(new)

  def get_space_at_pixels(self, x, y):
    (x, y) = (x / CONFIG.SQUARE_SIZE, y / CONFIG.SQUARE_SIZE)
    return self.spaces[x][y]

  def get_space_from_notation(self, notation):
    # a1 -> 0, 7; h8 -> 7, 0
    if notation == None or len(notation) < 2:
      raise Exception("Invalid notation: %s" % notation)
    letter = notation[:1]
    x = (ord(letter) - 96) - 1
    y = CONFIG.BOARD_HEIGHT - int(notation[1:len(notation)])
    return self.spaces[x][y]


class Space:
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    self.piece = None

  def get_pixels(self):
    return (self.x*CONFIG.SQUARE_SIZE, self.y*CONFIG.SQUARE_SIZE)

  def get_piece_center_pixels(self):
    (x, y) = self.get_pixels()
    return (x + CONFIG.SQUARE_SIZE/2, y + CONFIG.SQUARE_SIZE/2)

  def draw(self):
    (x0, y0) = self.get_pixels()
    window.draw_rectangle(x0, y0, (x0 + CONFIG.SQUARE_SIZE), (y0 + CONFIG.SQUARE_SIZE), self.color)

  def place_piece(self, piece):
    if self.has_piece():
      raise Exception("A space can only have one piece.")
    self.piece = piece
    (x, y) = self.get_piece_center_pixels()
    piece.place(x, y)

  def move_piece_here(self, piece, from_space):
    if self.has_piece():
      raise Exception("A space can only have one piece.")
    self.piece = piece
    from_space.remove_piece()
    (x, y) = self.get_piece_center_pixels()
    piece.move(x, y)

  def has_piece(self):
    return self.piece != None

  def get_piece(self):
    return self.piece

  def remove_piece(self):
    self.piece = None

  # Positive is to the right, negative to the left. Inclusive of final space.
  def get_horizontal_distance_to(self, dest_space):
    return dest_space.x - self.x

  # Positive is up, negative down (note: opposite of y coordinates). Inclusive of final space.
  def get_vertical_distance_to(self, dest_space):
    return -1*(dest_space.y - self.y)

# TODO: move to Game class.

"""
def callback(event):
    print "clicked at", event.x, event.y

canvas.bind("<Button-1>", callback)
"""

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#window.bind('<Motion>', motion)
