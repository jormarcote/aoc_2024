def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def is_outside(node, limits):
    return node[0] < 0 or node[0] >= limits[0] or node[1] < 0 or node[1] >= limits[1]


def printmap(map, antinodes):
    [
        print("".join([v if (i, j) not in antinodes else "X" for j, v in enumerate(r)]))
        for i, r in enumerate(map)
    ]


def p1(nodes, antennas, limits, map):
    # Add code here
    antinodes = set()
    for antenna in antennas:
        anodes = [node[:2] for node in nodes if node[2] == antenna]
        for i, n1 in enumerate(anodes[:-1]):
            for n2 in anodes[i + 1 :]:
                dist = sub(n1, n2)
                opt1 = add(n1, dist)
                opt2 = sub(n2, dist)
                if not is_outside(opt1, limits):
                    antinodes = set([*antinodes, opt1])
                if not is_outside(opt2, limits):
                    antinodes = set([*antinodes, opt2])
    return len(antinodes)


def push(node, list):
    list = set([*list, node])
    return list


def p2(nodes, antennas, limits, map):
    # Add code here
    print(antennas, limits)
    antinodes = []
    for antenna in antennas:
        anodes = [node[:2] for node in nodes if node[2] == antenna]
        for i, n1 in enumerate(anodes[:-1]):
            for n2 in anodes[i + 1 :]:
                dist = sub(n1, n2)
                opt = tuple([*n1])
                while True:
                    opt = add(opt, dist)
                    if is_outside(opt, limits):
                        break
                    antinodes = push(opt, antinodes)
                opt = tuple([*n2])
                while True:
                    opt = sub(opt, dist)
                    if is_outside(opt, limits):
                        break
                    antinodes = push(opt, antinodes)

    printmap(map, antinodes)
    for antenna in antennas:
        anodes = [node[:2] for node in nodes if node[2] == antenna]
        if len(anodes) <= 2:
            continue
        for node in anodes:
            antinodes = push((node[0], node[1]), antinodes)
    return len(antinodes)


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    map = [[v for v in r] for r in input.split("\n")]
    data = [
        (i, j, v)
        for i, line in enumerate(input.split("\n"))
        for j, v in enumerate(line)
        if v != "."
    ]
    antennas = set(v for i, j, v in data)
    return [data, antennas, [len(input.split("\n")), len(input.split("\n")[0])], map]


def main(input: str, part: int = 1):
    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
