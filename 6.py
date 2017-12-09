from PrepareData import PrepareData
inputdata = PrepareData.getDataAsInt()


data = inputdata[0]
l_data = len(data)


cache = []
while data not in cache:
    cache.append(data[:])

    minV = max(data)
    minI = data.index(minV)

    data[minI] = 0
    for i in range(minV):
        data[(minI + i + 1) % l_data] += 1

print len(cache)
print len(cache) - cache.index(data)
