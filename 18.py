from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

data = inputdata

import re
from collections import defaultdict

class Program:
    def __init__(self, progs):
        self.reg = defaultdict(int)
        self.location = 0
        self.waitForData = False

        self.progs = progs

    def __iter__(self):
        return self

    def getValue(self, v):
        return int(v) if not v.isalpha() else self.reg[v]

    def set(self, x, y):
        self.reg[x] = self.getValue(y)

    def add(self, x, y):
        self.reg[x] += self.getValue(y)

    def mul(self, x, y):
        self.reg[x] *= self.getValue(y)

    def mod(self, x, y):
        self.reg[x] %= self.getValue(y)

    def jgz(self, x, y):
        if self.getValue(x) > 0:
            self.location += self.getValue(y) - 1

    def snd(self, x):
        self.reg['snd'] = self.getValue(x)

    def rcv(self, x):
        if self.getValue(x) != 0:
            self.reg['rcv'] = self.reg['snd']
            self.location = -10

    def getResult(self):
        return self.reg['rcv']

    def next(self):
        if self.location < 0 or self.location >= len(self.progs):
            raise StopIteration

        self.progs[self.location](self)
        if not self.waitForData:
            self.location += 1

        return self.getResult()


class Program2(Program):
    def __init__(self, progs, id):
        Program.__init__(self, progs)
        self.message_queue = []
        self.reg['p'] = id
        self.send_counter = 0

        self.sendTo = None

    def snd(self, x):
        self.sendTo.message_queue.append(str(self.getValue(x)))
        self.send_counter += 1

    def rcv(self, x):
        if self.message_queue:
            self.set(x, self.message_queue.pop(0))
            self.waitForData = False
        else:
            self.waitForData = True

    def getResult(self):
        if self.waitForData and self.sendTo.waitForData:
            raise StopIteration

        return self.send_counter

import re
types = [
    (r'^set (\w) (-?[a-z0-9]+)$',          lambda p,args: p.set(*args)),
    (r'^add (\w) (-?[a-z0-9]+)$',          lambda p,args: p.add(*args)),
    (r'^mul (\w) (-?[a-z0-9]+)$',          lambda p,args: p.mul(*args)),
    (r'^mod (\w) (-?[a-z0-9]+)$',          lambda p,args: p.mod(*args)),
    (r'^jgz (-?[a-z0-9]+) (-?[a-z0-9]+)$', lambda p,args: p.jgz(*args)),
    (r'^snd (-?[a-z0-9]+)$',               lambda p,args: p.snd(*args)),
    (r'^rcv (-?[a-z0-9]+)$',               lambda p,args: p.rcv(*args))
]

progs = [lambda p, f=f, args=re.match(r, d).groups(): f(p, args) for d in data for r,f in types if re.match(r, d)]
p1 = Program(progs)
print reduce(lambda x,y: y, p1)


p_0 = Program2(progs, 0)
p_1 = Program2(progs, 1)

p_0.sendTo = p_1
p_1.sendTo = p_0

print [r_1 for r_0, r_1 in zip_longest(p_0, p_1)][-1]
