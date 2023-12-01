import pathlib
import re

path = pathlib.Path(".") / "19.example.txt"

with open(path, "r") as f:
    lines = f.read().splitlines()

class Blueprint:
    def __init__(self, name, ore_cost, clay_ore_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost):

        self.name = name
        self.ore_cost = ore_cost
        self.clay_ore_cost = clay_ore_cost
        self.obsidian_ore_cost = obsidian_ore_cost
        self.obsidian_clay_cost = obsidian_clay_cost
        self.geode_ore_cost = geode_ore_cost
        self.geode_obsidian_cost = geode_obsidian_cost


inputt = [list(map(int, re.findall("\d+", x))) for x in lines]

blueprints = [Blueprint(*x) for x in inputt]


print(Blueprint)
