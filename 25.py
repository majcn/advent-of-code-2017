from PrepareData import PrepareData
inputdata = PrepareData.fetchData()

import re

start_state =     re.match(r'^Begin in state (\w)\.$',                             inputdata[0]).group(1)
iterations  = int(re.match(r'^Perform a diagnostic checksum after (\d+) steps\.$', inputdata[1]).group(1))

state_program = {}

li = 3
while li < len(inputdata):
    stateI = re.match(r'^In state (\w):$', inputdata[li]).group(1)
    stateVR = (
        re.match(r'^    - Write the value (0|1)\.$',             inputdata[li + 2]).group(1),
        re.match(r'^    - Move one slot to the (left|right)\.$', inputdata[li + 3]).group(1),
        re.match(r'^    - Continue with state (\w)\.$',          inputdata[li + 4]).group(1),

        re.match(r'^    - Write the value (0|1)\.$',             inputdata[li + 6]).group(1),
        re.match(r'^    - Move one slot to the (left|right)\.$', inputdata[li + 7]).group(1),
        re.match(r'^    - Continue with state (\w)\.$',          inputdata[li + 8]).group(1),
    )

    stateV = (
        int(stateVR[0]), 1 if stateVR[1] == 'right' else -1, stateVR[2],
        int(stateVR[3]), 1 if stateVR[4] == 'right' else -1, stateVR[5],
    )

    state_program[stateI] = stateV

    li += 10


from collections import defaultdict
tape = defaultdict(int)
location = 0
state = start_state

for i in xrange(iterations):
    prog = state_program[state]
    if tape[location] == 0:
        tape[location] = prog[0]
        location += prog[1]
        state = prog[2]
    else:
        tape[location] = prog[3]
        location += prog[4]
        state = prog[5]

print sum(tape.values())