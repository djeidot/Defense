from data import map
from copy import deepcopy

# Create working area of map
workmap = deepcopy(map)
width = len(workmap)
height = len(workmap[0])

def putWall(r, c):
    if workmap[r][c] != "W" and workmap[r][c] != "L":
        workmap[r][c] = "L"

def printmap():
    printmap = '\n'.join(''.join(line) for line in workmap)
    printmap = printmap.replace("M", "^").replace("W", "~").replace("F", '"').replace("G", "'").replace("L", "#").replace("V", "H")
    print(printmap)

def get_land_cost(r, c):
    cell = map[r][c]
    costs = {"G": 1, "F": 10, "M": 100, "W": 0}
    return costs[cell]
    
def get_cost():
    total_cost = 0
    for r in range (0, width):
        for c in range(0, height):
            if workmap[r][c] == "L":
                total_cost = total_cost + get_land_cost(r, c)
                
    return total_cost

# draw wall on edges and calculate cost
def draw_walls(dist):
    for r in range(0, width):
        if r == dist or r == width - dist - 1:
            for c in range (dist, height - dist - 1):
                putWall(r, c)
        else:
            putWall(r, dist)
            putWall(r, height - dist - 1)


draw_walls(0)
printmap()
print("cost is " + str(get_cost()))



