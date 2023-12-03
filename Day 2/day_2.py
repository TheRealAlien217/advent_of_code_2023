#Advent of Code -- Day 2: Cube Conundrum

#Determine which games would have been possible if the bag initially contained 12 red cubes, 13 green cubes, and 14 blue cubes.
#Determine the sum of the IDs of the possible games.

#import regex module (for pattern matching in the strings)
import re
import math

game_input = 'puzzle_input_day_2.txt'

def get_min_cubes(sets): #takes a list of sets as an argument
    #initalizes a dictionary with each color and sets each to 0
    maxes = {
        'red': 0,
        'blue': 0,
        'green': 0,
    }
    for set in sets: #iterates through each set in the list of sets
        #splits each set into pairs
        for pairs in set.strip().split(','):
            qty, color = pairs.strip().split()
            if maxes[color] < int(qty):
                maxes[color] = int(qty)
    return math.prod(maxes.values()) #product of the maximum values for each color

#open the file and split each line in the file
with open (game_input, 'r') as f:
    power_sum = 0
    for line in f:
        _, *sets = re.split(';|:', line.strip())

        #calls get_min_cubes and adds the result to the sum
        power_sum+=get_min_cubes(sets)
    print(power_sum)