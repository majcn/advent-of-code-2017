from PrepareData import PrepareData
inputdata = PrepareData.fetchData()


data = inputdata[0]
l_data = len(data)


print sum([int(data[i]) for i in range(l_data) if data[i] == data[(i + 1)          % l_data]])

print sum([int(data[i]) for i in range(l_data) if data[i] == data[(i + l_data / 2) % l_data]])
