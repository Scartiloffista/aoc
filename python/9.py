import pathlib
import os

path = pathlib.Path('.').parent / "inputs/9.txt"
with open(path, "r") as f:
    lines = f.read().splitlines()

list_numbers = [int(x) for x in lines]
preamble_size = 25
first_preamble = list_numbers[:25]
rest_of_list = list_numbers[25:]

def get_couples(list):
    return [(a,b) for a in list for b in list if a != b]

def evaluate(preamble, listt: list):
    if list == []:
        return None
    couples = get_couples(preamble)
    value = listt[0]
    flag = any(a+b == value for (a,b) in couples)
    if not flag:
        return value
    else:
        return evaluate(preamble[1:] + [value], listt[1:])

value = evaluate(first_preamble, rest_of_list)
print(value)

def helper(listt: list):
    acc = 0
    acc_list = []
    for i in listt:
        acc += i
        acc_list += [i]
        if acc < value:
            continue
        elif acc == value:
            return min(acc_list), max(acc_list)
        else:
            return None

def evaluate2(listt: list):
    for i in range(len(listt)):
        ret_val = helper(listt[i:])
        if ret_val is not None:
            return ret_val

value2_1, value2_2 = evaluate2(list_numbers)
print(value2_1 + value2_2)