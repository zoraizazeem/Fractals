import random
from tkinter.tix import Tree
import pandas as pd
import os
import sys

density = 120
canv_size = 200
thresh = 0.8
r = 0.5 
center = canv_size/2
num_particles = 100
seed_pos = (int(center-r),int(center-r),int(center+r),int(center+r))


store_dir = "/Users/zoraizazeem/Documents/PProjects/FractalsDiss/ClusterCSV/"
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

#if 

class Ball:

    def __init__(self, x, y, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.shape = (x, y,x+(2*r), y+(2*r) )

    def move(self):
        top_left = (self.shape[0], self.shape[1])
        bottom_right = (self.shape[2], self.shape[3])
        #canvas.move(self.shape, self.speed_x, self.speed_y)

        movement = (self.speed_x, self.speed_y)
        self.shape = tuple([sum(x) for x in zip(movement,top_left)]) + tuple([sum(x) for x in zip(movement,bottom_right)])
        
        pos = self.shape    
        if pos[3] >= canv_size or pos[1] <= 0:
            self.speed_y = -self.speed_y
        if pos[2] > canv_size or pos[0] <= 0:
            self.speed_x = -self.speed_x

    def get_posit(self):
        return self.shape



def dist(a, b):
    a = (((a[0]+a[2])/2), ((a[1]+a[3])/2))
    b = (((b[0]+b[2])/2), ((b[1]+b[3])/2))
    #print(a)
    return sum([(aItem -bItem)**2 for aItem, bItem in zip(a, b)])




def move():
    while len(tree) < (thresh*no_free_balls ):
        #if len(tree) > (0.5*no_free_balls ):
            #screenshot()
            #print("restart here")
            #os.execl(sys.executable, sys.executable, *sys.argv)
               
        i = 0
        length = len(all_balls)

        while i < length:
            ball_gone = 0
            posit = all_balls[i].get_posit()
            for point_tree in tree:
                distance = dist(posit, point_tree)
                #print(distance)
                if distance <= (r*r*4):
                    #canvas.create_oval(posit[0], posit[3], posit[2], posit[1], fill="green")
                    tree.append(posit)
                    #all_balls[i].delete()
                    ball_gone =1
                    all_balls.remove(all_balls[i])
                    i -= 1
                    length -= 1
                    break
            if ball_gone != 1:
                all_balls[i].move()
            i += 1
        ratio = len(tree)/(thresh*no_free_balls)
        print("iterating here : {}".format(ratio))

    print("save file here")
    new_file = iters[-1] + 1
    new_file = "{}.csv".format(new_file)
    new_file = store_dir +new_file 
    print(len(all_balls))
    df = pd.DataFrame(tree)
    df.to_csv(new_file, index=False)
    print("restart here")
    os.execl(sys.executable, sys.executable, *sys.argv)

    #print("final tree : {}".format(tree))
    #threading.Timer(0.1, move).start()



tree = []
tree.append(seed_pos)

all_balls = []
for _ in range(density):
    offset_x = random.randint(-7, 7)
    offset_y = random.randint(-7, 7)
    a = random.randint(2, canv_size-2)
    b = random.randint(2, canv_size-2)
    all_balls.append((Ball(a ,b , offset_x, offset_y)))
no_free_balls = len(all_balls)
print(no_free_balls)
move()
#no_free_balls = len(all_balls)



