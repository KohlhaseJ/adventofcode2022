import helper

class Node():
    def __init__(self, key: str, value: int = 0):
        self.key = key
        self.value = value
        self.parent: Node = None
        self.children = []
    def addNode(self, obj):
        obj.parent = self
        self.children.append(obj)
    def size(self) -> int:
        size = self.value        
        for child in self.children:
            size += child.size()
        return size
    def print(self, level=0):
        tabs = "| " * level
        print("{}{}: {} ({})".format(tabs, self.key, self.value, self.size()))
        for child in self.children:
            child.print(level+1)
    def flat(self):
        nodes = [self]
        for child in self.children:
            nodes.extend(child.flat())
        return nodes



root = Node("/")
currentNode = root
for line in helper.get_input(7):
    line = line.replace("\n", "")
    if line.startswith("$ cd"):
        nextDir = line[5::]
        if nextDir == "/":
            currentNode = root
        elif nextDir == "..":
            currentNode = currentNode.parent
        else:
            currentNode = list(filter(lambda c: c.key == nextDir, currentNode.children))[0]
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        childDir = line[4::]
        currentNode.addNode(Node(childDir))
    else:
        currentNode.value += int(line.split()[0])

root.print()

allNodes = root.flat()
nodeSum = sum([node.size() for node in list(filter(lambda c: c.size() <= 100000, allNodes))])
print("sum of the total sizes {}".format(nodeSum))

totalSpace = 70000000
necessarySpace = 30000000
freeSpace = totalSpace - root.size()
deletable = [node.size() for node in list(filter(lambda c: c.size() >= necessarySpace - freeSpace, allNodes))]
print(min(deletable))