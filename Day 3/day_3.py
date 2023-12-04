#--- Day 3: Gear Ratios ---

#Read engine_schematic line by line and find the numbers
#Store the number's positions in the array
#Find the symbols in engine_schematic and store their positions in the array. Remember '.' do not count as symbols
#For each number in the array see if there is a symbol next to, above, below, or diagonally to it.
    #If there is a symbol mark it as true. Else mark as false
#Sum the values of the numbers that were true

engine_schematic = "puzzle_input_day_3.txt"

def main():
    lines = []
    with open(engine_schematic, "r") as input:
        line = input.readline()
        while line:
            lines.append(line.strip("\n"))
            line = input.readline()

    NUM_LINES = len(lines)
    LINE_LEN = len(lines[0])

    # find all numbers in the schematic. store the number and where the number is
    nums = []
    for i in range(len(lines)):
        j = 0
        while j < LINE_LEN:
            if lines[i][j].isdecimal():
                start = j
                num = ""
                while j < LINE_LEN and lines[i][j].isdecimal():
                    num += lines[i][j]
                    j += 1
                j -= 1
                nums.append((int(num), (i, start, j)))

            j += 1

    #checking whether any of the characters the number are symbols. if there is a symbol, add the number to the sum
    sum = 0
    for num in nums:
        part_number = False
        for i in range(num[1][0] - 1, num[1][0] + 2):
            if i >= 0 and i < NUM_LINES:
                for j in range(num[1][1] - 1, num[1][2] + 2):
                    if j >= 0 and j < LINE_LEN:
                        if not (lines[i][j].isdecimal() or lines[i][j] == "."):
                            part_number = True
                            sum += num[0]
                            break
                if part_number:
                    break

    print(sum)


if __name__ == "__main__":
    main()
