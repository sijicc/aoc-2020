with open("input.txt", "r") as f:
    data = f.read().splitlines()
print(data)

#sn > 0 = north
#sn < 0 = south

sn = 0
we = 0
r = 90
wpsn = 1
wpwe = 10

for direction in data:
    if direction[0] == "S":
        sn = sn - int(direction[1:])
    elif direction[0] == "N":
        sn = sn + int(direction[1:])
    elif direction[0] == "W":
        we = we - int(direction[1:])
    elif direction[0] == "E":
        we = we + int(direction[1:])
    elif direction[0] == "L":
        r = r - int(direction[1:])
    elif direction[0] == "R":
        r = r + int(direction[1:])
    elif direction[0] == "F":
        if r%360 == 0:
            sn = sn + int(direction[1:])
        elif r%360 == 90:
            we = we + int(direction[1:])
        elif r%360 == 180:
            sn = sn - int(direction[1:])
        elif r%360 == 270:
            we = we - int(direction[1:])

print(str(we) + "we")
print(str(sn) + "sn")
print(abs(we) + abs(sn))

sn = 0
we = 0

for direction in data:
    if direction[0] == "S":
        wpsn = wpsn - int(direction[1:])
    elif direction[0] == "N":
        wpsn = wpsn + int(direction[1:])
    elif direction[0] == "W":
        wpwe = wpwe - int(direction[1:])
    elif direction[0] == "E":
        wpwe = wpwe + int(direction[1:])
    elif direction[0] == "L":
        if direction[1:] == "90":
            x = wpwe
            y = wpsn
            wpwe = -y
            wpsn = x
        elif direction[1:] == "180":
            wpwe = -wpwe
            wpsn = -wpsn
        elif direction[1:] == "270":
            x = wpwe
            y = wpsn
            wpwe = y
            wpsn = -x
    elif direction[0] == "R":
        if direction[1:] == "90":
            x = wpwe
            y = wpsn
            wpwe = y
            wpsn = -x
        elif direction[1:] == "180":
            wpwe = -wpwe
            wpsn = -wpsn
        elif direction[1:] == "270":
            x = wpwe
            y = wpsn
            wpwe = -y
            wpsn = x

    elif direction[0] == "F":
        sn = sn + (int(direction[1:]) * wpsn)
        we = we + (int(direction[1:]) * wpwe)

print(str(we) + "we")
print(str(sn) + "sn")
print(abs(we) + abs(sn))


