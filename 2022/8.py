
import pathlib
import itertools

# path = pathlib.Path(".") / "8.example.txt"
path = pathlib.Path('.') / "8.txt"
with open(path, "r", encoding="utf-8") as f:
    input_list = [[int(y) for y in x] for x in f.read().splitlines()]

lato = len(input_list)
acc = 0

for i in range(1, lato-1): # riga/y
    for j in range(1, lato-1): # colonna/x

        up = all(input_list[xx][j] < input_list[i][j] for xx in range(0, i))
        down = all(input_list[xx][j] < input_list[i][j] for xx in range(i+1, lato))

        sx = all(input_list[i][xx] < input_list[i][j] for xx in range(0, j))
        dx = all(input_list[i][xx] < input_list[i][j] for xx in range(j+1, lato))

        if up or down or sx or dx:
            acc += 1

print(acc + (lato-1)*4)


# p2

listt = []

for i in range(1, lato-1): # riga/y
    for j in range(1, lato-1): # colonna/x
        curr = input_list[i][j]

        up = [input_list[xx][j]  for xx in range(0, i)]
        down = [input_list[xx][j]  for xx in range(i+1, lato)]

        sx = [input_list[i][xx]  for xx in range(0, j)]
        dx = [input_list[i][xx]  for xx in range(j+1, lato)]
        
        up, sx = up[::-1], sx[::-1]

        upT = len(up) if curr not in up else len(list(itertools.takewhile(lambda x: x < curr, up))) + 1
        downT = len(down) if curr not in down else len(list(itertools.takewhile(lambda x: x < curr, down))) + 1
        sxT = len(sx) if curr not in sx else len(list(itertools.takewhile(lambda x: x < curr, sx))) + 1
        dxT = len(dx) if curr not in dx else len(list(itertools.takewhile(lambda x: x < curr, dx))) + 1


        res = upT * downT * sxT * dxT

        listt.append(res)



print(max(listt))
