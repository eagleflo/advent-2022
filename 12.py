#!/usr/bin/env python3
import sys
from collections import deque

sys.setrecursionlimit(10000)

# Key insight: start from the end and work backwards.
# Vast flat area in the beginning and only one way to the top.

grid = open("12.txt").read().splitlines()
HEIGHT = len(grid)
WIDTH = len(grid[0])

# Maintain a dictionary of the cheapest path to any visited node
cheapest = {}


def possible_steps(grid, path):
    steps = deque()
    y, x = path[-1]
    height = ord(grid[y][x])

    # Special handling for the starting node
    if height == ord("S"):
        height = ord("a") - 1

    directions = []
    if x < WIDTH - 1:
        directions.append((y, x + 1))
    if y < HEIGHT - 1:
        directions.append((y + 1, x))
    if y > 0:
        directions.append((y - 1, x))
    if x > 0:
        directions.append((y, x - 1))

    for coords in directions:
        new_y, new_x = coords
        # If we already have a cheaper way to reach this exact same node, stop here.
        if cheapest.get(coords) and len(cheapest.get(coords)) <= len(path) + 1:
            continue
        if coords not in path:
            step = ord(grid[new_y][new_x])
            # Special handling for the end node
            if step == ord("E"):
                step = ord("z") + 1
            if height + 1 == step:
                steps.appendleft(coords)
            elif height >= step:
                steps.append(coords)

    return steps


def walk(grid, path):
    steps = possible_steps(grid, path)
    for step in steps:
        y, x = step
        if grid[y][x] == "E":
            complete_paths.append(path + [step])
            complete_paths.sort(key=len)
            return
        next = path + [step]
        cheapest[step] = next

        # Key insight: if we already have a shorter complete path, just give up.
        if len(complete_paths) > 0 and len(next) > len(complete_paths[0]):
            return
        walk(grid, next)


def find_start(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "S":
                return (i, j)


def find_end(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "E":
                return (i, j)


start = find_start(grid)
end = find_end(grid)

path = [start]
complete_paths = []
walk(grid, path)

# Start doesn't count as a step
print(len(complete_paths[0]) - 1)
