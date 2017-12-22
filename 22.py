from PrepareData import PrepareData
inputdata = PrepareData.fetchData()


directions = {
    'up':    ('up',    lambda x,y: (x, y-1)),
    'down':  ('down',  lambda x,y: (x, y+1)),
    'left':  ('left',  lambda x,y: (x-1, y)),
    'right': ('right', lambda x,y: (x+1, y))
}

next_direction = {
    ('up',    'left'):  directions['left'],
    ('up',    'right'): directions['right'],
    ('down',  'left'):  directions['right'],
    ('down',  'right'): directions['left'],
    ('left',  'left'):  directions['down'],
    ('left',  'right'): directions['up'],
    ('right', 'left'):  directions['up'],
    ('right', 'right'): directions['down']
}

reverse_direction = {
    'up':    directions['down'],
    'down':  directions['up'],
    'left':  directions['right'],
    'right': directions['left'],
}

def getCluster(infected_id, cluster_size = 5555):
    data = [map(lambda x: infected_id if x == '#' else 0, d) for d in inputdata]
    start_y = len(data) / 2
    start_x = len(data[start_y]) / 2

    cluster = [[0] * cluster_size for i in range(cluster_size)]
    c_start_y = len(cluster) / 2
    c_start_x = len(cluster[c_start_y]) / 2

    for y in range(len(data)):
        for x in range(len(data[y])):
            cluster[c_start_y - start_y + y][c_start_x - start_x + x] = data[y][x]

    return (cluster, c_start_x, c_start_y, directions['up'])

result = 0
cluster, cx, cy, direction = getCluster(1)
for i in range(10000):
    node = cluster[cy][cx]
    if node == 0:
        result += 1
        direction = next_direction[(direction[0], 'left')]
    elif node == 1:
        direction = next_direction[(direction[0], 'right')]

    cluster[cy][cx] = (node + 1) % 2
    cx, cy = direction[1](cx,cy)
print result


result = 0
cluster, cx, cy, direction = getCluster(2)
for i in range(10000000):
    node = cluster[cy][cx]
    if node == 0:
        direction = next_direction[(direction[0], 'left')]
    elif node == 1:
        result += 1
    elif node == 2:
        direction = next_direction[(direction[0], 'right')]
    elif node == 3:
        direction = reverse_direction[direction[0]]

    cluster[cy][cx] = (node + 1) % 4
    cx, cy = direction[1](cx,cy)
print result
