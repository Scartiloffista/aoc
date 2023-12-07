import pathlib

path = pathlib.Path('.') / "2.txt"
with open(path, "r") as f:
    input_list = f.read().strip().splitlines()

# p1

# only 12 red cubes, 13 green cubes, and 14 blue cubes?
red_cubes = 12
green_cubes = 13
blue_cubes = 14

possible_games = []

split_colon = [i.split(":") for i in input_list]

for game, draws_list in split_colon:
    _, game_number = game.split(" ")
    game_number = int(game_number)
    is_possible = True
    draws = draws_list.strip().split(";")
    for draw in draws:
        balls_list = draw.strip().split(",")
        for balls in balls_list:
            count, colour = balls.strip().split(" ")
            count = int(count)
            if colour == "red":
                if red_cubes < count:
                    is_possible = False
                    break
            elif colour == "green":
                if green_cubes < count:
                    is_possible = False
                    break
            elif colour == "blue":
                if blue_cubes < count:
                    is_possible = False
                    break
    if is_possible:
        possible_games.append(game_number)

        
print(sum(possible_games))

# p2
powers_list = []

for game, draws_list in split_colon:
    max_red = max_green = max_blue = float('-inf')

    _, game_number = game.split(" ")
    game_number = int(game_number)
    is_possible = True
    draws = draws_list.strip().split(";")
    for draw in draws:
        balls_list = draw.strip().split(",")
        for balls in balls_list:
            count, colour = balls.strip().split(" ")
            count = int(count)
            if colour == "red":
                if count > max_red:
                    max_red = count
            elif colour == "green":
                if count > max_green:
                    max_green = count
            elif colour == "blue":
                if count > max_blue:
                    max_blue = count

    power_game = max_red * max_green * max_blue
    powers_list.append(power_game)

print(sum(powers_list))

