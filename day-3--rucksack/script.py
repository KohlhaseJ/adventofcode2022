prioritySum = 0

with open("C:\\dev\\advent-of-code\\day-3--rucksack\\input.txt", "r") as file:
    for line in file:
        compSize = (int)(len(line)/2)
        comp1 = set(line[0:compSize])
        comp2 = set(line[compSize:len(line)-1])

        itemType = comp1.intersection(comp2).pop()
        asciiOrd = ord(itemType)
        priority = asciiOrd - 38
        if asciiOrd >= 97:
            priority = asciiOrd - 96
            
        prioritySum += priority
        

print("sum of the priorities {}".format(prioritySum))

