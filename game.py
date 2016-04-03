import window
from board import Board
from config import TEAMS

class Game:
  def __init__(self):
    self.board = Board()
    self.input_manager = UserInputManager(self.board, self.move)
    self.captured = []
    self.whosePly = TEAMS.WHITE

  def move(self, from_space, dest_space):
    # TODO: check if piece can move this way
    # TODO: make sure nothing is obstructing
    # TODO: make sure we are not moving into check.
    # TODO: Check if piece is other color
    if not from_space.has_piece():
      return
    piece = from_space.get_piece()

    # Only move your pieces.
    if piece.color != self.whosePly:
      return

    # You cannot move to a space containing your piece
    if dest_space.has_piece() and dest_space.piece.color == self.whosePly:
      return

    # On an empty board, does the piece allow this movement?
    if not piece.can_move(from_space, dest_space):
      return

    # Make sure we are not 'jumping' over pieces, unless the piece jumps.
    if not (piece.can_jump or self.no_piece_obstructs(from_space, dest_space)):
      return

    # Can we capture?
    if dest_space.has_piece():
      dest_space.piece.capture()
      dest_space.remove_piece()
    dest_space.move_piece_here(piece, from_space)

    # TODO: is there a way we can make our run loop better?
    self.whosePly = TEAMS.BLACK if self.whosePly == TEAMS.WHITE else TEAMS.WHITE

  def no_piece_obstructs(self, from_space, dest_space):
    (x, y) = (from_space.x, from_space.y)
    (x1, y1) = (dest_space.x, dest_space.y)

    def inc(source, dest):
      diff = dest - source
      if diff == 0:
        return 0
      return 1 if diff > 0 else -1

    def next_space(x, y):
      x += inc(x, x1)
      y += inc(y, y1)
      return (x, y)

    # Do not check the current space, nor the final space.
    (x, y) = next_space(x, y)
    while x != x1 and y != y1:
      space = self.board.spaces[x][y]
      if space.has_piece():
        return False
      (x, y) = next_space(x, y)

    return True


  def run(self):
    self.board.draw()
    # whose turn?
    # wait for their move
    # is move ok?
    # if so make it, otherwise loop back
    # make move.
    #  - did we capture a piece?
    #  - should we upgrade?
    # is game checkmate checkmate? if so exit
    # is game a draw? if so exit.

      # next person turn.

class UserInputManager:
  def __init__(self, board, move_cb):
    self.move = move_cb
    self.board = board
    self.space_of_piece_selected = None
    window.bind_left_click(self.click_callback)

  # TODO: maybe we should move the clicking elsewhere?
  def click_callback(self, event):
    (x, y) = (event.x, event.y)
    space = self.board.get_space_at_pixels(x, y)

    if self.space_of_piece_selected == None:
      self.space_of_piece_selected = space

    # Clicking on the same space clears the state.
    elif self.space_of_piece_selected == space:
      self.space_of_piece_selected = None
    else:
      from_space = self.space_of_piece_selected
      self.move(from_space, space)
      self.space_of_piece_selected = None

