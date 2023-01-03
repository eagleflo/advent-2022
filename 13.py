#!/usr/bin/env python3
import itertools

pairs = [p.split("\n") for p in open("13.txt").read().strip().split("\n\n")]
packets = [(eval(p[0]), eval(p[1])) for p in pairs]


def int_check(a, b):
    """Check for the case where both are integers."""
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a > b:
            return False
        else:
            # Signal that we need to move on
            return -1


def convert_to_lists(a, b):
    """Convert to lists if necessary."""
    if isinstance(a, int) and isinstance(b, list):
        return ([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return (a, [b])
    else:
        return (a, b)


def compare(left, right):
    if not left and right:
        return True
    if left and not right:
        return False

    int_result = int_check(left, right)
    if int_result == -1:
        return None
    if int_result != None:
        return int_result

    left, right = convert_to_lists(left, right)
    for a, b in itertools.zip_longest(left, right):
        # print(a, b)
        result = compare(a, b)
        if result != None:
            return result


sum = 0
for i, pair in enumerate(packets):
    if compare(pair[0], pair[1]):
        sum += i + 1
        print(pair[0], pair[1], "true")
    else:
        print(pair[0], pair[1], "false")
    print()
print(sum)
