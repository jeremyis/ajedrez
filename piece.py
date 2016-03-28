import window
from config import CONFIG, PIECES

def create(name, color):
  return {
    PIECES.PAWN: Pawn(color),
    PIECES.KING: King(color),
    PIECES.QUEEN: Queen(color),
    PIECES.BISHOP: Bishop(color),
    PIECES.KNIGHT: Knight(color),
    PIECES.ROOK: Rook(color)
  }[name]

piece_directory = './resources/pieces/'
class Piece(object):
  def __init__(self, color):
    self.color = color
    self.captured = False
    self.name = ''

  def move(self, x, y):
    print 'move', x, y
    window.move_image(self.image, x, y)

  def draw(self):
    self.image = window.add_image(
        CONFIG.SQUARE_SIZE, CONFIG.SQUARE_SIZE, self.get_file())

  def capture(self):
    window.remove(image)
    self.captured = True

  def get_file(self):
    print '%s%s_%s.png' % (piece_directory, self.name, self.color)
    return '%s%s_%s.png' % (piece_directory, self.name, self.color)

class Pawn(Piece):
  def __init__(self, color):
    super(Pawn, self).__init__(color)
    self.name = 'pawn'

class King(Piece):
  def __init__(self, color):
    super(King, self).__init__(color)
    self.name = 'king'

class Queen(Piece):
  def __init__(self, color):
    super(Queen, self).__init__(color)
    self.name = 'queen'

class Bishop(Piece):
  def __init__(self, color):
    super(Bishop, self).__init__(color)
    self.name = 'bishop'

class Knight(Piece):
  def __init__(self, color):
    super(Knight, self).__init__(color)
    self.name = 'knight'

class Rook(Piece):
  def __init__(self, color):
    super(Rook, self).__init__(color)
    self.name = 'rook'
