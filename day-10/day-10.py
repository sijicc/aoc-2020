input = open("input.txt", "r")
input = input.read().splitlines()
input = list(map(int, input))
input.extend([max(input) + 3, 0])
input.sort()

i = 0
one_diff = 0
three_diff = 0

##################################
#            part one            #
##################################

for i in range(0, len(input)):
    if input[i] - input[i - 1] == 1:
        one_diff = one_diff + 1
    if input[i] - input[i - 1] == 3:
        three_diff = three_diff + 1

##################################
#            part two            #
##################################

input = input[1:-1]
x = [1] + [0]*max(input)
for i in input:
    x[i] = x[i-3] + x[i-2] + x[i-1]


print(three_diff * one_diff)
print(max(x))
