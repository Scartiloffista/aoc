import ast
import pathlib
import itertools

path = pathlib.Path('.') / "13.txt"

inputt = []

with open(path, "r") as f:
    inputtt = f.read().strip().replace("\n\n", "\n").splitlines()
    for x in inputtt:
        foo = ast.literal_eval(x)
        inputt.append(foo)

# print(inputt)

def evaluate(l, r):

    zipped = list(itertools.zip_longest(l, r))

    for a, b in zipped:
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                pass
        
        elif a is None:
            return 1
        elif b is None:
            return -1
            
        elif isinstance(a, list) and isinstance(b, list):
            evaluation = evaluate(a,b)
            if evaluation == 0:
                pass
            else:
                return evaluation

        elif isinstance(a, int):
            evaluation = evaluate([a],b)
            if evaluation == 0:
                pass
            else:
                return evaluation
        
        elif isinstance(b, int):
            evaluation = evaluate(a,[b])
            if evaluation == 0:
                pass
            else:
                return evaluation

        else:
            print("non dovrei essere qui")
        
    
    return 0

from functools import cmp_to_key
inputt = sorted(inputt, key=cmp_to_key(evaluate), reverse=True)

due = None
sei = None

for i, x in enumerate(inputt):
    if x == [[2]]:
        due = i+1
    if x == [[6]]:
        sei = i+1

print(due*sei)
