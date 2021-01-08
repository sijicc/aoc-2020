input = open("input.txt", "r")
input = input.read().split(".\n")

bags = {}
x = 0

for line in input:
    split = line.replace(" bags", "").replace(" bag", "").replace(".", "").split(" contain ")
    bags.update({split[0]:split[1]})

def one(counted_bag):
    for parent in bags:
        content = bags[parent]
        if counted_bag in content:
            if parent not in bag_list:
                bag_list.append(parent)
            one(parent)

def two(eldest):
    global x
    used_names = []
    content = bags[eldest].split(", ")
    if content[0] == "no other":
        pass
    else:
        for inside in content:
            inside_name = str(inside[2:])
            count = int(inside[0])
            if inside_name not in used_names:
                used_names.append(inside)
                x += count
            for i in range(count):
                two(inside_name)


bag_list = []

one("shiny gold")
two("shiny gold")

print(len(bag_list))
print(x)