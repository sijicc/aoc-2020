data = open("input.txt", "r")
data = data.read().splitlines()

new_data = []
newer_data = []
line_sum = []
sum_of_seats_around = 0
seat_count = 0

for line in data:
    new_line = line.replace("L", "0").replace("#", "1")
    new_data.append(new_line)

newest_data = new_data

while True:
    newer_data = []
    print(str(newest_data) + " NEWEST DATA")
    for line in range(0, len(newest_data)):
        temp_list = []
        print("###########################")
        print(newest_data[line])
        print("###########################")
        for character in range(0, len(newest_data[line])):
            line_sum = []
            try:
                c0 = newest_data[line][character + 1]
                line_sum.extend(c0)
            except IndexError:
                pass
            try:
                if character - 1 >= 0:
                    c1 = newest_data[line][character - 1]
                    line_sum.extend(c1)
            except IndexError:
                pass
            try:
                c2 = newest_data[line + 1][character]
                line_sum.extend(c2)
            except IndexError:
                pass
            try:
                c3 = newest_data[line + 1][character + 1]
                line_sum.extend(c3)
            except IndexError:
                pass
            try:
                if character - 1 >= 0:
                    c4 = newest_data[line + 1][character - 1]
                    line_sum.extend(c4)
            except IndexError:
                pass
            try:
                if line - 1 >= 0:
                    c5 = newest_data[line - 1][character]
                    line_sum.extend(c5)
            except IndexError:
                pass
            try:
                if line - 1 >= 0:
                    c6 = newest_data[line - 1][character + 1]
                    line_sum.extend(c6)
            except IndexError:
                pass
            try:
                if line - 1 >= 0 and character - 1 >= 0:
                    c7 = newest_data[line - 1][character - 1]
                    line_sum.extend(c7)
            except IndexError:
                pass
            sum_of_seats_around = 0
            print(line_sum)
            for ele in line_sum:
                if ele != ".":
                    sum_of_seats_around = sum_of_seats_around + int(ele)

            if newest_data[line][character] == ".":
                print("dot")
                x = newest_data[line][character]
                temp_list.extend(str(x))

            elif sum_of_seats_around == 0 and newest_data[line][character] != ".":
                #print(str(sum_of_seats_around) + " sum_of_seats_around == 0")
                print(sum_of_seats_around)
                print("0 to 1")
                x = newest_data[line][character].replace("0", "1")
                temp_list.extend(str(x))

            elif sum_of_seats_around >= 4 and newest_data[line][character] != ".":
                #print(str(sum_of_seats_around) + " sum_of_seats_around >= 4")
                print(sum_of_seats_around)
                print("1 to 0")
                x = newest_data[line][character].replace("1", "0")
                temp_list.extend(str(x))

            elif 0 < sum_of_seats_around < 4 and newest_data[line][character] != ".":
                #print("ELSE")
                print(sum_of_seats_around)
                print("keep value")
                x = newest_data[line][character]
                temp_list.extend(str(x))

        y = ''.join(temp_list)
        newer_data.append(y)
    print(str(newer_data) + " NEWER DATA")
    if newest_data == newer_data:
        for ele in newest_data:
            for char in ele:
                if char != ".":
                    seat_count = seat_count + int(char)
        for ele in newer_data:
            print(ele)
        print(seat_count)
        exit()
    newest_data = newer_data


