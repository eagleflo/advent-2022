#!/usr/bin/env python3
from math import prod

lines = open("08.txt").read().splitlines()
grid = [0] * len(lines)
for i, line in enumerate(lines):
    grid[i] = [0] * len(line)
    for j, char in enumerate(line):
        grid[i][j] = int(char)


# Assumes square grid
def visible(grid, x, y):
    # Perimeter
    if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
        return True
    else:
        height = grid[y][x]
        left = grid[y][:x]
        right = grid[y][x + 1 :]
        top = [c[x] for c in grid[:y]]
        bottom = [c[x] for c in grid[y + 1 :]]
        # print(height, left, right, top, bottom)
        return any(
            [
                all(height > tree for tree in left),
                all(height > tree for tree in right),
                all(height > tree for tree in top),
                all(height > tree for tree in bottom),
            ]
        )


visibles = 0
for i, line in enumerate(grid):
    for j, tree in enumerate(line):
        if visible(grid, j, i):
            visibles += 1
print(visibles)


def scenic_score(grid, x, y):
    height = grid[y][x]
    left = grid[y][:x][::-1]
    right = grid[y][x + 1 :]
    top = [c[x] for c in grid[:y]][::-1]
    bottom = [c[x] for c in grid[y + 1 :]]
    # print(height, left, right, top, bottom)
    scores = [0] * 4
    for tree in left:
        scores[0] += 1
        if tree >= height:
            break
    for tree in right:
        scores[1] += 1
        if tree >= height:
            break
    for tree in top:
        scores[2] += 1
        if tree >= height:
            break
    for tree in bottom:
        scores[3] += 1
        if tree >= height:
            break
    return prod(scores)


scenic_scores = []
for i, line in enumerate(grid):
    for j, tree in enumerate(line):
        scenic_scores.append(scenic_score(grid, j, i))
print(max(scenic_scores))
