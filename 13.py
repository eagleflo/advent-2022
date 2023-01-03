#!/usr/bin/env python3
import functools
import itertools

pairs = [p.split("\n") for p in open("13.txt").read().strip().split("\n\n")]
packets = [(eval(p[0]), eval(p[1])) for p in pairs]


def int_check(a, b):
    """Check for the case where both are integers."""
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            # Signal that we need to move on
            return 0


def convert_to_lists(a, b):
    """Convert to lists if necessary."""
    if isinstance(a, int) and isinstance(b, list):
        return ([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return (a, [b])
    else:
        return (a, b)


def compare(left, right):
    int_result = int_check(left, right)
    if int_result == 0:
        return None
    if int_result != None:
        return int_result

    left, right = convert_to_lists(left, right)
    if left == None:
        return -1
    if right == None:
        return 1

    for a, b in itertools.zip_longest(left, right):
        result = compare(a, b)
        if result != None:
            return result


sum = 0
for i, pair in enumerate(packets):
    if compare(pair[0], pair[1]) < 0:
        sum += i + 1
        # print(pair[0], pair[1], "true")
    else:
        # print(pair[0], pair[1], "false")
        pass
    # print()
print(sum)

# Unzip pairs
xs, ys = zip(*packets)
# Inject sentinels
sorted_packets = sorted([*xs, *ys, [[2]], [[6]]], key=functools.cmp_to_key(compare))
x = sorted_packets.index([[2]]) + 1
y = sorted_packets.index([[6]]) + 1
print(x * y)
