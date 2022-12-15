from scipy.sparse import csr_matrix
import string
from scipy.sparse.csgraph import dijkstra


inputt = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

mapping = { x: i+1 for i, x in enumerate(string.ascii_lowercase)}

counter = 0
grid = []

for _ in inputt.splitlines():
    
    for x in row:





inputt = [[y for y in x] for x in inputt]

pos_S = None
pos_E = None

for i, _ in enumerate(inputt):
    for j, c in enumerate(inputt[i]):
        if c == 'S':
            pos_S = (i,j)
            inputt[i][j] = 'a'
        if c == 'E': 
            pos_E = (i,j)
            inputt[i][j] = 'z'

grid = [[mapping[y] for y in x] for x in inputt]

# print(grid)


graph = csr_matrix(grid)

dist_matrix, predecessors = dijkstra(csgraph=graph, directed=False, return_predecessors=True)

print(predecessors)


