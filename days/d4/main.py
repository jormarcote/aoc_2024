import numpy as np

word = ["X", "M", "A", "S"]
variations = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    [(0, 0), (1, -1), (2, -2), (3, -3)],
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
]


def is_out_of_bounds(pos, data):
    x, y = pos
    return x < 0 or x >= len(data) or y < 0 or y >= len(data[0])


def get(data, pos):
    x, y = pos
    return data[x][y]


def add(pos, v):
    return (pos[0] + v[0], pos[1] + v[1])


def check_pos(pos, data):
    total = 0
    for v in variations:
        if is_out_of_bounds(add(pos, v[-1]), data):
            continue
        row = [get(data, add(pos, i)) for i in v]
        if row == word:
            total += 1
    return total


def p1(data):
    total = 0
    for i, r in enumerate(data):
        for j, c in enumerate(r):
            total += check_pos((i, j), data)
    return total


word2 = ["M", "M", "A", "S", "S"]
variations2 = [
    [(-1, -1), (-1, 1), (0, 0), (1, 1), (1, -1)],
    [(-1, 1), (1, 1), (0, 0), (1, -1), (-1, -1)],
    [(1, 1), (1, -1), (0, 0), (-1, -1), (-1, 1)],
    [(1, -1), (-1, -1), (0, 0), (-1, 1), (1, 1)],
]


def check_pos2(pos, data):
    total = 0
    for v in variations2:
        if np.any([is_out_of_bounds(add(pos, vi), data) for vi in v]):
            continue
        row = [get(data, add(pos, i)) for i in v]
        if row == word2:
            total += 1
    return total


def p2(data):
    total = 0
    for i, r in enumerate(data):
        if i == 0 or i == len(data) - 1:
            continue
        for j, c in enumerate(r):
            if j == 0 or j == len(r) - 1:
                continue
            total += check_pos2((i, j), data)
    return total


def parse_input(input: str):  # -> list[Any]:
    data = [[v for v in line] for line in input.split("\n") if line]
    return [data]


def main(input: str, part: int = 1):

    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
