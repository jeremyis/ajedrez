from Tkinter import *
from PIL import ImageTk

from config import CONFIG

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
  return CANVAS.create_image(CONFIG.SQUARE_SIZE, CONFIG.SQUARE_SIZE, image=image)

def move_image(image, x, y):
  CANVAS.coords(image, (x, y))

def remove(image):
  CANVAS.delete(image)

def bind_left_click_down(callback):
  CANVAS.bind("<Button-1>", callback)
def bind_left_click_up(callback):
  CANVAS.bind("<ButtonRelease-1>", callback)
def bind_mouse_motion(callback):
  WINDOW.bind('<Motion>', callback)
def unbind_left_click_up():
  CANVAS.unbind("<ButtonRelease-1>")
def unbind_mouse_motion():
  WINDOW.unbind('<Motion>')

VERSION = "0.1"
WINDOW = Tk()
WINDOW.title("Alejdrez %s" % VERSION)
CANVAS = Canvas(WINDOW, width=CONFIG.SQUARE_SIZE*CONFIG.BOARD_WIDTH, height=CONFIG.SQUARE_SIZE*CONFIG.BOARD_HEIGHT)
