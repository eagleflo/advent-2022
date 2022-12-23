#!/usr/bin/env python3

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

    def turn(self):
        for item in self.items:
            self.inspect_item(item)
        self.items = []

    def inspect_item(self, item):
        print(f'Monkey inspects an item with worry level of {item}')
        op, val = self.operation.split(' ')
        if val == 'old':
            val = item
        else:
            val = int(val)
        match op:
            case '+':
                item += val
                print(f'  Worry level increased by {val} to {item}')
            case '*':
                item *= val
                print(f'  Worry level is multiplied by {val} to {item}')

        # Relief
        item = item // 3
        print(f'  Monkey gets bored with item. Worry level is divided by 3 to {item}.')

        # Test
        if item % self.test == 0:
            print(f'  Current worry level is divisible by {self.test}.')
            self.throw(item, self.true)
        else:
            print(f'  Current worry level is not divisible by {self.test}.')
            self.throw(item, self.false)

        self.inspected += 1

    def throw(self, item, monkey_idx):
        print(f'  Item with worry level {item} is thrown to monkey {monkey_idx}.')
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
        print(i, monkey)
        monkey.turn()
    print(monkeys)

monkeys = sorted(monkeys, key=lambda monkey: monkey.inspected)
monkey_business = monkeys[-1].inspected * monkeys[-2].inspected
print(monkey_business)
