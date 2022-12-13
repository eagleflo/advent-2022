#!/usr/bin/env python3

moves = open("09.txt").read().splitlines()

head = (0, 0)
tail = (0, 0)
tail_history = [(0, 0)]

for move in moves:
    direction, amount = move.split(" ")
    amount = int(amount)
    for i in range(amount):
        match direction:
            case "L":
                head = (head[0] - 1, head[1])
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = (head[0] + 1, tail[1])
                    if tail[1] != head[1] and i > 0:
                        tail = (tail[0], head[1])
                tail_history.append(tail)
            case "R":
                head = (head[0] + 1, head[1])
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = (head[0] - 1, tail[1])
                    if tail[1] != head[1] and i > 0:
                        tail = (tail[0], head[1])
                tail_history.append(tail)
            case "U":
                head = (head[0], head[1] - 1)
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = (tail[0], head[1] + 1)
                    if tail[0] != head[0] and i > 0:
                        tail = (head[0], tail[1])
                tail_history.append(tail)
            case "D":
                head = (head[0], head[1] + 1)
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = (tail[0], head[1] - 1)
                    if tail[0] != head[0] and i > 0:
                        tail = (head[0], tail[1])
                tail_history.append(tail)


print(len(set(tail_history)))
