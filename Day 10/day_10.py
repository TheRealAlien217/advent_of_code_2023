#--- Day 10: Pipe Maze ---

import math

pipes = "input_day_10.txt"

#define a dictionary mapping directions to step changes
dir_to_step: dict[str, tuple[int, int]] = {
        "^": (-1, 0),
        "<": (0, -1),
        "v": (1, 0),
        ">": (0, 1),
}

#define a dictionary mapping current and next direction to the next direction when encountering certain pipe characters
next_dir_dict: dict[tuple[str, str], str] = {
        ("|", "^"): "^",
        ("|", "v"): "v",
        ("-", "<"): "<",
        ("-", ">"): ">",
        ("L", "v"): ">",
        ("L", "<"): "^",
        ("J", "v"): "<",
        ("J", ">"): "^",
        ("7", "^"): "<",
        ("7", ">"): "v",
        ("F", "^"): ">",
        ("F", "<"): "v",
}

#define a set of characters representing different types of pipes
pipe_characters: set[str] = {"|", "-", "L", "J", "7", "F"}

#define a function to check if a given direction and pipe character connect
def connects(dir: str, pipe: str) -> bool:
    return next_dir_dict.get((pipe, dir)) is not None

#define a function to get the next direction given the current direction and pipe character
def next_dir(dir: str, pipe: str) -> str:
    return next_dir_dict[(pipe, dir)]

#define a function to add two tuples element-wise
def add_tuples(t1, t2) -> tuple[int, int]:
    return tuple(i1 + i2 for i1, i2 in zip(t1, t2))

#define a function to set the character at a given index in the grid
def set_idx(idx: tuple[int, int], character: str):
    lines[idx[0]][idx[1]] = character

#define a function to get the character at a given index in the grid
def get_idx(idx: tuple[int, int]) -> str:
    return lines[idx[0]][idx[1]]

#define a function to check if a given index is within the grid boundaries
def idx_in_grid(idx: tuple[int, int]) -> bool:
    return 0 <= idx[0] and idx[0] < len(lines) and 0 <= idx[1] and idx[1] < len(lines[0])

#open the file containing the pipe maze and create a list of lists representing the grid
with open(pipes, "r") as file:
    lines = [list(line.rstrip()) for line in file]

#find the starting index (S) in the grid
s_idx = (0, 0)
for i, line in enumerate(lines):
    for j, character in enumerate(line):
        if character == "S":
            s_idx = (i, j)

#initialize the integral variable
integral = 0

#initialize the position tuple with an empty direction and the starting index
pos: tuple[str, tuple[int, int]] = ("", (0,0))

#iterate through directions and steps to find the initial position
for dir, step in dir_to_step.items():
    next_idx = add_tuples(s_idx, step)
    next_character = get_idx(next_idx)
    if next_character in pipe_characters and connects(dir, next_character):
        pos = (next_dir_dict[(next_character, dir)], next_idx)
        integral -= step[1] * next_idx[0]
        break

#initialize the steps variable
steps = 1

#loop for traversing the pipe maze
while True:
    print(f"integral {integral}")

    #increment the steps counter
    steps += 1

    #print the current position
    print(pos)
    dir, idx = pos
    character = get_idx(idx)

    #determine the step change based on the current direction
    step = dir_to_step[dir]
    #calculate the next index by adding the current index and the step
    next_idx = add_tuples(idx, step)
    #update the integral value based on the movement
    integral -= step[1] * next_idx[0]
    print(f"next_idx {next_idx}")
    #check if the next index is within the grid boundaries
    if not idx_in_grid(next_idx):
        print("Next idx not in grid!")
        break

    #get the character at the next index
    next_character = get_idx(next_idx)
    print("next_character {next_character}")
    if next_character == "S":
        #calculate the net value and print the results for both parts of the puzzle
        net = abs(integral) - int(steps/2) + 1
        print(f"steps {steps}")
        print(f"Part 1 answer: {math.ceil(steps / 2)}")
        print(f"integral {integral}")
        print(f"Part 2 answer: {net}")
        break

    #check if the next character is a valid pipe character and connects to the current direction
    if not(next_character in pipe_characters and connects(dir, next_character)):
        print("Failed to continue!")
        break

    #update the position with the next direction and index
    pos = (next_dir_dict[(next_character, dir)], next_idx)