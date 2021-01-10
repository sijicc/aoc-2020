from copy import deepcopy

input = open("input.txt", "r")
input = input.read().split("\n")

fixed = []
for line in input:
    split = line.split(" ")
    fixed.append(split)

#####################################
#              PART 1               #
#####################################

acc = 0
i = 0
iset = set()
while i != len(fixed):
    name = fixed[i][0]
    if name == "jmp":
        if str(fixed[i][1])[:1] == "+":
            i = i + int(fixed[i][1][1:]) - 1
            if int(i) in iset:
                break
            else:
                iset.add(i)
        elif str(fixed[i][1])[:1] == "-":
            i = i - int(fixed[i][1][1:]) - 1
            if int(i) in iset:
                break
            else:
                iset.add(i)

    elif name == "acc":
        if str(fixed[i][1])[:1] == "+":
            acc = acc + int(fixed[i][1][1:])
        if str(fixed[i][1])[:1] == "-":
            acc = acc - int(fixed[i][1][1:])
    elif name == "nop":
        pass

    i = i + 1
print(acc)

#####################################
#              PART 2               #
#####################################


for n in range(len(fixed)):
    changed = deepcopy(fixed)
    if changed[n][0] == "jmp":
        changed[n][0] = "nop"
    elif changed[n][0] == "nop":
        changed[n][0] == "jmp"

    acc = 0
    i = 0
    iset = set()
    while i != len(changed):
        name = changed[i][0]

        if name == "jmp":
            if str(changed[i][1])[:1] == "+":
                i = i + int(changed[i][1][1:]) - 1
                if int(i) in iset:
                    break
                else:
                    iset.add(i)
            elif str(changed[i][1])[:1] == "-":
                i = i - int(changed[i][1][1:]) - 1
                if int(i) in iset:
                    break
                else:
                    iset.add(i)

        elif name == "acc":
            if str(changed[i][1])[:1] == "+":
                acc = acc + int(changed[i][1][1:])
            if str(changed[i][1])[:1] == "-":
                acc = acc - int(changed[i][1][1:])

        i = i + 1
    if i == len(changed):
        print(acc)