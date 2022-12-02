import pathlib
import os

path = pathlib.Path('.').parent / "inputs/5.txt"
with open(path, "r") as f:
    input_tickets = f.read().splitlines()

numbers = []

for number in input_tickets:
    number = number.replace("F", "0")
    number = number.replace("B", "1")
    number = number.replace("L", "0")
    number = number.replace("R", "1")

    numbers.append(int(number, 2))

print(max(numbers))

def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst] 

print(find_missing(sorted(numbers)))