import pathlib


path = pathlib.Path('.') / "12.txt"
with open(path, "r") as f:
    inputt = f.read().strip().splitlines()

pos_E = None
pos_S = None

prev = {}
dist = {}

q = set()

inputt = [[y for y in x] for x in inputt]

a_pos = []

for y, row in enumerate(inputt):
    for x, c in enumerate(row):
        
        pos = (y,x)
        prev[pos] = None

        if c == 'S' or c == 'a':
            a_pos.append(pos)

        if c == 'S':
            pos_S = pos
            inputt[y][x] = 'a'
        else:
            if c == 'E': 
                pos_E = pos
                inputt[y][x] = 'z'
        
        dist[pos] = float('inf')
            
        q.add(pos)

a_pos = None
dist[pos_E] = 0

while len(q) > 0:
    # _, u = heapq.heappop(q)
    u = min(q, key=dist.get)

    uy, ux = u
    if inputt[uy][ux] == 'a':
        a_pos = u
        break


    q.discard(u)

    neighs = []
    for y, x in [(1,0), (0,1), (-1, 0), (0,-1)]:
            
        cy, cx = u
        v = tuple(map(sum,zip(u, (y, x))))
        ny, nx = v
        if v in q:
            current_val = ord(inputt[cy][cx])
            neigh_val = ord(inputt[ny][nx])

            if (x,y) != (0,0) and neigh_val >= current_val-1:
                
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    

flag = False
curr = a_pos
i = 0
while curr is not pos_E:
    curr = prev[curr]
    y, x = curr
    i+=1


print(i)
