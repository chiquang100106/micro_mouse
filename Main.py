import API
import sys
from math import *

x = 0
y = 0
direction = ['n', 'e', 's', 'w']
point = 0
xg = 8
yg = 8
visited = set()
visited_counts = {}

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def update_location(x, y):
    global point
    match direction[point]:
        case 'n':
            y = y + 1
        case 'e':
            x = x + 1
        case 'w':
            x = x - 1
        case 's':
            y = y - 1
    visited.add((x, y))
    if (x, y) in visited_counts:
        visited_counts[(x, y)] += 1
    else:
        visited_counts[(x, y)] = 1
    return x, y

def cost_multiplier(location):
    return 2 ** visited_counts.get(location, 0)

def Forward():
    global x, y, point, direction
    API.moveForward()
    x, y = update_location(x, y)
    API.setColor(x, y, "Y")
    text = "Location: ({},{}), Direction: {}".format(x, y, direction[point])
    log(text)

def steer_Right():
    global point
    API.turnRight()
    point += 1
    if point == 4:
        point = 0

def steer_Left():
    global point
    API.turnLeft()
    point -= 1
    if point == -1:
        point = 3

def dmin():
    if direction[point] == 'n':
        ds = sqrt(pow(xg - x, 2) + pow(yg - (y + 1), 2)) * cost_multiplier((x, y + 1))
        dl = sqrt(pow(xg - (x - 1), 2) + pow(yg - y, 2)) * cost_multiplier((x - 1, y))
        dr = sqrt(pow(xg - (x + 1), 2) + pow(yg - y, 2)) * cost_multiplier((x + 1, y))
    elif direction[point] == 'e':
        ds = sqrt(pow(xg - (x + 1), 2) + pow(yg - y, 2)) * cost_multiplier((x + 1, y))
        dl = sqrt(pow(xg - x, 2) + pow(yg - (y + 1), 2)) * cost_multiplier((x, y + 1))
        dr = sqrt(pow(xg - x, 2) + pow(yg - (y - 1), 2)) * cost_multiplier((x, y - 1))
    elif direction[point] == 'w':
        ds = sqrt(pow(xg - (x - 1), 2) + pow(yg - y, 2)) * cost_multiplier((x - 1, y))
        dl = sqrt(pow(xg - x, 2) + pow(yg - (y - 1), 2)) * cost_multiplier((x, y - 1))
        dr = sqrt(pow(xg - x, 2) + pow(yg - (y + 1), 2)) * cost_multiplier((x, y + 1))
    elif direction[point] == 's':
        ds = sqrt(pow(xg - x, 2) + pow(yg - (y - 1), 2)) * cost_multiplier((x, y - 1))
        dl = sqrt(pow(xg - (x + 1), 2) + pow(yg - y, 2)) * cost_multiplier((x + 1, y))
        dr = sqrt(pow(xg - (x - 1), 2) + pow(yg - y, 2)) * cost_multiplier((x - 1, y))
    return ds, dl, dr

def main():
    log("Start...")
    global x, y, point, direction, xg, yg
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    visited.add((x, y))
    visited_counts[(x, y)] = 1
    while (x, y) != (xg, yg):
        ds, dl, dr = dmin()
        if not API.wallFront():
            if not API.wallLeft() and not API.wallRight():
                if ds < dl and ds < dr:
                    Forward()
                elif dr < dl and dr <= ds:
                    steer_Right()
                    Forward()
                else:
                    steer_Left()
                    Forward()
            elif API.wallRight() and API.wallLeft():
                API.setColor(x,y,color="red")
                Forward()
            elif API.wallLeft() and not API.wallRight():
                API.setColor(x,y,color="red")
                if ds < dr:
                    Forward()
                else:
                    steer_Right()
                    Forward()
            elif API.wallRight() and not API.wallLeft():
                API.setColor(x,y,color="red")
                if ds < dl:
                    Forward()
                else:
                    steer_Left()
                    Forward()
        else:
            if not API.wallLeft() and not API.wallRight():
                if dl <= dr:
                    steer_Left()
                    Forward()
                else:
                    steer_Right()
                    Forward()
            elif API.wallRight() and not API.wallLeft():
                API.setColor(x,y,color="red")
                steer_Left()
                Forward()
            elif API.wallLeft() and not API.wallRight():
                API.setColor
                steer_Right()
                Forward()
            else:
                API.setColor(x,y,color="red")
                steer_Right()
                steer_Right()
                Forward()
    log("Reached the goal!")
    API.setText(xg, yg, "Goal")

if __name__ == "__main__":
    main()
