#!/usr/bin/env python3
import math

class Monkey():
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0

    @classmethod
    def from_note(cls, note):
        _, items = note[1].split(':')
        items = [int(i.strip()) for i in items.split(',')]
        _, operation = note[2].split(': ')
        _, operation = operation.split('= ')
        operation = operation[4:]
        test = int(note[3].split(' ')[-1])
        true = int(note[4].split(' ')[-1])
        false = int(note[5].split(' ')[-1])
        return cls(items, operation, test, true, false)

    def turn(self, relief=None):
        for item in self.items:
            self.inspect_item(item, relief)
        self.items = []

    def inspect_item(self, item, relief=None):
        op, val = self.operation.split(' ')
        if val == 'old':
            val = item
        else:
            val = int(val)
        match op:
            case '+':
                item += val
            case '*':
                item *= val

        if relief:
            item = item // 3
        else:
            lcd = math.prod(m.test for m in monkeys)
            item = item % lcd

        # Test
        if item % self.test == 0:
            self.throw(item, self.true)
        else:
            self.throw(item, self.false)

        self.inspected += 1

    def throw(self, item, monkey_idx):
        monkey = monkeys[monkey_idx]
        monkey.items.append(item)

    def __repr__(self):
        return str(self.items)


notes = [n.split('\n') for n in open('11.txt').read().split('\n\n')]
monkeys = []
for note in notes:
    monkeys.append(Monkey.from_note(note))

for round in range(20):
    for i, monkey in enumerate(monkeys):
        monkey.turn(True)

monkeys = sorted(monkeys, key=lambda monkey: monkey.inspected)
monkey_business = monkeys[-1].inspected * monkeys[-2].inspected
print(monkey_business)

monkeys = []
for note in notes:
    monkeys.append(Monkey.from_note(note))

for round in range(10000):
    for monkey in monkeys:
        monkey.turn()
    if round % 1000 == 0:
        print(f'\nRound {round}\n')
        for i, monkey in enumerate(monkeys):
            print(i, monkey.inspected)

monkeys = sorted(monkeys, key=lambda monkey: monkey.inspected)
monkey_business = monkeys[-1].inspected * monkeys[-2].inspected
print(monkey_business)
