from tkinter import * 
import time
window = Tk()
WIDTH = 500
HEIGHT = 500
window.resizable(False, False)
TK_SILENCE_DEPRECATION=1
canvas = Canvas(window, width= WIDTH, height=HEIGHT)
canvas.pack()
#my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)
canvas.create_oval(200,200,300,300, fill ="black")

xspeed = yspeed = 3


window.mainloop()
