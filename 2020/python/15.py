inputt = [2, 0, 6, 12, 1, 3]
turns = {n: i+1 for i, n in enumerate(inputt)}
n = 0
for i in range(7, 30000000):
    if n not in turns:
        new_n = 0
    else:
        new_n = i - turns[n]

    turns[n] = i
    n = new_n
print(n)
