from random import randint, uniform
from datetime import datetime

grid = []
rules = {}
w = 300
h = 300

def inc(x, y):
    return (grid[x][y] + 1) % 3

def dec(x, y):
     return (grid[x][y] - 1) % 3 

def no_flip(x, y):
    return grid[x][y]

def get_value(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0
    else:
        return grid[x][y]       
    
def get_neighborhood(x, y):
    n = 0
    for i in range(-1,2):
        for j in range(-1,2):
            n += get_value(x + i, y + j)
    return n

def setup():
    global grid,rules
    size(w, h)
    background(0)
    stroke(255)
    frameRate(300)
    for i in range(width):
        grid.append([])
        for j in range(height):
            grid[i].append(0)
    grid[w/2][h/2] = 1
    for i in range(19):
        p = uniform(0,1)
        if p < 1.0/3.0:
            rules[i] = inc
        elif p < 2.0/3.0:
            rules[i] = dec
        else:
            rules[i] = no_flip
            
def draw():
    global grid
    temp_grid = []
    for i in range(0, width):
        temp_grid.append([])
        for j in range(0,height):
            temp_grid[i].append(rules[get_neighborhood(i, j)](i, j))
    grid = temp_grid
    clear()
    for i in range(width):
        for j in range(height):
            if grid[i][j] == 1:
                stroke(255)
                point(i,j)
            elif grid[i][j] == 2:
                stroke(255,0,0)
                point(i,j)

def keyPressed():
    if (key == 's'):
        now = datetime. now()
        time = now.strftime("%H-%M-%S")
        print("Saving image as cellular-{}.png".format(time))
        saveFrame("cellular-{}.png".format(time))
