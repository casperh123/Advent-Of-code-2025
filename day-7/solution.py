

import os

def solve(lines):
    beams = [False] * len(lines[0])
    splitters = 0

    start_index = 0

    for index, char in enumerate(lines[0]):
        if char == "S":
            start_index = index

    beams[start_index] = True
            
    for i in range(1, len(lines) - 1):
        for index, char in enumerate(lines[i]):
            if char == "^" and beams[index] == True:
                splitters += 2
                beams[index] = False
                beams[index + 1] = True
                beams[index - 1] = True

    return splitters

def paths(row, position, manifolds, memo):
    key = (row, position)
    
    if key in memo:
        return memo[key]
    
    if row >= len(manifolds):
        return 1
    
    char = manifolds[row][position]
    timelines = 0

    if char == '.' or char == "S":
        timelines = paths(row + 1, position, manifolds, memo)
    elif char == "^":
        left_timeline = paths(row + 1, position - 1, manifolds, memo)
        right_timeline = paths(row + 1, position + 1, manifolds, memo)

        timelines = left_timeline + right_timeline


    memo[key] = timelines
    
    return timelines


def solve_2(lines):
    start_index = 0

    for index, char in enumerate(lines[0]):
        if char == "S":
            start_index = index

    return paths(0, start_index, lines, {})


path = os.path.dirname(os.path.abspath(__file__))
lines = [list(x.rstrip()) for x in open(path + '/day-7.txt').readlines()]

count = solve_2(lines)

print(lines)
print(count)