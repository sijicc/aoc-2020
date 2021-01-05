input = open('input.txt', 'r')
lines = input.readlines()
def one():
    main_number = 0
    number_added = 0
    i = 0
    len_lines = len(lines) - 1
    while lines[number_added] != len_lines or lines[main_number] != len_lines:
        sum = int(lines[main_number]) + int(lines[number_added])
        i = i + 1
        if sum == 2020:
            multiplied = int(lines[main_number]) * int(lines[number_added])
            print(sum)
            print(int(lines[main_number]))
            print(int(lines[number_added]))
            print(multiplied)
            break
        number_added = 1 + number_added
        if number_added == len_lines:
            number_added = 0
            main_number = main_number + 1
        if main_number == len_lines:
            print(i)
            break


def two():
    main_number = 0
    second_number = 0
    third_number = 0
    i = 0
    len_lines = len(lines) - 1
    while lines[main_number] != len_lines:
        sum = int(lines[main_number]) + int(lines[second_number]) + int(lines[third_number])
        i = i + 1
        if sum == 2020:
            multiplied = int(lines[main_number]) * int(lines[second_number]) * int(lines[third_number])
            print(sum)
            print(int(lines[main_number]))
            print(int(lines[second_number]))
            print(int(lines[third_number]))
            print(multiplied)
            print(str(i) + "i")
            break
        third_number = 1 + third_number
        if third_number == len_lines:
            third_number = 0
            second_number = second_number + 1
        if second_number == len_lines:
            third_number = 0
            second_number = 0
            main_number = main_number + 1
        i = i + 1

two()
