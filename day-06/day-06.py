input = open("input.txt", "r")
input = input.read().split("\n\n")

def one():
    fixed = []
    y = 0
    for line in input:
        z = line.replace("\n", "")
        fixed.append(z)

    for group in fixed:
        x = set(group)
        z = int(len(x))
        y = y + z

    print(y)


def two():
    fixed = []
    groups_divided = []
    valid_ans = 0
    characters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c" , "v", "b", "n", "m"]
    y = 0
    for line in input:
        x = line.replace("\n", " ")
        fixed.append(x)

    for group in fixed:
        x = group.split()
        groups_divided.append(x)
    for group in groups_divided:
        for character in characters:
            is_character = 0
            for person in group:
                if character in person:
                    is_character += 1
            if is_character == len(group):
                valid_ans += 1
    print(valid_ans)


one()
two()