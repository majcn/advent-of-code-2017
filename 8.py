from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

import re
# print inputdata

registers = {}

aaa = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+) (<|<=|>|>=|==|!=) (-?\d+)')
for line in inputdata:
    a,b,c,d,e,f = aaa.match(line).groups()
    registers[a] = 0
    registers[d] = 0
    # print a,b,c,d,e,f

mmm = 0
for line in inputdata:
    a,b,c,d,e,f = aaa.match(line).groups()
    if eval('registers[d] ' + e + ' ' + f):
        registers[a] += int(c) * (-1 if b == 'dec' else 1)
        if mmm < registers[a]:
            mmm = registers[a]

print registers
print max(registers.values())
print mmm