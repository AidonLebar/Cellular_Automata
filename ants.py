from random import randint, uniform

grid = []
a = None
w = 300
h = 300

def flip(x, y):
    global grid
    if grid[x][y] == 0:
        grid[x][y] = 1
    else:
        grid[x][y] = 0

def no_flip(x, y):
    pass

def get_value(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0
    else:
        return grid[x][y]
    
class ant():
    x = w/2
    y = h/2
    dir = [0,1]
    move_actions = {}
    grid_actions = {}

    def __init__(self):
        self.move_actions[0] = self.forward
        self.grid_actions[0] = flip
        for i in range(1,255):
            p1 = uniform(0,1)
            if p1 < 0.1:
                self.move_actions[i] = self.forward
            elif p1 < 0.55:
                self.move_actions[i] = self.turn_right
            else:
                self.move_actions[i] = self.turn_left
            p2 = uniform(0,1)
            if p2 < 0.5:
                self.grid_actions[i] = flip
            else:
                self.grid_actions[i] = no_flip

    def forward(self):
        self.x = (self.x + self.dir[0]) % width
        self.y = (self.y + self.dir[1]) % height

    def turn_right(self):
        if self.dir[0] == 1:
            self.dir[0] = 0
            self.dir[1] = -1
        elif self.dir[0] == -1:
            self.dir[0] = 0
            self.dir[1] = 1
        elif self.dir[1] == 1:
            self.dir[0] = 1
            self.dir[1] = 0
        elif self.dir[1] == -1:
            self.dir[0] = -1
            self.dir[1] = 0
        self.forward()

    def turn_left(self):
        if self.dir[0] == 1:
            self.dir[0] = 0
            self.dir[1] = 1
        elif self.dir[0] == -1:
            self.dir[0] = 0
            self.dir[1] = -1
        elif self.dir[1] == 1:
            self.dir[0] = -1
            self.dir[1] = 0
        elif self.dir[1] == -1:
            self.dir[0] = 1
            self.dir[1] = 0
        self.forward()

    def act(self):
        n = get_neighborhood(self.x, self.y)
        self.grid_actions[n](self.x, self.y)
        self.move_actions[n]()
        
    
def get_neighborhood(x, y):
    n = 0
    c = 7
    for i in range(-1,1):
        for j in range(-1,1):
            n += get_value(x + i, y + j) << c
            c -= 1
    return n

def setup():
    global grid,a
    size(w, h)
    background(0)
    stroke(255)
    frameRate(300)
    a = ant()  
    for i in range(width):
        grid.append([])
        for j in range(height):
            p = uniform(0,1)
            if p < 0.99:
                grid[i].append(0)
            else:
                grid[i].append(1)
            
def draw():
    clear()
    a.act()
    for i in range(width):
        for j in range(height):
            if grid[i][j] == 1:
                point(i,j)
                
