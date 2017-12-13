from PrepareData import PrepareData
inputdata = PrepareData.getDataAsStr()

data = [[int(x[0].replace(':', '')), int(x[1])] for x in inputdata]

class Layer:

    def __init__(self, r):
        self.r = r
        self.i = 1 if r > 0 else 0
        self.direction = 1

    def move(self):
        if self.r < 1:
            return

        if self.i == self.r:
            self.direction = -1

        if self.i == 1:
            self.direction = 1

        self.i += self.direction

    def isIOne(self):
        return self.i == 1

    def copy(self):
        r = Layer(0)
        r.r = self.r
        r.i = self.i
        r.direction = self.direction
        return r

maxLayers = data[-1][0] + 1
layers = [Layer(next((x[1] for x in data if x[0] == i), 0)) for i in range(maxLayers)]

def getCaughtGen(layers):
    copyLayers = [l.copy() for l in layers]

    for i in range(len(copyLayers)):
        if copyLayers[i].isIOne():
            yield [i, copyLayers[i].r]

        [l.move() for l in copyLayers]


print sum(map(lambda x: x[0] * x[1], getCaughtGen(layers)))


delay = 0
while True:
    if not next(getCaughtGen(layers), None):
        break

    [l.move() for l in layers]
    delay += 1

print delay