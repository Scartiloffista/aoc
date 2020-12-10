import pathlib
import os

path = pathlib.Path('.').parent / "inputs/10.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

list_numbers = sorted([int(x) for x in lines])


# p1
sum_diff_1 = 1
sum_diff_3 = 1

for i in range(len(list_numbers)-1):
    a = list_numbers[i+1]
    b = list_numbers[i]
    if a - b == 1:
        sum_diff_1 += 1
    elif a - b == 3:
        sum_diff_3 += 1

print(sum_diff_1 * sum_diff_3)

# p2
list_of_combination = [0] * len(list_numbers)
enumeration = list(enumerate(list_numbers))
for i, x in enumeration:
    actual_adapter = x
    start = i-3 if i > 3 else 0  # just looking for optimization?
    
    candidates = [j for j, x in enumeration[start:i]
                  if actual_adapter - 3 <= x <= actual_adapter-1]

    list_of_combination[i] = sum([list_of_combination[j] for j in candidates])
    
    if 0 <= actual_adapter <= 3:
        list_of_combination[i] += 1
    pass

print(list_of_combination[-1])
