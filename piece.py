import window
from config import CONFIG, PIECES, TEAM_DIRECTION

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
    self.moves_made = 0

  def place(self, x, y):
    window.move_image(self.image, x, y)
  def move(self, x, y):
    self.place(x, y)
    self.moves_made += 1

  def draw(self):
    self.image = window.add_image(
        CONFIG.SQUARE_SIZE, CONFIG.SQUARE_SIZE, self.get_file())

  def capture(self):
    window.remove(self.image)
    self.captured = True

  def get_file(self):
    return '%s%s_%s.png' % (piece_directory, self.name, self.color)

  # Returns true if the piece can legally move from from_space to to_space
  # pretending nothing else is on the board.
  def can_move(self, from_space, to_space):
    raise Exception("Calling base Piece.can_move_here!")


class Pawn(Piece):
  def __init__(self, color):
    super(Pawn, self).__init__(color)
    self.name = 'pawn'

  def direction_factor(self):
    # TODO: put this into the config.
    return TEAM_DIRECTION[self.color]

  def can_move(self, from_space, dest_space):
    hor = from_space.get_horizontal_distance_to(dest_space)
    vert = from_space.get_vertical_distance_to(dest_space)

    # Account for white and black movements.
    vert = self.direction_factor()*vert

    # Can take one space diagonally in front.
    diagonal_once = abs(hor) == 1 and vert == 1
    has_enemy = dest_space.has_piece() and dest_space.piece.color != self.color
    if diagonal_once and has_enemy:
      return True

    # TODO: handle EP (probably in game logic)

    # If not taking diagonally, a pawn can never move horizontally.
    if hor != 0:
      return False

    dest_without_piece = not dest_space.has_piece()

    # OK to move 2 spaces if never moved.
    if self.moves_made is 0 and vert is 2 and dest_without_piece:
      return True

    # Normal pawn movement.
    if vert is 1 and dest_without_piece:
      return True

    # TODO: capturing.

    return False


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
