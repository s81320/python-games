from random import *
from tkinter import *
from time import sleep, time
size = 500
TIME_LIMIT = 5
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()
ende = time() + TIME_LIMIT
while time() < ende:
     col = choice(['red', 'blue', 'purple', 'pink'])
     x0 = randint(0, size)
     y0 = randint(0, size)
     d = randint(0, size/5)
     canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=col)
     window. update()
