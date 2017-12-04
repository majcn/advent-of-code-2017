from PrepareData import PrepareData
inputdata = PrepareData.getDataAsInt()


data = inputdata


print sum([max(line) - min(line) for line in data])

from itertools import permutations
print sum(next(x / y for x, y in permutations(line, 2) if x % y == 0) for line in data)
