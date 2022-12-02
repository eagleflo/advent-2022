#!/usr/bin/env python3

scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

with open("02.txt", "r") as f:
    score = 0

    for line in f:
        opponent, me = line.strip().split(" ")
        # Draw
        if scores[opponent] == scores[me]:
            score += 3 + scores[me]
        # Win
        elif (
            opponent == "A"
            and me == "Y"
            or opponent == "B"
            and me == "Z"
            or opponent == "C"
            and me == "X"
        ):
            score += 6 + scores[me]
        else:
            score += scores[me]

    print(score)


with open("02.txt", "r") as f:
    score = 0

    for line in f:
        opponent, outcome = line.strip().split(" ")
        # Lose
        if outcome == "X":
            if opponent == "A":
                me = "Z"
            elif opponent == "B":
                me = "X"
            else:
                me = "Y"
            score += scores[me]
        # Draw
        elif outcome == "Y":
            me = opponent
            score += 3 + scores[me]
        # Win
        elif outcome == "Z":
            if opponent == "A":
                me = "Y"
            elif opponent == "B":
                me = "Z"
            else:
                me = "X"
            score += 6 + scores[me]

    print(score)
