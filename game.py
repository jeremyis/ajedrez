import window
from board import Board

class Game:
  def __init__(self):
    self.board = Board()
    self.input_manager = UserInputManager(self.board, self.move)
    self.captured = []

  def move(self, from_space, dest_space):
    # TODO: check if piece can move this way
    # TODO: make sure nothing is obstructing
    # TODO: make sure we are not moving into check.
    # TODO: Check if piece is other color
    if not from_space.has_piece():
      return
    piece = from_space.get_piece()
    if dest_space.has_piece():
      # TODO: implement capturing
      pass
    dest_space.place_piece(piece)

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
    pass

class UserInputManager:
  def __init__(self, board, move_cb):
    self.move = move_cb
    self.board = board
    self.space_of_piece_selected = None
    window.bind_left_click(self.click_callback)

  # TODO: maybe we should move the clicking elsewhere?
  def click_callback(self, event):
    print "clicked at", event.x, event.y
    (x, y) = (event.x, event.y)
    space = self.board.get_space_at_pixels(x, y)

    if self.space_of_piece_selected != None:
      self.move(self.space_of_piece_selected, space)
      self.space_of_piece_selected = None
      # TODO: check if move is legal. How to call game.move(self, from, to)?

    else:
      self.space_of_piece_selected = space

