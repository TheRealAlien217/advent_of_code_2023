#Advent of Code -- Day 1: Trebuchet

#What is the problem asking?
#Find the sum of the calibration values for each line in the given document. The calibration value for each line is obtained by taking the first digit and the last digit of that line and combining them to form a two digit number. Repeat this process for every line. Finally add all these two digit numbers up and get the sum.

#Steps
#1. Read the calibration document and process each line to get the first and last digits.
#2. Extract the first and last digits for each line.
#3. Form the two digit numbers for each line
#4. Sum the calibration values
#5. Print the result.
#7. Handle the edge cases where the first and last digits may not be present.

#Open the 'calibration_document.txt' in read mode
calibration_document = 'calibration_document.txt'

combined = []

#Provide a list of the spelled out numbers and map them to their corresponding digits
spelled_out_mapping = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine" : "n9e"}
print(spelled_out_mapping)

with open(calibration_document, 'r') as file:
    #Iterate over each line in the file
    for line in file:

        # Check for spelled-out numbers and replace them with their numeric values
        for word in spelled_out_mapping:
            if word in line:
                line = line.replace(word, spelled_out_mapping[word])

        print(line)

        #find the first digit in the line
        first_digit = next((char for char in line if char.isdigit()), None)

        #find the last digit in the line
        reversed_line = line[::-1] #make the line backwards
        last_digit = next((char for char in reversed_line if char.isdigit()), None)

        #Concatenate First digit and Last digit 
        concatenated_string = str(first_digit) + str(last_digit) #Convert first and last to strings
        concatenated_int = int(concatenated_string) #Convert the concatenated string back to an integer

        combined.append(concatenated_int) #Add the concatenated_int to combined

Total = sum(combined)

print (Total)