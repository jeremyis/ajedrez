from Tkinter import *
from PIL import ImageTk

VERSION = "0.2"

SQUARE_SIZE = 100
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

# There is a bug with Tkinter where images
images = {}

def run():
  CANVAS.pack()
  WINDOW.mainloop()

def draw_rectangle(x, y, x1, y1, color):
  CANVAS.create_rectangle(x, y, x1, y1, fill = color, outline = color)

def add_image(width, height, path):
  image = None
  if images.has_key(path):
    image = images[path]
  else:
    image = ImageTk.PhotoImage(file=path)
    images[path] = image
  return CANVAS.create_image(SQUARE_SIZE, SQUARE_SIZE, image=image)

def move_image(image, x, y):
  CANVAS.coords(image, (x, y))

def remove(image):
  CANVAS.remove(image)

def bind_left_click(callback):
  CANVAS.bind("<Button-1>", callback)

WINDOW = Tk()
WINDOW.title("Chuns %s" % VERSION)
CANVAS = Canvas(WINDOW, width=SQUARE_SIZE*BOARD_WIDTH, height=SQUARE_SIZE*BOARD_HEIGHT)

