prioritySum = 0
groupSize = 3
groupItems = [set() for _ in range(groupSize)]

with open("C:\\dev\\advent-of-code\\day-3--rucksack\\input.txt", "r") as file:
    lineCounter = 1

    for line in file:
        groupIndex = lineCounter % groupSize
        groupItems[groupIndex] = set(line.replace("\n", ""))
        
        if lineCounter % groupSize == 0:
            intersectingItems = groupItems[0]
            for i in range(1, groupSize):
                intersectingItems = intersectingItems.intersection(groupItems[i])
            itemType = intersectingItems.pop()
            asciiOrd = ord(itemType)
            priority = asciiOrd - 38
            if asciiOrd >= 97:
                priority = asciiOrd - 96
                
            prioritySum += priority
        
        lineCounter+=1

print("sum of the priorities {}".format(prioritySum))

