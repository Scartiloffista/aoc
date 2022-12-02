import pathlib

path = pathlib.Path(".").parent / "inputs/22.txt"
with open(path, "r") as f:
    player_1, player_2 = f.read().split("\n\n")

player_1 = player_1.splitlines()
player_2 = player_2.splitlines()

player_1, player_2 = list(map(int, player_1[1:])), list(map(int, player_2[1:]))

n_cards = len(player_1) + len(player_2)

debug_count = 1
while player_1 and player_2:
    p1_card, p2_card = player_1[0], player_2[0]
    if p1_card > p2_card:
        player_1 = player_1[1:] + [p1_card] + [p2_card]
        player_2 = player_2[1:]
    else:
        player_2 = player_2[1:] + [p2_card] + [p1_card]
        player_1 = player_1[1:]
    debug_count += 1

points = list(range(n_cards, 0, -1))

if player_1:
    val = sum([i * x for i, x in zip(player_1, points)])
else:
    val = sum([i * x for i, x in zip(player_2, points)])

print(val)
