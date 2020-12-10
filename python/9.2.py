import pathlib
import os

path = pathlib.Path('.').parent / "inputs/9.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

list_numbers = [int(x) for x in lines]

    def evaluate22(numbers):
        value = 133015568
        start = 0
        end = 1
        acc = numbers[0]
        while True:
            acc += numbers[end]
            if acc < value:
                end += 1
            elif acc > value:
                acc -= numbers[start]
                acc -= numbers[end]
                start +=1
            else:
                return start, end

start, end = evaluate22(list_numbers)
minn, maxx = min(list_numbers[start:end]), max(list_numbers[start:end])
print(minn + maxx)
