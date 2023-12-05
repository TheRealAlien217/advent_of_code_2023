#--- Day 4: Scratchcards ---

scratchcards_input = 'puzzle_input_day_4.txt'

scratchcards = open(scratchcards_input, "r")
#read scatchcards and store them as a list in whole_input
whole_input = scratchcards.readlines()

#initailize all_cards and set each element to 1
all_cards = [1 for i in range(len(whole_input))]

for line in whole_input: 
    #set ard matches to 0
    card_matches = 0

    winning_numbers = ((line.split(": ")[1]).split(" | ")[0]).split()
    owned_numbers = ((line.split(": ")[1]).split(" | ")[1]).split()

    #increment card matches if a number in owned numbers is also i winning numbers and card matches
    for number in owned_numbers:
        if number in winning_numbers:
            card_matches += 1

    for copy in range(all_cards[whole_input.index(line)]):
        a = 1  #a helping valuable for calculating the indexes of the cards that should have a new copy
        for i in range(card_matches):
            all_cards[whole_input.index(line) + a] += 1
            a += 1

print(sum(all_cards))