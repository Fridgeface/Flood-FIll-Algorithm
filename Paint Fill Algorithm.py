#takes in a set of strings that represent a matrix full of different coloured sections depending on the letter associated with that position.
#calculates how many seperate areas there are.
from random import randint


def paintFill():

    xdimension = int(input("Please enter the width of the matrix you would like to test: "))
    ydimension = int(input("Please enter the height of the matrix you would like to test: "))

    ydimension9s = []
    inputstr = []

    for i in range(0, xdimension):
        ydimension9s.append("9")
    range_end = ""
    range_end = int(range_end.join(ydimension9s))
    range_start = int(10 ** (xdimension - 1))

    print(range_end)
    print("This is range start: " + str(range_start))
    print("\n")

    for i in range(0, ydimension):
        inputstr.append(str(randint(range_start, range_end)))

    for i in inputstr:
        print(i)

    if inputstr != 0:

        xDim = len(inputstr[0]) - 1
        yDim = len(inputstr) - 1
        print(xDim)
        print(yDim)
        print("\n")
        checked_points = []
        outputstr = inputstr
        regional_points = []
        counter = 1

        for y in range(0, yDim + 1):
            for x in range(0, xDim + 1):
                regional_points.clear()

                if checked_points.count((x, y)) == 0 and outputstr[y][x] != "0": # checks if master iteration coordinate is already in regional_points from region point finder
                    regional_points.append((x, y))

                    print("Region Number: " + str(counter))
                    counter += 1

                    if len(regional_points) != 0: # checks initial points isnt empty, for first master iteration only

                        for point in regional_points: # for points in regional points

                            print("This is point: " + str(point))
                            print("These points are in this region: " + str(regional_points))

                            current_value = inputstr[point[1]][point[0]] # regional current value
                            print("Current region value: " + str(current_value).upper())

                            if 0 <= point[0] + 1 <= xDim and inputstr[point[1]][point[0] + 1] == current_value and regional_points.count((point[0]+1, point[1])) == 0: # checks if value to the right is the same, if its within constraints of size and if the point to the right is already in initial points (registered in that region)
                                regional_points.append((point[0]+1, point[1]))

                            if 0 <= point[0] - 1 <= xDim and inputstr[point[1]][point[0] - 1] == current_value and regional_points.count((point[0]-1, point[1])) == 0: # checks if value to the left is the same, if its within constraints of size and if the point to the right is already in initial points (registered in that region)
                                regional_points.append((point[0]-1, point[1]))

                            if 0 <= point[1] + 1 <= yDim and inputstr[point[1] + 1][point[0]] == current_value and regional_points.count((point[0], point[1]+1)) == 0: # checks if value below is the same, if its within constraints of size and if the point to the right is already in initial points (registered in that region)
                                regional_points.append((point[0], point[1]+1))

                            if 0 <= point[1] - 1 <= yDim and inputstr[point[1] - 1][point[0]] == current_value and regional_points.count((point[0], point[1]-1)) == 0: # checks if value above is the same, if its within constraints of size and if the point to the right is already in initial points (registered in that region)
                                regional_points.append((point[0], point[1]-1))

                            if checked_points.count((point[0], point[1])) == 0:
                                checked_points.append((point[0], point[1]))

                            variable_outputstr = list(outputstr[point[1]])
                            variable_outputstr[point[0]] = "0"
                            s = ""
                            s = s.join(variable_outputstr)
                            outputstr[point[1]] = s

                            print("\n")

        print("Total number of individual regions: " + str(counter))
        print("\n")
        for i in outputstr:
            print(i)
        #print(checked_points)

paintFill()

