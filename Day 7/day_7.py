camel_cards = 'input_day_7.txt'

#read lines from the file, split each line, and create a tuple of tuples
hands = tuple((x[0], int(x[1])) for x in map(
    lambda x: x.strip().split(), open(camel_cards).readlines()))

#possible card values
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q', 
'K', 'A']

#calculate the score of a hand
def score(hand, joker=None):
    #count occurrences of each card
    jokers = 0 if joker is None else hand.count(joker)
    chars = sorted(
        (hand.count(x) for x in set(hand) if x != joker), reverse=True)
    chars = [5] if chars == [] else chars
    for (i, x) in enumerate(chars):
        #adjusts for jokers
        n = min(5 - x, jokers)
        jokers -= n
        chars[i] += n
    #generates a string representation of the hand's score
    s = ''.join(str(c) for c in chars).ljust(5, '0')
    for x in hand:
        s += str(0 if x == joker else cards.index(x) + 1).zfill(2)
    return int(s)

#calculate total winnings for a set of hands
def total_winnings(hands, joker=None):
    #sort the hands based on their scores and enumerates them
    sorted_hands = sorted(hands, key=lambda x: score(x[0], joker))
    #sum up the product of the hand's position (index + 1) and its score
    return sum(map(lambda x: (x[0] + 1) * x[1][1], enumerate(sorted_hands)))


#print the total winnings without using any joker
print("1:", total_winnings(hands))
#print the total winnings using 'J' as the joker
print("2:", total_winnings(hands, joker='J'))