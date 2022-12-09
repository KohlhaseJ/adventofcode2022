import helper

prioritySum = 0

for line in helper.get_input(3):
    compSize = len(line)//2
    comp1 = set(line[0:compSize])
    comp2 = set(line[compSize:len(line)])

    itemType = comp1.intersection(comp2).pop()
    asciiOrd = ord(itemType)
    priority = asciiOrd - 38
    if asciiOrd >= 97:
        priority = asciiOrd - 96
        
    prioritySum += priority
        

print("sum of the priorities {}".format(prioritySum))