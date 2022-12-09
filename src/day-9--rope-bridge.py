import helper

class Position():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def touches(self, other):
        xd = abs(self.x - other.x)
        yd = abs(self.y - other.y)
        return max(xd, yd) <= 1

    def follow(self, leader):
        if self.touches(leader):
            return
        
        if self.x == leader.x or self.y != leader.y:
            self.y = self.y + 1 if leader.y > self.y else self.y - 1

        if self.y == leader.y or self.x != leader.x:
            self.x = self.x + 1 if leader.x > self.x else self.x - 1

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, obj):
        return isinstance(obj, Position) and obj.x == self.x and obj.y == self.y

numberOfKnots = 10
positions = [Position(0,0) for _ in range(numberOfKnots)]
mapDict = {}

headIndex = 0
tailIndex = numberOfKnots-1

mapDict[str(positions[tailIndex])] = 1
for line in helper.get_input(9):
    direction, move = line.split(" ")        

    for _ in range(int(move)):
        if direction == "R":
            positions[headIndex].x = positions[headIndex].x + 1
        elif direction == "L":
            positions[headIndex].x = positions[headIndex].x - 1
        elif direction == "U":
            positions[headIndex].y = positions[headIndex].y + 1
        elif direction == "D":
            positions[headIndex].y = positions[headIndex].y - 1

        for pi in range(1, len(positions)):            
            positions[pi].follow(positions[pi-1])
        
        mapDict[str(positions[tailIndex])] = 1

print("visited by tail: {}".format(sum(mapDict.values())))