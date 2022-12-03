#!/usr/bin/env python3
import numpy
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase

priorities = 0
for line in open("03.txt"):
    index = len(line) // 2
    a, b = set(line[:index]), set(line[index:])
    common = a.intersection(b).pop()

    if common in lowercase:
        priorities += lowercase.index(common) + 1
    elif common in uppercase:
        priorities += uppercase.index(common) + len(uppercase) + 1

print(priorities)

priorities = 0
lines = open("03.txt").read().splitlines()
groups = numpy.array_split(lines, len(lines) / 3)
for group in groups:
    a, b, c = set(group[0]), set(group[1]), set(group[2])
    common = set.intersection(a, b, c).pop()

    if common in lowercase:
        priorities += lowercase.index(common) + 1
    elif common in uppercase:
        priorities += uppercase.index(common) + len(uppercase) + 1

print(priorities)
