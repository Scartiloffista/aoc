import ast
import pathlib
import itertools

path = pathlib.Path('.') / "13.txt"
with open(path, "r") as f:
    inputt = f.read().strip().split("\n\n")
    inputt = [[ast.literal_eval(y) for y in x.splitlines()] for x in inputt]

print(inputt)

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


acc = 0

for i, (l, r) in enumerate(inputt):
    evaluation = evaluate(l,r)
    if evaluation == 1:
        acc += 1 + i

print(acc)
