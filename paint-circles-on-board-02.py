from tkinter import *
from random import *
from time import sleep, time



board = [[-1,0,0,0] , [-1,-1,0,1] , [-1 , 0, 1, 1], [0,0,-1,1]]
# colours set wrt board: -1: empty , 0: color for player 0 , 1: color for player 1

dim = 4
diam = 40
square_size = 50
size = 20 + dim * (diam + 10) + 20
size = 500

window = Tk()

canvas = Canvas(window, width=size, height=size)

canvas.pack()

for i in (1,2,3,4,5,6):
	for j in (1,2,3,4,5,6):		
		canvas.create_oval(square_size*int(i) , square_size*int(j), int(i)*square_size+diam , int(j)*square_size+diam, fill='red')

mainloop()