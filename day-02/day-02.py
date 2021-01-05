input = open('input.txt', 'r')
lines = input.readlines()

len_lines = len(lines)
def one():
    i = 0
    tc = 0
    while i != len_lines:
        x = lines[i].replace('-', ' ').replace(':', ' ')
        y = x.split()
        min = y[0]
        max = y[1]
        char = y[2]
        passwd = y[3]
        if passwd.count(char) >= int(min) and passwd.count(char) <= int(max):
            tc = tc + 1
        i = i + 1
    print(tc)


def two():
    i = 0
    tc = 0
    while i != len_lines:
        x = lines[i].replace('-', ' ').replace(':', ' ')
        y = x.split()
        poss1 = int(y[0]) - 1
        poss2 = int(y[1]) - 1
        char = y[2]
        passwd = y[3]
        splitpasswd = list(passwd)
        if splitpasswd[poss1] == char and splitpasswd[poss2] != char:
            tc = tc + 1

        if splitpasswd[poss1] == char and splitpasswd[poss2] == char:
            pass

        if splitpasswd[poss1] != char and splitpasswd[poss2] == char:
            tc = tc + 1

        if splitpasswd[poss1] != char and splitpasswd[poss2] != char:
            pass

        i = i + 1
    print(tc)


one()
two()