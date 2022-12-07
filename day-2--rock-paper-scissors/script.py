shapeScores = {"X": 1, "Y": 2, "Z": 3}
outcomeMap = {"AX": "Z","AY": "X","AZ": "Y","BX": "X","BY": "Y","BZ": "Z","CX": "Y","CY": "Z","CZ": "X"}
roundOutcomes = {"AX": 3,"AY": 6,"AZ": 0,"BX": 0,"BY": 3,"BZ": 6,"CX": 6,"CY": 0,"CZ": 3}

score = 0

with open("C:\\dev\\advent-of-code\\day-2--rock-paper-scissors\\input.txt", "r") as file:
    for line in file:
        opponent = line[0:1]
        me = line[2:3]
        me = outcomeMap[opponent+me]
        score += shapeScores[me] + roundOutcomes[opponent+me]
        
print("total score of {}".format(score))