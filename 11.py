from PrepareData import PrepareData
inputdata = PrepareData.fetchData()


data = inputdata[0][0].split(',')


x = 0
y = 0
maxx = 0
maxy = 0

for d in data:
    if d == 'ne':
        x += 1
        y += 1
    if d == 'se':
        x += 1
        y -= 1
    if d == 's':
        y -= 2
    if d == 'sw':
        x -= 1
        y -= 1
    if d == 'nw':
        x -= 1
        y += 1
    if d == 'n':
        y += 2

    maxx = max(maxx, abs(x))
    maxy = max(maxy, abs(y))

for cx,cy in [[x,y], [maxx,maxy]]:
    ax = abs(cx)
    ay = abs(cy)

    if ax >= ay:
        print ax
    else:
        r = ay - ax
        print r / 2 + ax
