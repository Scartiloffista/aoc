import pathlib
from collections import deque
import itertools


def main(p1, p2):
    count = 1
    set_previous_games = set()
    # set_previous_games.add((p1, p2))
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in set_previous_games:
            # todo implement win p1
            return 1, p1
        else:
            set_previous_games.add((tuple(p1), tuple(p2)))
            p1_card, p2_card = p1.popleft(), p2.popleft()
            if p1_card <= len(p1) and p2_card <= len(p2):
                new_p1 = deque(itertools.islice(p1, 0, p1_card))
                new_p2 = deque(itertools.islice(p2, 0, p2_card))
                ret, _ = main(new_p1, new_p2)
                if ret == 1:
                    p1.append(p1_card)
                    p1.append(p2_card)
                else:
                    p2.append(p2_card)
                    p2.append(p1_card)
            # else:
            elif p1_card > p2_card:
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                p2.append(p2_card)
                p2.append(p1_card)
        count += 1
    if p1:
        return 1, p1
    else:
        return 2, p2


path = pathlib.Path(".").parent / "inputs/22.txt"
with open(path, "r") as f:
    player_1, player_2 = f.read().split("\n\n")

player_1 = player_1.splitlines()
player_2 = player_2.splitlines()

player_1, player_2 = deque(map(int, player_1[1:])), deque(map(int, player_2[1:]))

n_cards = len(player_1) + len(player_2)


winner, deck = main(player_1, player_2)
points = list(range(n_cards, 0, -1))
val = sum([i * x for i, x in zip(deck, points)])

print(val)
