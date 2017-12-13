from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

data = [d.split(': ') for d in inputdata]
data = [map(int, d) for d in data]
data = [[d[0], d[1], d[1] * 2 - 2] for d in data]

print sum(d[0] * d[1] for d in data if d[0] % d[2] == 0)

import itertools
print next(i for i in itertools.count() if not any(1 for d in data if (d[0] + i) % d[2] == 0))
