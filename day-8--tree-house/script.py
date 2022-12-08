map = []
visibleElements = 0
maxScenicScore = 0

with open("C:\\dev\\advent-of-code\\day-8--tree-house\\input.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if len(line) > 0:
            map.append([int(ch) for ch in line])

#visibleElements += len(map)*2 + len(map[0])*2 - 4

for ri in range(len(map)):
    for ci in range(len(map[0])):
        element = map[ri][ci]
        left = map[ri][:ci]
        right = map[ri][ci+1:]
        top = [row[ci] for row in map[:ri]]
        bottom = [row[ci] for row in map[ri+1:]]
        
        isVisible = 0
        if element > max(left or [-1]) or element > max(right or [-1]) or element > max(top or [-1]) or element > max(bottom or [-1]):
            visibleElements += 1
            isVisible = 1

        scenicScore = 0
        scoresLeft = [i+1 for i, ele in enumerate(list(reversed(left))) if ele >= element]
        scoresRight = [i+1 for i, ele in enumerate(right) if ele >= element]
        scoresTop = [i+1 for i, ele in enumerate(list(reversed(top))) if ele >= element]
        scoresBottom = [i+1 for i, ele in enumerate(bottom) if ele >= element]

        scoreLeft = scoresLeft[0] if len(scoresLeft) > 0 else len(left) if len(left) > 0 else 0
        scoreRight = scoresRight[0] if len(scoresRight) > 0 else len(right) if len(right) > 0 else 0
        scoreTop = scoresTop[0] if len(scoresTop) > 0 else len(top) if len(top) > 0 else 0
        scoreBottom = scoresBottom[0] if len(scoresBottom) > 0 else len(bottom) if len(bottom) > 0 else 0
        
        scenicScore += scoreLeft * scoreRight * scoreTop * scoreBottom

        maxScenicScore = max(scenicScore, maxScenicScore)


print("visibleElements: {}".format(visibleElements))
print("maxScenicScore: {}".format(maxScenicScore))

