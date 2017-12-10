from PrepareData import PrepareData
inputdata = PrepareData.getDataAsStr()


def process(data, rounds):
    a = range(256)
    l_a = len(a)

    i = 0
    skipSize = 0
    for r in range(rounds):
        for x in data:
            subarray = [a[(c + i) % l_a] for c in range(x)]
            rsubarray = subarray[::-1]
            for index, c in enumerate(range(x)):
                a[(c + i) % l_a] = rsubarray[index]

            i += x + skipSize
            skipSize += 1

    return a

data = map(lambda x: int(x), inputdata[0][0].split(','))
print reduce(lambda x,y: x*y, process(data, 1)[:2])

data = map(lambda x: ord(x), inputdata[0][0]) + [17, 31, 73, 47, 23]
pdata = process(data, 64)
hdata = [reduce(lambda x,y: x^y, pdata[i:i+16]) for i in range(0,256,16)]
print ''.join(['{:02x}'.format(x) for x in hdata])
