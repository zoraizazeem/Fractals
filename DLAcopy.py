import tkinter as tk
import random
import os
from PIL import ImageGrab
import sys

store_dir = "/Users/zoraizazeem/Documents/PProjects/FractalsDiss/clusters/exp2/"
files = os.listdir(store_dir)
iters= []
for file in files:
    if not file.endswith('.DS_Store'):
        num = int(''.join([str(s) for s in file if s.isdigit()]))
        iters.append(num)
iters.sort()

if iters[-1] == 25:
    print("ENDED due to enough iterations done!")
    os._exit(0)

# --- classes ---
r = 6
canv_size = 500
class Ball:

    def __init__(self, x, y, speed_x, speed_y, color):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.shape = canvas.create_oval(x, y, x+(2*r), y+(2*r), fill=color)

    def move(self):

        canvas.move(self.shape, self.speed_x, self.speed_y)

        pos = canvas.coords(self.shape)

        if pos[3] >= canv_size or pos[1] <= 0:
            self.speed_y = -self.speed_y
        if pos[2] > canv_size or pos[0] <= 0:
            self.speed_x = -self.speed_x
    def get_posit(self):
        return canvas.coords(self.shape)

    def delete(self):
        canvas.delete(self.shape)

# --- functions ---
def dist(a, b):
    return sum([(aItem -bItem)**2 for aItem, bItem in zip(a, b)])



def screenshot():
    
    root.deiconify()
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    x1 = x + root.winfo_width()
    y1 = y + root.winfo_height()
    x_pixels = 337
    y_pixels = 79
    x_screen = 171
    y_screen = 41
    x = x*(x_pixels/x_screen)
    y = y*(y_pixels/y_screen)
    x1 = x1*(x_pixels/x_screen)
    y1 = y1*(y_pixels/y_screen)
    new_file = iters[-1] + 1
    new_file = "{}.png".format(new_file)
    new_file = store_dir +new_file 
    ImageGrab.grab().crop((x, y, x1, y1)).save(new_file)
    print("screenshot taken, file in in: {}".format(new_file))

def move():
    if len(tree) > (0.5*no_free_balls ):
        screenshot()
        print(tree)
        print("Here is the number of balls final: {}".format(len(all_balls)))
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    i = 0
    length = len(all_balls)

    while i < length:
        ball_gone = 0
        posit = all_balls[i].get_posit()
        for point_tree in tree:
            distance = dist(posit, point_tree)
            if distance < (r*r*10):
                canvas.create_oval(posit[0], posit[3], posit[2], posit[1], fill="green")
                tree.append(posit)
                all_balls[i].delete()
                ball_gone =1
                all_balls.remove(all_balls[i])
                i -= 1
                length -= 1
                break
        if ball_gone != 1:
            all_balls[i].move()
        i += 1
    root.after(100, move)
    '''for ball in all_balls:
        ball_gone = 0
        posit = ball.get_posit()
        if posit:
            for point_tree in tree:
                distance = dist(posit, point_tree)

                if distance < (r*r*10):
                    canvas.create_oval(posit[0], posit[3], posit[2], posit[1], fill="green")
                    tree.append(posit)
                    ball.delete()
                    ball_gone =1
                    break
            if ball_gone != 1:
                ball.move()

    root.after(100, move)'''


# --- main ---

root = tk.Tk()
#root.withdraw()
canvas = tk.Canvas(root, width=canv_size, height=canv_size)
canvas.pack()

center = canv_size/2

tree =[(center-r,center-r,center+r,center+r)]
canvas.create_oval(center-r,center-r,center+r,center+r, fill ="yellow")

all_balls = []

for x in range(2, canv_size, 30):
    for y in range(4, canv_size, 30):
        offset_x = random.randint(-4, 4)
        offset_y = random.randint(-4, 4)
        a = random.randint(r, canv_size-r)
        b = random.randint(r, canv_size-r)
        all_balls.append((Ball(a ,b , offset_x, offset_y, "red")))
no_free_balls = len(all_balls)


move()

root.mainloop()
