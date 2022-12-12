#!/usr/bin/env python3
lines = open("01.txt").readlines()
calories = []
current = 0

for line in lines:
    if line == "\n":
        calories.append(current)
        current = 0
    else:
        current += int(line)

calories.sort()
print(calories[-1])
print(sum(calories[-3:]))
