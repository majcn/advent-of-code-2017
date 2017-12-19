from PrepareData import PrepareData
inputdata = PrepareData.fetchData()


from collections import defaultdict
registers = defaultdict(int)


import re
regex = re.compile(r'^(\w+) (inc|dec) (-?\d+) if (\w+) (<|<=|>|>=|==|!=) (-?\d+)$')


mmm = 0
for line in inputdata:
    a,b,c,d,e,f = regex.match(line).groups()
    if eval('registers[d] {} {}'.format(e, f)):
        registers[a] += int(c) * (-1 if b == 'dec' else 1)
        mmm = max(mmm, registers[a])

print max(registers.values())
print mmm
