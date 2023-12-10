#--- Day 8: Haunted Wasteland ---

network = 'input_day_8.txt'

import sys
import numpy as np
from typing import List

#read lines from the file and return a list of strings
def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(network, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            lines.append(line)

    return lines

#part 1
def part_one():
    lines = read_lines_to_list()
    answer = 0

    #extract instructions from the first line of input
    instructions = list(lines.pop(0))
    #discard the next line
    lines.pop(0)

    #dictionary to store nodes and their left and right connections
    nodes = dict()
    curr = "AAA" #starting point

    #populate the nodes dictionary from the input
    for line in lines:
        split = line.split(" = ")
        node = split[0]
        split = split[1].split(", ")
        left = split[0][1:]
        right = split[1][:-1]

        nodes[node] = (left, right)

    #traverse the structure until reaching the end point "ZZZ"
    while curr != "ZZZ":
        for instruction in instructions:
            (left, right) = nodes[curr]
            if instruction == "L":
                curr = left
            else:
                curr = right
            answer += 1

            if curr == "ZZZ":
                break

    print(f"Part 1: {answer}")

#part 2: least common multiple
def part_two():
    lines = read_lines_to_list()

    instructions = list(lines.pop(0))
    lines.pop(0)

    nodes = dict()
    currs = []

    #populate nodes and find nodes ending with "A" to start paths
    for line in lines:
        split = line.split(" = ")
        node = split[0]
        split = split[1].split(", ")
        left = split[0][1:]
        right = split[1][:-1]

        nodes[node] = (left, right)

        if node.endswith("A"):
            currs.append(node)

    endings = []

    #calculate steps for each path and store in the endings list
    for curr in currs:
        curr_answer = 0
        while not curr.endswith("Z"):
            for instruction in instructions:
                (left, right) = nodes[curr]
                if instruction == "L":
                    curr = left
                else:
                    curr = right
                curr_answer += 1

                if curr.endswith("Z"):
                    break
        endings.append(curr_answer)

    #calculate the least common multiple of steps for all paths
    answer = np.lcm.reduce(np.array(endings))
    print(f"Part 2: {answer}")

#run the functions
part_one()
part_two()
