from PrepareData import PrepareData
inputdata = PrepareData.getDataAsStr()


data = inputdata


class TreeNode:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def numOfParents(self):
        if self.parent == None:
            return 0

        return self.parent.numOfParents() + 1

    def isBalanced(self):
        cw = [c.calculateWeight() for c in self.children]
        return len(set(cw)) <= 1

    def calculateWeight(self):
        return self.weight + sum([c.calculateWeight() for c in self.children])


nodes_with_name = {line[0]: TreeNode(line[0], int(line[1].replace('(','').replace(')',''))) for line in data}
for line in data:
    name = line[0]
    children = [x.replace(',','') for x in line[3:]]

    tn_node = nodes_with_name[name]
    for child in children:
        tn_child = nodes_with_name[child]
        tn_child.parent = tn_node
        tn_node.children.append(tn_child)
nodes = nodes_with_name.values()


print next(node.name for node in nodes if node.parent == None)


unbalanced = filter(lambda x: not x.isBalanced(), nodes)
broken = max(unbalanced, key=lambda x: x.numOfParents())

brokenCalculatedWeights = [c.calculateWeight() for c in broken.children]
brokenCalculatedWeightsSet = set(brokenCalculatedWeights)
if len(brokenCalculatedWeights) == 2:
    raise NotImplementedError()
if len(brokenCalculatedWeightsSet) != 2:
    raise Exception("Corrupted data")

brokenWeight, okWeight = sorted(brokenCalculatedWeightsSet, key=lambda x: brokenCalculatedWeights.count(x))

print broken.children[brokenCalculatedWeights.index(brokenWeight)].weight + okWeight - brokenWeight
