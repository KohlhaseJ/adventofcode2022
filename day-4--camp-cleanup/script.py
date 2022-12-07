counterSubset = 0
counterOverlap = 0

with open("C:\\dev\\advent-of-code\\day-4--camp-cleanup\\input.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        range1, range2 = line.split(",")[::1]
        min1, max1 = range1.split("-")
        rangeSet1 = set(range(int(min1), int(max1)+1))
        
        min2, max2 = range2.split("-")
        rangeSet2 = set(range(int(min2), int(max2)+1))

        if rangeSet1.issubset(rangeSet2) or rangeSet2.issubset(rangeSet1):
            counterSubset += 1

        if len(rangeSet1.intersection(rangeSet2)) > 0:
            counterOverlap += 1
        

print("assignment pairs in which one range fully contain the other {}".format(counterSubset))
print("assignment pairs in which one range overlaps the other {}".format(counterOverlap))

