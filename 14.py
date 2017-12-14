inputdata = 'ljoxqyyw'
size = 128

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

r = []
for i in range(size):
    data = map(lambda x: ord(x), (inputdata + '-' + str(i))) + [17, 31, 73, 47, 23]
    pdata = process(data, 64)
    hdata = [reduce(lambda x,y: x^y, pdata[i:i+16]) for i in range(0,256,16)]
    nhdata = ''.join(map(lambda x: bin(x)[2:].zfill(8), hdata))
    r.append(map(int, nhdata))

print sum(map(sum, r))


group_count = 2
full_queue = [[(x,y)] for x in range(size) for y in range(size)]
for queue in full_queue:
    while queue:
        x, y = queue.pop()
        if r[x][y] != 1:
            continue

        left =   ((x-1,y), r[x-1][y] if x > 0 else 0)
        right =  ((x+1,y), r[x+1][y] if x < (size - 1) else 0)
        top =    ((x,y-1), r[x][y-1] if y > 0 else 0)
        bottom = ((x,y+1), r[x][y+1] if y < (size - 1) else 0)

        neighbours = [left, right, top, bottom]
        queue += [n[0] for n in neighbours if n[1] == 1]
        g = next((n[1] for n in neighbours if n[1] > 1), None)

        if not g:
            g = group_count
            group_count += 1

        r[x][y] = g

print group_count - 2