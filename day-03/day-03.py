input = open('input.txt', 'r')
lines = input.read().splitlines()


def one():
    i = 0
    v = 3
    pos = 0
    trees = 0
    for line in lines:
        lines_len = len(lines[i])
        if line[pos%lines_len] == "#":
            trees = trees + 1
        pos = pos + v
        i = i + 1
    print(trees)

def two():
    speed = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    i = 0
    z = 0
    l = 1
    lines_len = len(lines[i])
    speed_len = len(speed)
    while z != speed_len:
        v = speed[z][0]
        pos = 0
        trees = 0
        for line in lines[::int(speed[z][1])]:
            if line[pos % lines_len] == "#":
                trees = trees + 1
            pos = pos + v
            i = i + 1
        #print(trees)
        z = z + 1
        l = l * trees
    print(l)


one()
two()