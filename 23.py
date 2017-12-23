from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

data = inputdata

import re
from collections import defaultdict

class Program:
    def __init__(self, progs):
        self.reg = defaultdict(int)
        self.location = 0

        self.progs = progs

    def __iter__(self):
        return self

    def getValue(self, v):
        return int(v) if not v.isalpha() else self.reg[v]

    def set(self, x, y):
        self.reg[x] = self.getValue(y)

    def sub(self, x, y):
        self.reg[x] -= self.getValue(y)

    def mul(self, x, y):
        self.reg['mul_count'] += 1
        self.reg[x] *= self.getValue(y)

    def jnz(self, x, y):
        if self.getValue(x) != 0:
            self.location += self.getValue(y) - 1

    def next(self):
        if self.location < 0 or self.location >= len(self.progs):
            raise StopIteration

        self.progs[self.location](self)
        self.location += 1

        return self.reg['mul_count']


class Program2(Program):
    def __init__(self, progs):
        Program.__init__(self, progs)
        self.reg['a'] = 1
        self.reg['f'] = 1

    def next(self):
        while True:
            if self.location < 0 or self.location >= len(self.progs):
                raise StopIteration

            self.progs[self.location](self)
            self.location += 1

            if self.location == 8:
                self.location = 26
                if not self.isPrime(self.reg['b']):
                    return self.reg['b']

    @staticmethod
    def isPrime(n):
        if (n <= 1): return False
        elif (n <= 3): return True
        elif (n % 2 == 0 or n % 3 == 0): return False

        i = 5
        while i * i <= n:
            if (n % i == 0 or n % (i + 2) == 0): return False
            i += 6

        return True

import re
types = [
    (r'^set (\w) (-?[a-z0-9]+)$', lambda p,args: p.set(*args)),
    (r'^sub (\w) (-?[a-z0-9]+)$', lambda p,args: p.sub(*args)),
    (r'^mul (\w) (-?[a-z0-9]+)$', lambda p,args: p.mul(*args)),
    (r'^jnz (\w) (-?[a-z0-9]+)$', lambda p,args: p.jnz(*args)),
]

progs = [lambda p, f=f, args=re.match(r, d).groups(): f(p, args) for d in data for r,f in types if re.match(r, d)]

p1 = Program(progs)
print reduce(lambda x,y: y, p1)

p2 = Program2(progs)
print len([1 for x in p2])

b = 107900
c = 124900
step = 17
print len([1 for x in range(b, c+1, step) if not Program2.isPrime(x)])
