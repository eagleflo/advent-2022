#!/usr/bin/env python3
import copy
import re

text = open('05.txt').read()
diagram, commands = [s.splitlines() for s in text.split('\n\n')]

stacks = []
number_of_stacks = int(re.findall(r'(\d+)', diagram[-1])[-1])
for n in range(number_of_stacks):
    stack = []
    for line in diagram[:-1]:
        pos = 4 * n
        try:
            item = line[pos+1]
            if item.isalpha():
                stack.append(item)
        except:
            pass
    stack.reverse()
    stacks.append(stack)

stacks2 = copy.deepcopy(stacks)

for command in commands:
    a, b, c = map(int, re.findall(r'(\d+)', command))
    s1, s2 = stacks[b-1], stacks[c-1]
    for _ in range(a):
        s2.append(s1.pop())

print(''.join(s[-1] for s in stacks))

for command in commands:
    a, b, c = map(int, re.findall(r'(\d+)', command))
    s1, s2 = stacks2[b-1], stacks2[c-1]
    for crate in s1[-a:]:
        s2.append(crate)
        s1.pop()
        
print(''.join(s[-1] for s in stacks2))
