def enum(**enums):
  return type('Enum', (), enums)

PIECES = enum(PAWN=0, KING=1, QUEEN=2, BISHOP=3, KNIGHT=4, ROOK=5)
TEAMS = enum(WHITE='white', BLACK='black')


class GameConfig:
  first_mover = None
  BOARD_WIDTH = 8
  BOARD_HEIGHT = 8
  SQUARE_SIZE = 100
  BOARD_DARK_COLOR = "#1F53AD"
  BOARD_LIGHT_COLOR = "#e6e6e6"
  PLAYERS = []
  PIECES = []

class NormalConfig(GameConfig):
  PIECES = (
    ( PIECES.PAWN,   TEAMS.WHITE, 'a2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'b2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'c2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'd2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'e2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'f2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'g2' ),
    ( PIECES.PAWN,   TEAMS.WHITE, 'h2' ),
    ( PIECES.ROOK,   TEAMS.WHITE, 'a1' ),
    ( PIECES.KNIGHT, TEAMS.WHITE, 'b1' ),
    ( PIECES.BISHOP, TEAMS.WHITE, 'c1' ),
    ( PIECES.KING,   TEAMS.WHITE, 'd1' ),
    ( PIECES.QUEEN,  TEAMS.WHITE, 'e1' ),
    ( PIECES.BISHOP, TEAMS.WHITE, 'f1' ),
    ( PIECES.KNIGHT, TEAMS.WHITE, 'g1' ),
    ( PIECES.ROOK,   TEAMS.WHITE, 'h1' ),

    ( PIECES.PAWN,   TEAMS.BLACK, 'a7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'b7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'c7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'd7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'e7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'f7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'g7' ),
    ( PIECES.PAWN,   TEAMS.BLACK, 'h7' ),
    ( PIECES.ROOK,   TEAMS.BLACK, 'a8' ),
    ( PIECES.KNIGHT, TEAMS.BLACK, 'b8' ),
    ( PIECES.BISHOP, TEAMS.BLACK, 'c8' ),
    ( PIECES.KING,   TEAMS.BLACK, 'd8' ),
    ( PIECES.QUEEN,  TEAMS.BLACK, 'e8' ),
    ( PIECES.BISHOP, TEAMS.BLACK, 'f8' ),
    ( PIECES.KNIGHT, TEAMS.BLACK, 'g8' ),
    ( PIECES.ROOK,   TEAMS.BLACK, 'h8' ),
  )

CONFIG = NormalConfig()
