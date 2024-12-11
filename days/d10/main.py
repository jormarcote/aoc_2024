from typing import Union

import numpy as np


def is_outside(data, pos):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(data) or pos[1] >= len(data[0])


def add(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def get_next_positions(data, pos):
    return [
        add(pos, d)
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not is_outside(data, add(pos, d))
    ]


def getData(data, pos):
    return data[pos[0], pos[1]]


def getMap(map, pos) -> Union[set, list]:
    # pos1 = str(pos)
    return map[pos] if pos in map else []


def setMap(map, pos, value, islist: bool = False):
    # pos1 = str(pos)
    if pos not in map:
        map[pos] = value
    else:
        # print("SETTING", pos, value | map[pos])
        if islist:
            map[pos] = [*map[pos], *value]
        else:
            map[pos] = map[pos] | value


translator = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
}


def printmap(data, stack, final: bool = False):
    if not final:
        [
            print(
                "".join(
                    [
                        str(v) if (i, j) not in stack else translator.get(v, "X")
                        for j, v in enumerate(r)
                    ]
                )
            )
            for i, r in enumerate(data)
        ]
    else:
        [
            print(
                "".join([str(v) if (i, j) in stack else "." for j, v in enumerate(r)])
            )
            for i, r in enumerate(data)
        ]


def p1(data):
    # Add code here
    zeros = [(i, j) for i, r in enumerate(data) for j, v in enumerate(r) if v == 0]
    printmap(data, zeros)
    map = {}
    total = 0
    for z in zeros:
        value = 0
        result = set()
        stack = [z]
        visited = set()
        while stack:
            pos = stack[-1]
            visited.add(pos)
            if getData(data, pos) == 9 and value == 9:
                result = set([pos])
                setMap(map, pos, result)
                stack.pop()
                value -= 1
                continue
            if result:
                setMap(map, pos, result)

            next_pos = get_next_positions(data, pos)
            npos = None
            for nps in next_pos:
                if nps in stack or nps in visited:
                    continue
                if getData(data, nps) == value + 1:
                    npos = nps
                    break
            if npos is None:
                stack.pop()
                value -= 1
                setMap(map, pos, result)
                result = map[pos] if pos in map else result
            else:
                stack.append(npos)
                result = set()
                value += 1
        if result:
            total += len(result)

    return total


def p2(data):

    zeros = [(i, j) for i, r in enumerate(data) for j, v in enumerate(r) if v == 0]
    printmap(data, zeros)
    map = {}
    total = 0
    for z in zeros:
        value = 0
        result = set()
        stack = [z]
        visited = set()
        while stack:
            pos = stack[-1]
            visited.add(pos)
            if getData(data, pos) == 9 and value == 9:
                result = [[pos]]
                setMap(map, pos, result, islist=True)
                stack.pop()
                value -= 1
                continue
            if result:
                result = [(pos, *r) for r in result]
                setMap(map, pos, result, islist=True)

            next_pos = get_next_positions(data, pos)
            npos = None
            for nps in next_pos:
                if nps in stack or nps in visited:
                    continue
                if getData(data, nps) == value + 1:
                    npos = nps
                    break
            if npos is None:
                stack.pop()
                results = []
                for npos in next_pos:
                    if getData(data, npos) == value + 1:
                        results = [*results, *getMap(map, npos)]

                results = [(pos, *r) for r in results]
                setMap(map, pos, results, islist=True)
                result = results
                value -= 1
            else:
                stack.append(npos)
                result = []
                value += 1

        final_result = set([str(r) for r in result])
        if final_result:
            total += len(final_result)

    return total


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    data = np.array([[int(v) for v in r] for r in input.split("\n")])
    return [data]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
