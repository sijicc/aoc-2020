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
        for character in range(0, len(newest_data[line])):
            line_sum = []
            sum_of_seats_around = 0
            c1, c2, c3, c4, c5, c6, c7, c8 = False, False, False, False, False, False, False, False
            for x in range(1, 100):
                try:
                    if newest_data[line + x][character] != "." and c1 is False:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line + x][character])
                        c1 = True
                except IndexError:
                    pass
                try:
                    if newest_data[line + x][character + x] != "." and c2 is False:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line + x][character + x])
                        c2 = True
                except IndexError:
                    pass
                try:
                    if newest_data[line + x][character - x] != "." and c3 is False and character - x >= 0:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line + x][character - x])
                        c3 = True
                except IndexError:
                    pass

                try:
                    if newest_data[line - x][character] != "." and c4 is False and line - x >= 0:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line - x][character])
                        c4 = True
                except IndexError:
                    pass
                try:
                    if newest_data[line - x][character + x] != "." and c5 is False and line - x >= 0:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line - x][character + x])
                        c5 = True
                except IndexError:
                    pass
                try:
                    if newest_data[line - x][character - x] != "." and c6 is False and line - x >= 0 and character - x >= 0:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line - x][character - x])
                        c6 = True
                except IndexError:
                    pass
                try:
                    if newest_data[line][character + x] != "." and c7 is False:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line][character + x])
                        c7 = True
                except IndexError:
                    pass
                try:
                    if newest_data[line][character - x] != "." and c8 is False and character - x >= 0:
                        sum_of_seats_around = sum_of_seats_around + int(newest_data[line][character - x])
                        c8 = True
                except IndexError:
                    pass


            if newest_data[line][character] == ".":
                x = newest_data[line][character]
                temp_list.extend(str(x))

            elif sum_of_seats_around == 0 and newest_data[line][character] != ".":
                x = newest_data[line][character].replace("0", "1")
                temp_list.extend(str(x))

            elif sum_of_seats_around >= 5 and newest_data[line][character] != ".":
                x = newest_data[line][character].replace("1", "0")
                temp_list.extend(str(x))

            elif 0 < sum_of_seats_around < 5 and newest_data[line][character] != ".":
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


