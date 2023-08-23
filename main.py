with open('calories.txt') as f:
    lines = f.readlines()
    biggest_elf = 0
    temp = 0
    elf_number = 0
    for x in range(len(lines)):
        if lines[x] == "\n":
            elf_number = elf_number + 1
            if temp > biggest_elf:
                biggest_elf_number = elf_number
                biggest_elf = 0 + temp
            temp = 0
        else:
            temp = temp + int(lines[x])
print(f"{biggest_elf} im durchgang {biggest_elf_number}")
            

            

