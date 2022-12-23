#!/usr/bin/env python3
import numpy as np

instructions = open('10.txt').read().splitlines()

cycles = []
interesting_cycles = [20, 60, 100, 140, 180, 220]
X = 1

for instruction in instructions:
    if instruction.startswith('noop'):
        cycles.append(X)
    elif instruction.startswith('addx'):
        _, val = instruction.split(" ")
        val = int(val)
        cycles.append(X)
        cycles.append(X)
        X += val

signal_strengths = 0
for cycle in interesting_cycles:
    signal_strength = cycles[cycle-1] * cycle
    #print(cycle, cycles[cycle-1], signal_strength)
    signal_strengths += signal_strength

print(signal_strengths)

crt = np.zeros((6, 40))

def print_crt(crt):
    for row in crt:
        line = ""
        for val in row:
            if val == 0:
                line += '.'
            elif val == 1:
                line += '#'
        print(line)

for i, cycle in enumerate(cycles):
    if abs((i % 40) - cycle) < 2:
        crt[i // 40][i % 40] = 1

print_crt(crt)
