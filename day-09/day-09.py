input = open("input.txt", "r")
input = input.read().split("\n")
input = list(map(int, input))

i = 0
mn = 0
sn = 0
sum_list = []
number = 0
sums = set()

for i in range(0, len(input) - 25):
    if i <= len(input) - 6:
        sum_list.extend(input[i:25 + i])
    number = input[25 + i]
    mn = 0
    sn = 0
    while mn != len(sum_list):
        if mn != sn:
            suma = int(sum_list[mn]) + int(sum_list[sn])
            sums.add(suma)
        sn = sn + 1
        if sn == len(sum_list):
            sn = 0
            mn = mn + 1

    if i < len(input) - 26:
        sum_list = []
    if number not in sums:
        break
    sums = set()
    i = i + 1

print(number)

i = 0
x = 1
for x in range(2, 2**64):
    i = 0
    for i in range(0, len(input) - 1):
        test = input[i:i + x]
        f = sum(test)
        if f == number:
            print(min(test) + max(test))
            exit()
        i = i + 1
    x = x + 1
