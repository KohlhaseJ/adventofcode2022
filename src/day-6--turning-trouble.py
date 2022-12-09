import helper

windowSize = 14

for line in helper.get_input(6):
    markerIndex = 0
    for i in range(len(line) - windowSize):
        distinctChars = set(line[i:(windowSize+i)])
        if (len(distinctChars) == windowSize):
            markerIndex = i + windowSize
            break
    print("first marker after {} characters".format(markerIndex))