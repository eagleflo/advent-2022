#!/usr/bin/env python3

with open("01.txt", "r") as f:
    calories = []
    current = 0

    for line in f:
        if line == "\n":
            calories.append(current)
            current = 0
        else:
            current += int(line)

    calories.sort()
    print(calories[-1])
    print(sum(calories[-3:]))
