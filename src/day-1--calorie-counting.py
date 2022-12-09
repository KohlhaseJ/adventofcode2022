import helper

calories = [0]
index = 0

for line in helper.get_input(1):
    if line == "" or line == "\n":
        index += 1
        calories.append(0)
    else:
        calories[index] = calories[index] + int(line)

print("The elve carrying the most calories carries {} calories".format(max(calories)))
calories.sort(reverse=True)
print("The top 3 elves are carrying {} calories together".format(calories[0] + calories[1] + calories[2]))