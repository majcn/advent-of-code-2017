from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

data = inputdata[0].split(',')

import re

re_spin = re.compile(r'^s(\d+)$')
def spin(myProg, x):
    x = int(x)
    x = x % len(myProg)

    return myProg[-x:] + myProg[:len(myProg) - x]

re_exchange = re.compile(r'^x(\d+)/(\d+)$')
def exchange(myProg, i1, i2):
    return partner(myProg, myProg[int(i1)], myProg[int(i2)])

re_partner = re.compile(r'^p(\w+)/(\w+)$')
def partner(myProg, p1, p2):
    return myProg.replace(p1, '$', 1).replace(p2, p1, 1).replace('$', p2, 1)

progs = [
    (re_spin, spin),
    (re_exchange, exchange),
    (re_partner, partner)
]

moves = [lambda p, f=f, a=r.match(d).groups(): f(p, *a) for d in data for r,f in progs if r.match(d)]

myProg = 'abcdefghijklmnop'

print reduce(lambda p, m: m(p), moves, myProg)


n_loops = 1000000000

cache = {}
pp = myProg
for i in xrange(n_loops):
    if pp in cache:
        break
    cache[pp] = i
    cache[i] = pp

    pp = reduce(lambda p, m: m(p), moves, pp)

print cache[(n_loops - cache[pp]) % (len(cache) / 2 - cache[pp])]
