x = 380

def g(steps):
    location = 0
    for i in xrange(1, steps + 1):
        location = ((location + x) % i) + 1
        yield (i, location)


data = []
for i, location in g(2017):
    data.insert(location, i)
print data[location + 1]


print [i for i,location in g(50000000) if location == 1][-1]
