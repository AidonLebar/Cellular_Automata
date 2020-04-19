from random import randint, uniform
from datetime import datetime

grid = []
rules = {}
w = 300
h = 300

def flip(x, y):
    global grid
    if grid[x][y] == 0:
        return 1
    else:
        return 0

def flip_one(x, y):
    return 1

def flip_zero(x, y):
    return 0 

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
            p = uniform(0,1)
            if p < 0.999:
                grid[i].append(0)
            else:
                grid[i].append(1)
    for i in range(10):
        p = uniform(0,1)
        if p < 0.25:
            rules[i] = flip
        elif p < 0.5:
            rules[i] = flip_one
        elif p < 0.75:
            rules[i] = flip_zero
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
                point(i,j)

def keyPressed():
    if (key == 's'):
        now = datetime. now()
        time = now.strftime("%H-%M-%S")
        print("Saving image as cellular-{}.png".format(time))
        saveFrame("cellular-{}.png".format(time))
