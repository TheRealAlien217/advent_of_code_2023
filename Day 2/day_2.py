#Advent of Code -- Day 2: Cube Conundrum

#Determine which games would have been possible if the bag initially contained 12 red cubes, 13 green cubes, and 14 blue cubes.
#Determine the sum of the IDs of the possible games.

#immport regex module (for pattern matching in the strings)
import re

game_input = 'puzzle_input_day_2.txt'

#Set the limits for red, blue, and green
limits = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

#Take the ist of sets and check if the colors meet the limits
def set_valid(sets):
    for set in sets:
        for pairs in set.strip().split(','):
            qty, color = pairs.strip().split()
            #if the pair goes over the limit return false
            if int(qty) > limits[color]:
                return False
    return True

with open (game_input, 'r') as f: #Read the game input file
    id_sum = 0
    #extract the game id of the quantity-color pairs
    for line in f:
        game, *sets = re.split(';|:', line.strip())
        id = game.split()[1]

        #If the set is valid add it to the id sum
        if set_valid(sets):
            id_sum+=(int(id))

            
    print(id_sum)