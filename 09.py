#!/usr/bin/env python3

moves = open("09_easy.txt").read().splitlines()

head = (0, 0)
tail = (0, 0)
tail_history = [(0, 0)]


class Knot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.history = []

    def move(self, direction):
        self.history.append((self.x, self.y))
        match direction:
            case "L":
                self.x -= 1
            case "R":
                self.x += 1
            case "U":
                self.y -= 1
            case "D":
                self.y += 1

    def touching(self, other):
        return abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2

    def follow(self, direction, head):
        match direction:
            case "L":
                if abs(self.x - head.x) == 2 and self.y == head.y:
                    self.move(direction)
                elif not self.touching(head):
                    self.history.append((self.x, self.y))
                    self.x -= 1
                    self.y = head.y
            case "R":
                if abs(self.x - head.x) == 2 and self.y == head.y:
                    self.move(direction)
                elif not self.touching(head):
                    self.history.append((self.x, self.y))
                    self.x += 1
                    self.y = head.y
            case "U":
                if abs(self.y - head.y) == 2 and self.x == head.x:
                    self.move(direction)
                elif not self.touching(head):
                    self.history.append((self.x, self.y))
                    self.y -= 1
                    self.x = head.x
            case "D":
                if abs(self.y - head.y) == 2 and self.x == head.x:
                    self.move(direction)
                elif not self.touching(head):
                    self.history.append((self.x, self.y))
                    self.y += 1
                    self.x = head.x

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rope:
    def __init__(self, length: int) -> None:
        self.knots = []
        for i in range(length):
            self.knots.append(Knot())

    def move(self, direction, amount):
        for i in range(amount):
            head, tail = self.knots[0], self.knots[1:]
            head.move(direction)
            for j, knot in enumerate(tail):
                previous = self.knots[j]
                knot.follow(direction, previous)


rope_1 = Rope(2)
for move in moves:
    direction, amount = move.split(" ")
    amount = int(amount)
    rope_1.move(direction, amount)

print(rope_1.knots[-1].history)
print(len(set(rope_1.knots[-1].history)))
