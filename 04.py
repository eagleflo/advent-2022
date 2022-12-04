#!/usr/bin/env python3

count = 0
for line in open("04.txt").read().splitlines():
    a, b = line.split(",")
    a1, a2 = [int(x) for x in a.split("-")]
    b1, b2 = [int(x) for x in b.split("-")]
    if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
        count += 1

print(count)

count = 0
for line in open("04.txt").read().splitlines():
    a, b = line.split(",")
    a1, a2 = [int(x) for x in a.split("-")]
    b1, b2 = [int(x) for x in b.split("-")]
    if (b1 <= a2 <= b2) or (a1 <= b2 <= a2):
        count += 1

print(count)
