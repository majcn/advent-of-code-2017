from PrepareData import PrepareData
inputdata = PrepareData.getDataAsStr()


data = [map(lambda x: x.replace(',', ''), d) for d in inputdata]
data = { d[0]: d[2:] for d in data }


groups = []

keys = set(data)
while keys:
    group = set()
    queue = data[next(iter(keys))]

    while queue:
        el = queue.pop()
        if not el in group:
            group.add(el)
            queue += data[el]

    groups.append(group)

    keys -= group


print next(len(g) for g in groups if '0' in g)
print len(groups)
