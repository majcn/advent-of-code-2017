from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

data = inputdata


d_down  = lambda x,y: (x,y+1)
d_up    = lambda x,y: (x,y-1)
d_left  = lambda x,y: (x-1,y)
d_right = lambda x,y: (x+1,y)

class G:
    def __init__(self, data):
        self.data = data

        self.minX, self.maxX = [0, len(data[0]) - 1]
        self.minY, self.maxY = [0, len(data) - 1]

        self.x = next(i for i in range(len(data[0])) if data[0][i] == '|')
        self.y = 0

        self.direction = d_down
        self.steps = 0

    def nextDirection(self):
        c = self.data[self.y][self.x]
        if c != '+':
            return self.direction

        if self.direction in [d_down, d_up]:
            if self.x == self.minX:
                return d_right
            if self.x == self.maxX:
                return d_left
            if self.data[self.y][self.x+1] != ' ':
                return d_right
            if self.data[self.y][self.x-1] != ' ':
                return d_left

        if self.direction in [d_left, d_right]:
            if self.y == self.minY:
                return d_down
            if self.y == self.maxY:
                return d_up
            if self.data[self.y+1][self.x] != ' ':
                return d_down
            if self.data[self.y-1][self.x] != ' ':
                return d_up

    def __iter__(self):
        return self

    def next(self):
        while True:
            c = self.data[self.y][self.x]

            if c == ' ':
                raise StopIteration

            self.direction = self.nextDirection()
            self.x, self.y = self.direction(self.x, self.y)
            self.steps += 1

            if c.isalpha():
                return (self.steps, c)

print reduce(lambda r, x: r + x[1],       G(data), '')
print reduce(lambda r, x: x[0],           G(data),  0)
