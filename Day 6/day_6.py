#--- Day 6: Wait For It ---

# w = record distance
# f(x) = ax^2 + bx + c
# f(x) = w
# f(x) - w = 0
# 0 = ax^2 + bx + (c - w) 
# x = (-b +/- sqrt(b^2 - 4a(c-w)) / 2a
 
import math
import numpy as np

race_statistics = 'input_day_6.txt'

input = []
with open(race_statistics) as file:
    lines = file.readlines()
    #extract times and distances from race_statistics
    times = [int(x.strip()) for x in lines[0].split(" ") if x.strip().isnumeric()]
    distances = [int(x.strip()) for x in lines[1].split(" ") if x.strip().isnumeric()]
    #create a list of pairs containing time and distance
    for i in range(len(times)):
        input.append([times[i], distances[i]])

#get the winning times using d=distance and t=time
def get_winning_times(d, t):
    #calculate the quadratic equation roots
    x1 = math.floor((d - math.sqrt(d ** 2 - 4 * t)) / 2) + 1
    x2 = math.ceil((d + math.sqrt(d ** 2 - 4 * t)) / 2) - 1
    #return the range of winning times
    return x2 - x1 + 1

#part 1
def part1(input):
    #use NumPy to calculate the product of winning times for each pair
    return np.array([get_winning_times(x[0], x[1]) for x in input]).prod()

#part 2
def part2(input):
    # Construct two integers by concatenating the digits of time and distance
    time_integer = int(''.join([str(x[0]) for x in input]))
    distance_integer = int(''.join([str(x[1]) for x in input]))
    #use the quadratic equation to calculate winning times for the constructed integers
    return get_winning_times(int(''.join([str(x[0]) for x in input])), int(''.join([str(x[1]) for x in input])))

print(f"Part 1: {part1(input)}\nPart 2: {part2(input)}")