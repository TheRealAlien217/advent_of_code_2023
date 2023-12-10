#--- Day 9: Mirage Maintenance ---

from itertools import pairwise

oasis_data = 'input_day_9.txt'

#calculate the next reading based on a specific pattern
def next_reading(reading_set):
    #if all values in the reading_set are the same, return that value
    if len(set(reading_set)) == 1:
        return reading_set[0]
    #otherwise, calculate the next reading using differences between consecutive values
    return reading_set[-1] + next_reading([x[1] - x[0] for x in pairwise(reading_set)])

#open and read data
with open(oasis_data, "r") as file:
    #convert each line of the file to a list of integers
    readings = [[int(val) for val in line.split(" ")] for line in file.readlines()]
    #initialize lists to store results for Part One and Part Two
    p1_results = []
    p2_results = []
    #iterate through each reading_set in the readings list
    for reading_set in readings:
        #calculate the result for Part One and append it to p1_results
        p1_results.append(next_reading(reading_set))
        #calculate the result for Part Two (reversed order) and append it to p2_results
        p2_results.append(next_reading(reading_set[::-1]))
    
    #print the sum of results for Part One and Part Two
    print(f"Part One : {sum(p1_results)}")
    print(f"Part Two : {sum(p2_results)}")