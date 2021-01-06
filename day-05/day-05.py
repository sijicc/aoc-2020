input = open('input.txt', 'r')
lines = input.read().split("\n")

rows = []
columns = []
ids = []

for line in lines:
    stripped = line.strip("LR").replace("F", "0").replace("B", "1")
    r = int(stripped, 2)
    rows.append(r)

for line in lines:
    stripped = line.strip("FB").replace("R", "1").replace("L", "0")
    c = int(stripped, 2)
    columns.append(c)

i = 0
while i != len(columns):
    binid = (int(rows[int(i)]) * 8) + int(columns[int(i)])
    ids.append(binid)
    i = i + 1
ids.sort()
print("highest id is: " + str(max(ids)))

for seat in range(min(ids), max(ids)):
    if (seat not in ids and (seat + 1) in ids and (seat - 1) in ids):
        print("your seat is: " + str(seat))