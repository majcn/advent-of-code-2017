from PrepareData import PrepareData
inputdata = PrepareData.getDataAsInt()


data = [x[0] for x in inputdata]


steps = 0
loc = 0
while loc < len(data):
    offset = data[loc]

    data[loc] += (1 if offset < 3 else -1)
    steps += 1
    loc += offset
print steps
