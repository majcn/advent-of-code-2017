data = 361527

from math import sqrt
sdata = int(sqrt(data))
sdata += 1 if sdata % 2 == 0 else 2

steps = sdata / 2
additionalSteps = abs((sdata * sdata - data) % (steps * 2) - steps)
print steps + additionalSteps





l = 15
grid = [[ 0 ] * l for x in range(l)]

up    = lambda x,y: (x    , y - 1)
down  = lambda x,y: (x    , y + 1)
right = lambda x,y: (x + 1, y    )
left  = lambda x,y: (x - 1, y    )
directions = [right, up, left, down]

x = l / 2
y = l / 2
directionI = 0

grid[x][y] = 1
while grid[x][y] < data:
    newDirectionI = (directionI + 1) % 4
    ndx, ndy = directions[newDirectionI](x, y)
    if grid[ndx][ndy] == 0:
        directionI = newDirectionI

    x, y = directions[directionI](x, y)
    grid[x][y] = grid[x-1][y] + grid[x][y-1] + grid[x+1][y] + grid[x][y+1] + grid[x+1][y+1] + grid[x-1][y-1] + grid[x+1][y-1] + grid[x-1][y+1]

print grid[x][y]