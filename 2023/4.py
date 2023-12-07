import pathlib

path = pathlib.Path('.') / "4.txt"
with open(path, "r") as f:
    input_list = f.read().strip().splitlines()
    input_list = [x.strip() for x in input_list]

res = 0

# for line in input_list:
#     _, numbers = line.split(":")
#     winning, having = numbers.strip().split("|")
#     winning = winning.strip().split(" ")
#     having = having.strip().split(" ")
#     winning = set([int(i) for i in winning if i != ""])
#     having = set([int(i) for i in having if i != ""])
#     intersectionn = winning.intersection(having)
#     power = len(intersectionn)-1

#     value = 0 if power < 0 else 2 ** power

#     res += value
#     pass

# print(int(res))

copies_of_cards = {} # int -> int

for line in input_list:
    card, numbers = line.split(":")
    _, card = card.strip().split()
    card = int(card.strip())

    copies_of_cards[card] = copies_of_cards.get(card, 0) + 1
    number_of_copies_of_this_card = copies_of_cards[card]

    winning, having = numbers.strip().split("|")
    winning = winning.strip().split(" ")
    having = having.strip().split(" ")
    winning = set([int(i) for i in winning if i != ""])
    having = set([int(i) for i in having if i != ""])
    intersectionn = winning.intersection(having)

    for i in range(card+1, card+len(intersectionn)+1):
        copies_of_cards[i] = copies_of_cards.get(i, 0) + number_of_copies_of_this_card
    
print(sum(copies_of_cards.values()))
