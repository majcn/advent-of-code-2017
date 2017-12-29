data = 361527

sdata = int(pow(data, 0.5))
sdata += 1 if sdata % 2 == 0 else 2

steps = sdata / 2
additionalSteps = abs((sdata * sdata - data) % (steps * 2) - steps)
print steps + additionalSteps




from collections import defaultdict
grid = defaultdict(int)

up    = lambda x,y: (x    , y - 1)
down  = lambda x,y: (x    , y + 1)
right = lambda x,y: (x + 1, y    )
left  = lambda x,y: (x - 1, y    )
directions = [right, up, left, down]

neighbours = lambda x,y: [ (x-1,y-1), (x-1,y+0), (x-1,y+1), (x+0,y-1), (x+0,y+1), (x+1,y-1), (x+1,y+0), (x+1,y+1) ]

x = 0
y = 0
directionI = 0

grid[x,y] = 1
while grid[x,y] < data:
    newDirectionI = (directionI + 1) % 4
    ndx, ndy = directions[newDirectionI](x, y)
    if grid[ndx,ndy] == 0:
        directionI = newDirectionI

    x, y = directions[directionI](x, y)
    grid[x,y] = sum([grid[n] for n in neighbours(x,y)])

print grid[x,y]
