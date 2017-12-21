from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

def getAllMoves():
    ff = lambda x: 1 if x == '#' else 0

    rotate = lambda l: tuple(reversed(zip(*l)))
    flip   = lambda l: tuple(map(lambda x: tuple(reversed(x)), l))

    result = {}
    for d in inputdata:
        i,o = d.split(' => ')

        ii = tuple(tuple(map(ff, ii)) for ii in i.split('/'))
        oo = tuple(tuple(map(ff, oo)) for oo in o.split('/'))

        iir1 = rotate(ii)
        iir2 = rotate(iir1)
        iir3 = rotate(iir2)

        iif1 = flip(ii)
        iif1r1 = rotate(iif1)
        iif1r2 = rotate(iif1r1)
        iif1r3 = rotate(iif1r2)

        result[ii] = oo
        result[iir1] = oo
        result[iir2] = oo
        result[iir3] = oo
        result[iif1] = oo
        result[iif1r1] = oo
        result[iif1r2] = oo
        result[iif1r3] = oo

    return result

def split(g, step):
    return [ tuple( tuple(g[i+y][j+x] for x in range(step) ) for y in range(step)) for i in range(0, len(g), step) for j in range(0, len(g), step) ]

from math import sqrt
def merge(lg, step):
    size = int(sqrt(len(lg)))
    return tuple( reduce(lambda r,e: r+e, [lg[size*i + j][x] for j in range(size)]) for i in range(size) for x in range(step) )


moves = getAllMoves()


data = ( (0,1,0), (0,0,1), (1,1,1) )

f =  lambda g,s: merge([moves[x] for x in split(g, s)], s+1)
ff = lambda g,_: f(g, 2) if len(g) % 2 == 0 else f(g, 3)

print sum(map(sum, reduce(ff, range(5),  data)))
print sum(map(sum, reduce(ff, range(18), data)))
