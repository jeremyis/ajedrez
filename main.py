from Tkinter import *

VERSION = "0.2"

DARK_COLOR = "#0d0d0d"
LIGHT_COLOR = "#e6e6e6"
SQUARE_SIZE = 100
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

def draw_square(canvas, color, x0, y0):
    canvas.create_rectangle(x0, y0, (x0 + SQUARE_SIZE), (y0 + SQUARE_SIZE), fill = color, outline = color)
    canvas.pack()

def draw_row(canvas, row):
    x = 0
    y = row*SQUARE_SIZE

    for i in range(0, BOARD_WIDTH):
        if (row + i) % 2 != 0:
            color = LIGHT_COLOR
        else:
            color = DARK_COLOR

        draw_square(canvas, color, x, y)
        x += SQUARE_SIZE

def draw_board():
    window = Tk()
    window.title("Chuns %s" % VERSION)

    canvas = Canvas(window, width=SQUARE_SIZE*BOARD_WIDTH, height=SQUARE_SIZE*BOARD_HEIGHT)
    for j in range(0, BOARD_HEIGHT):
        draw_row(canvas, j)
    window.mainloop()

draw_board()
