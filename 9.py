from PrepareData import PrepareData
inputdata = PrepareData.getDataAsStr()


data = inputdata[0][0]


groupLevel = 0
isGarbage = False
ignoreNext = False
score = 0
garbage = 0

for x in data:
    if ignoreNext:
        ignoreNext = False
        continue

    if x == '!':
        ignoreNext = True
        continue

    if not isGarbage and x == '<':
        isGarbage = True
        continue

    if x == '>':
        isGarbage = False
        continue


    if isGarbage:
        garbage += 1

    if not isGarbage and x == '{':
        groupLevel += 1
        score += groupLevel

    if not isGarbage and x == '}':
        groupLevel -= 1

print score
print garbage
