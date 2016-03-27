import window

BLACK = 'black'
WHITE = 'white'

DARK_COLOR = "#1F53AD"
LIGHT_COLOR = "#e6e6e6"
SQUARE_SIZE = 100
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

class Board:
  def __init__(self):
    self.spaces = [[0 for x in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]


  def get_pixels(self, i):
    return i*SQUARE_SIZE

  def flip_color(self, color):
    return DARK_COLOR if color is LIGHT_COLOR else LIGHT_COLOR

  def draw(self):
    color = LIGHT_COLOR
    for row in range(0, BOARD_HEIGHT):
      for col in range(0, BOARD_WIDTH):
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
    for col in [1, BOARD_HEIGHT-2]:
      for row in range(0, BOARD_WIDTH):
        self.spaces[row][col].place_piece(Piece(BLACK if col is 1 else WHITE))

  def get_space_at_pixels(self, x, y):
    (x, y) = (x / SQUARE_SIZE, y / SQUARE_SIZE)
    return self.spaces[x][y]

class Space:
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color
    self.piece = None

  def get_pixels(self):
    return (self.x*SQUARE_SIZE, self.y*SQUARE_SIZE)

  def get_piece_center_pixels(self):
    (x, y) = self.get_pixels()
    return (x + SQUARE_SIZE/2, y + SQUARE_SIZE/2)

  def draw(self):
    (x0, y0) = self.get_pixels()
    window.draw_rectangle(x0, y0, (x0 + SQUARE_SIZE), (y0 + SQUARE_SIZE), self.color)

  def place_piece(self, piece):
    if self.has_piece():
      raise Exception("A space can only have one piece.")
    self.piece = piece
    (x, y) = self.get_piece_center_pixels()
    piece.move(x, y)

  def has_piece(self):
    return self.piece != None

  def get_piece(self):
    return self.piece

  def remove_piece(self):
    self.piece = None

images = []
class Piece:
  def __init__(self, color):
    f = '/Volumes/projects/chuns/resources/pieces/pawn_%s.png' % color
    self.image = window.add_image(SQUARE_SIZE, SQUARE_SIZE, f)
    self.captured = False

  def move(self, x, y):
    print 'move', x, y
    window.move_image(self.image, x, y)

  def capture(self):
    window.remove(image)
    self.captured = True

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
