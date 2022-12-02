import os
import pathlib
import math

# shameless plug from rosettacode, with comments

from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    # extended euclidean, returns s/n_j (= multiplicative inverse a mod b)
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


path = pathlib.Path('.').parent / "inputs/13.txt.test"
with open(path, "r") as f:
    timestamp, original_buses = f.read().splitlines()

timestamp = int(timestamp)
buses_p1 = [int(x) for x in original_buses.split(',') if x != 'x']

earliest = sorted([(math.ceil(timestamp/b) * b, b) for b in buses_p1])[0]
p1 = earliest[1] * (earliest[0] - timestamp)


buses_p2 = [(int(i), int(bus))
            for i, bus in enumerate(original_buses.split(',')) if bus != 'x']
n = [i[1] for i in buses_p2]
a = [(bus-i) % bus for i, bus in buses_p2]
val = chinese_remainder(n, a)
print(val)