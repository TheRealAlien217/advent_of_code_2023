#--- Day 4: Scratchcards ---

scratchcards_input = 'puzzle_input_day_4.txt'

scratchcards = open(scratchcards_input, "r") 
#read scatchcards and store them as a list in whole_input
whole_input = scratchcards.readlines() 

#where to store the points for each scratchcard
all_points = []

for line in whole_input: 
    card_points = 0

    winning_numbers = ((line.split(": ")[1]).split(" | ")[0]).split()
    owned_numbers = ((line.split(": ")[1]).split(" | ")[1]).split()

    for number in owned_numbers:
        #if owned number is in winning numbers and card_points is 0 set card points to 1
        if number in winning_numbers and card_points == 0:
            card_points = 1
        #if its in wiining sumbers and card points is not 0 double it
        elif number in winning_numbers:
            card_points *= 2

    #if the scartchcard earned points append the points to all_points
    if card_points != 0:
        all_points.append(card_points)

print(sum(int(i) for i in all_points))