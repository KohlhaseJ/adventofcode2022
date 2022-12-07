windowSize = 14

with open("C:\\dev\\advent-of-code\\day-6--turning-trouble\\input.txt", "r") as file:
    for line in file:
        markerIndex = 0
        for i in range(len(line) - windowSize):
            distinctChars = set(line[i:(windowSize+i)])
            if (len(distinctChars) == windowSize):
                markerIndex = i + windowSize
                break
        print("first marker after {} characters".format(markerIndex))

