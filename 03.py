#!/usr/bin/env python3
import numpy
from string import ascii_letters as letters

priorities = 0
for line in open("03.txt"):
    index = len(line) // 2
    a, b = set(line[:index]), set(line[index:])
    common = a.intersection(b).pop()
    priorities += letters.index(common) + 1

print(priorities)

priorities = 0
lines = open("03.txt").read().splitlines()
groups = numpy.array_split(lines, len(lines) / 3)
for group in groups:
    a, b, c = set(group[0]), set(group[1]), set(group[2])
    common = set.intersection(a, b, c).pop()
    priorities += letters.index(common) + 1

print(priorities)
