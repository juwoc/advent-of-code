elfen = [0, 0, 0]
with open('01/calories.txt') as f:
    lines = f.readlines()
    temp = 0
    for x in range(len(lines)):
        if lines[x] == "\n":
            elfen.sort()
            if temp > elfen[0]:
                elfen[0] = temp
            temp = 0
        else:
            temp = temp + int(lines[x])
print(f"Elfen: {elfen} Total: {sum(elfen)}")


