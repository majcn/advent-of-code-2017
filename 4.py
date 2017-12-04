from PrepareData import PrepareData
inputdata = PrepareData.getDataAsStr()


data = inputdata


from itertools import permutations
check = lambda line: not any(1 for x,y in permutations(line, 2) if x == y)

print sum([check(line) for line in data])
print sum([check([sorted(x) for x in line]) for line in data])
