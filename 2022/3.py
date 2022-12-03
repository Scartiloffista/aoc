import string
import pathlib

path = pathlib.Path(".") / "3.txt"
with open(path, "r") as f:
    input_list = [x.strip() for x in f.read().strip().splitlines()]

list_p1 = []

values = dict(
    list((b, a) for a, b in enumerate(string.ascii_lowercase, 1))
    + list((b, a) for a, b in enumerate(string.ascii_uppercase, 27))
)

for x in input_list:
    a, b = x[: len(x) // 2], x[len(x) // 2 :]
    intersection = list(set(a) & set(b))
    list_p1.append(values[intersection[0]])

print("p1")
print(sum(list_p1))


def divide_chunks(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]


chunks = divide_chunks(input_list, 3)

list_p2 = []
for x in chunks:
    a, b, c = x[:3]
    intersection = list(set(a) & set(b) & set(c))
    list_p2.append(values[intersection[0]])

print("p2")
print(sum(list_p2))
