import window
from board import Board
from config import TEAMS
from piece import King, Rook

class Game:
  def __init__(self):
    self.board = Board()
    self.input_manager = UserInputManager(self.board, self.move, self.whose_ply)
    self.captured = []
    self.whosePly = TEAMS.WHITE

  def move_inner(self, from_space, dest_space):
    if not from_space.has_piece():
      return False
    piece = from_space.get_piece()

    # TODO: this is the wrong place to check for check!
    # ALSO, we need to generate a new set of spaces and see if the potential
    # move removes the check.
    in_check = self.check(self.board.spaces, self.whosePly)
    if in_check:
      print "%s is in check!" % self.whosePly
      return False

    # Only move your pieces.
    if piece.color != self.whosePly:
      return False

    # You cannot move to a space containing your piece
    if dest_space.has_piece() and dest_space.piece.color == self.whosePly:
      return False

    # Perform a castle if that is the move.
    if self.castle(from_space, dest_space, in_check):
      return True

    # On an empty board, does the piece allow this movement?
    if not piece.can_move(from_space, dest_space):
      return False

    # Make sure we are not 'jumping' over pieces, unless the piece jumps.
    if not (piece.can_jump or self.no_piece_obstructs(from_space, dest_space)):
      return False

    # Can we capture?
    if dest_space.has_piece():
      dest_space.piece.capture()
      dest_space.remove_piece()
    dest_space.move_piece_here(piece, from_space)
    return True

  # Returns False if the move cannot be made, True if it can be and was made.
  def move(self, from_space, dest_space):
    if self.move_inner(from_space, dest_space):
      self.whosePly = self.get_opponent(self.whosePly)
      print "Waiting on %s to move." % ('WHITE' if self.whosePly == TEAMS.WHITE else 'BLACK')
      return True
    return False

  # TODO: probably belongs somewhere else
  def find_king_space(self, spaces, team):
    for row in spaces:
      for col in range(len(row)):
        space = row[col]
        if not space.has_piece():
          continue
        if space.piece.color is team and isinstance(space.piece, King):
          return space
    return None

  # TODO: probably belongs somewhere else
  def find_pieces_spaces(self, spaces, team):
    result = []
    for row in spaces:
      for col in range(len(row)):
        space = row[col]
        if not space.has_piece():
          continue
        if space.piece.color is team:
          result.append(space)
    return result

  # TODO: probably belongs somewhere else
  def get_opponent(self, team):
    return TEAMS.BLACK if team == TEAMS.WHITE else TEAMS.WHITE

  # Is the given team in check for the provided spaces.
  def check(self, spaces, team):
    enemy_piece_spaces = self.find_pieces_spaces(spaces, self.get_opponent(team))
    team_king_space = self.find_king_space(spaces, team)
    for space in enemy_piece_spaces:
      # If a piece can move there, it controls it.
      if space.piece.can_move(space, team_king_space):
        return True
    return False

  def check_mate(self, spaces, team):
    pass

  # Returns false if the move is not a permittable castle move, true if it is and the move was made.
  def castle(self, from_space, dest_space, in_check):
    # The player cannot castle out of check.
    if in_check:
      return False

    # Is the moved piece a king?
    king = from_space.piece
    if not isinstance(king, King):
      return False

    hor = from_space.get_horizontal_distance_to(dest_space)
    vert = from_space.get_vertical_distance_to(dest_space)

    # Has the king moved horizontally two spaces?
    if not (abs(hor) == 2 and vert == 0):
      return False

    to_the_right = hor == 2
    castle_y = dest_space.y

    # Is there a rook two spaces to the left of your movement (or one to the right?).
    expected_rook_x = dest_space.x + 1 if to_the_right else dest_space.x - 2
    rook_space = self.board.spaces[expected_rook_x][castle_y]
    rook = rook_space.piece
    if not isinstance(rook, Rook):
      return False

    # Have the rook and king never moved?
    if king.moves_made != 0 or rook.moves_made != 0:
      return False

    # Are there no pieces between the rook and king?
    if not self.no_piece_obstructs(from_space, rook_space):
      return False

    # TODO: Does an enemy control any spaces that the king moves?
    # 1) generate the spaces between the king and its destination.
    # 2) Check if any of our enemy's pieces can move to those squares

    rooks_dest_x = dest_space.x - 1 if to_the_right else dest_space.x + 1
    rook_dest_space = self.board.spaces[rooks_dest_x][castle_y]

    dest_space.move_piece_here(king, from_space)
    rook_dest_space.move_piece_here(rook, rook_space)
    return True

  def whose_ply(self):
    return self.whosePly

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
    while not (x == x1 and y == y1):
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
  def __init__(self, board, move_cb, whose_ply):
    self.move = move_cb
    self.board = board
    self.space_of_piece_selected = None
    self.whose_ply = whose_ply

    # Called on click down.
    window.bind_left_click_down(self.click_down)

  def _get_space_from_event(self, event):
    return self.board.get_space_at_pixels(event.x, event.y)

  def click_down(self, event):
    try:
      space = self._get_space_from_event(event)
    except:
      return

    noSpaceAlreadySelected = self.space_of_piece_selected == None
    isPlayersPiece = space.piece and space.piece.color is self.whose_ply()

    if noSpaceAlreadySelected:
      # Make sure they are selecting a space with the players'  piece.
      if space.has_piece() and isPlayersPiece:
        self.space_of_piece_selected = space
        window.bind_mouse_motion(self.drag_piece)
        window.bind_left_click_up(self.execute_piece_move)

  def drag_piece(self, event):
    self.space_of_piece_selected.piece.place(event.x, event.y)

  def execute_piece_move(self, event):
    from_space = self.space_of_piece_selected
    self.space_of_piece_selected = None

    try:
      dest_space = self._get_space_from_event(event)
    except:
      pass
    successful_move = self.move(from_space, dest_space)

    if not successful_move:
      (x, y) = from_space.get_center_pixels()
      from_space.piece.place(x, y)

    window.unbind_left_click_up()
    window.unbind_mouse_motion()

