import pathlib

path = pathlib.Path('.') / "2.txt"
with open(path, "r") as f:
    input_list = f.read().strip().splitlines()
#     input_list = """A Y
# B X
# C Z""".strip().splitlines()

mapping = {
    'A' : 1,
    'X' : 1,
    'B' : 2, 
    'Y' : 2,
    'C' : 3, 
    'Z' : 3
}

acc = 0

# for p in input_list:
#     opponent_points, me_points = mapping[p[0]], mapping[p[2]]
#     acc += me_points
#     if opponent_points == me_points:
#         acc += 3
#     else:
#         if me_points == 3 and opponent_points == 1:
#             # io forbici, lui sasso
#             pass
#         elif me_points == 3 and opponent_points == 2:
#             # io forbici, lui carta
#             acc +=  6
#         elif me_points == 2 and opponent_points == 1:
#             # io carta, lui sasso
#             acc +=  6
#         elif me_points == 2 and opponent_points == 3:
#             # io carta, lui forbici
#             pass
#         elif me_points == 1 and opponent_points == 3:
#             # io sasso, lui forbici
#             acc += 6
#         elif me_points == 1 and opponent_points == 2:
#             # io sasso, lui carta
#             pass


# p2


for p in input_list:
    opponent_points, me_points = mapping[p[0]], mapping[p[2]]

    if me_points == 1: # perdere
        if opponent_points == 1: # lui rock
            acc += 3 # io scissors
        elif opponent_points == 2: # lui paper
            acc += 1 # io rock
        else: # lui scissors
            acc += 2 # io paper
    elif me_points == 2: # pareggio
        acc += 3 + opponent_points # punti pareggio piu stessi punti suoi
    else: # vincere
        acc += 6
        if opponent_points == 1: # lui rock
            acc += 2 # io paper
        elif opponent_points == 2: # lui paper
            acc += 3 # io scissors
        else: # lui scissors
            acc += 1 # io rock
        


print(acc)
