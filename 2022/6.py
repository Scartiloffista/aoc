import pathlib

path = pathlib.Path(".") / "6.txt"
with open(path, "r") as f:
    signal = f.read()

# p1
for i in range(len(signal)):
    if i > 3:
        if len(set(signal[i-4:i])) == 4:
            print(i)
            break

# p2
for i in range(len(signal)):
    if i > 13:
        if len(set(signal[i-14:i])) == 14:
            print(i)
            break
