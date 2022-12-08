import pathlib


class Node 

path = pathlib.Path('.') / "7.example.txt"

with open(path, "r") as f:
    input_list = f.read().split("\n$") 

sections = [[y.strip() for y in x.splitlines()] for x in input_list][1:]


cwd = "/"

# for i in sections:

    



print(sections)
