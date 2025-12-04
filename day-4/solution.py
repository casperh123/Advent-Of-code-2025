

import os

def is_roll(char):
    if char == "@":
        return True
    else:
        return False

def convolution(lines, i, j, filter_size):
    total = 0
    variance = int(filter_size / 2)

    start_i = i - variance
    end_i = i + variance
    start_j = j - variance
    end_j = j + variance

    for search_i in range(start_i, end_i + 1):

        if search_i >= 0 and search_i < len(lines):

            for search_j in range(start_j, end_j + 1):

                if search_j >= 0 and search_j < len(lines[search_i]):
                    if search_i == i and search_j == j:
                        continue
                    elif is_roll(lines[search_i][search_j]):
                        total = total + 1
                        
    return total

def solve(lines):
    adjacency_list = []

    for i_index, row in enumerate(lines):
        for j_index, column in enumerate(row):
            if is_roll(lines[i_index][j_index]):
                adjacency_list.append(convolution(lines, i_index, j_index, 3))

    return len([roll for roll in adjacency_list if roll < 4])

def solve_2(lines):

    total_removed = 0

    while True:

        to_remove = []

        for i, row in enumerate(lines):
            for j, column in enumerate(row):
                if is_roll(lines[i][j]) and convolution(lines, i, j, 3) < 4:
                    to_remove.append((i, j))

        if len(to_remove) == 0:
            break

        for i, j in to_remove:
            lines[i][j] = '.'

        total_removed = total_removed + len(to_remove)

    return total_removed



path = os.path.dirname(os.path.abspath(__file__))
lines = [list(x.rstrip()) for x in open(path + '/day-4.txt').readlines()]

count = solve_2(lines)

print(lines)
print(count)