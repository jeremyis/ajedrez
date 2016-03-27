from Tkinter import *
from PIL import ImageTk, Image

VERSION = "0.2"

DARK_COLOR = "#1F53AD"
LIGHT_COLOR = "#e6e6e6"
SQUARE_SIZE = 100
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

BLACK = 'black'
WHITE = 'white'

class Board:
  def __init__(self):
    self.spaces = [[0 for x in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]
    self.space_of_piece_selected = None
    CANVAS.bind("<Button-1>", self.click_callback)

    self.draw()
    self.place_pieces()

  # TODO: maybe we should move the clicking elsewhere?
  def click_callback(self, event):
    print "clicked at", event.x, event.y
    (x, y) = (event.x / SQUARE_SIZE, event.y / SQUARE_SIZE)
    space = self.spaces[x][y]
    if self.space_of_piece_selected:
      piece = self.space_of_piece_selected.piece
      self.space_of_piece_selected.remove_piece()
      space.place_piece(piece)
      self.space_of_piece_selected = None
    else:
      self.space_of_piece_selected = space


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

  def draw_space(self, x, y, color):
    space = Space(x, y, color)
    space.draw()
    self.spaces[x][y] = space
    return space

  def place_pieces(self):
    for col in [1, BOARD_HEIGHT-2]:
      for row in range(0, BOARD_WIDTH):
        self.spaces[row][col].place_piece(Piece(BLACK if col is 1 else WHITE))

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
    CANVAS.create_rectangle(x0, y0, (x0 + SQUARE_SIZE), (y0 + SQUARE_SIZE), fill = self.color, outline = self.color)
    print 'space', x0, y0, self.color

  def place_piece(self, piece):
    # TODO: check if there's a piece and throw an exception
    self.piece = piece
    (x, y) = self.get_piece_center_pixels()
    piece.move(x, y)

  def has_piece(self):
    return self.piece != None

  def remove_piece(self):
    self.piece = None

images = []
class Piece:
    def __init__(self, color):
      global images
      f = '/Volumes/projects/chuns/resources/pieces/pawn_%s.png' % color
      image = ImageTk.PhotoImage(file=f)
      images.append(image)
      self.image = CANVAS.create_image(SQUARE_SIZE, SQUARE_SIZE, image=image)

    def move(self, x, y):
      print 'move', x, y
      CANVAS.coords(self.image, (x, y))

# TODO: move to Game class.
WINDOW = Tk()
WINDOW.title("Chuns %s" % VERSION)
CANVAS = Canvas(WINDOW, width=SQUARE_SIZE*BOARD_WIDTH, height=SQUARE_SIZE*BOARD_HEIGHT)
board = Board()
CANVAS.pack()
WINDOW.mainloop()

"""
def callback(event):
    print "clicked at", event.x, event.y

canvas.bind("<Button-1>", callback)
"""

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

window.bind('<Motion>', motion)
