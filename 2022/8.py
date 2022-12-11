
import pathlib

path = pathlib.Path(".") / "8.example.txt"
# path = pathlib.Path('.') / "5.example.txt"
with open(path, "r", encoding="utf-8") as f:
    input_list = [[int(y) for y in x] for x in f.read().splitlines()]

lato = len(input_list)
acc = 0


for i in range(1, lato-1): # riga/y
    for j in range(1, lato-1): # colonna/x

        all_rows = all(input_list[xx][j] < input_list[i][j] for xx in range(0, lato) if xx != i)
        all_cols = all(input_list[i][xx] < input_list[i][j] for xx in range(0, lato) if xx != j)

        if all_cols and all_rows:
            acc += accb

print(acc)
