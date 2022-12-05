import string
import pathlib

path = pathlib.Path(".") / "4.txt"
# path = pathlib.Path(".") / "4.example.txt"


with open(path, "r") as f:
    input_list = f.read().strip().splitlines()

count_p1 = 0
for x in input_list:
    a, b = x.split(",")
    a, b = a.split("-"), b.split("-")
    a0, a1, b0, b1 = int(a[0]), int(a[1]), int(b[0]), int(b[1])

    if (a0 <= b0 <= b1 <= a1) or (b0 <= a0 <= a1 <= b1):
        count_p1 += 1


s

count_p2 = 0
for x in input_list:
    a, b = x.split(",")
    a, b = a.split("-"), b.split("-")
    a, b = range(int(a[0]), int(a[1]) + 1), range(int(b[0]), int(b[1]) + 1)

    if set(a).intersection(b):
        count_p2 += 1


print(count_p1)
print(count_p2)
