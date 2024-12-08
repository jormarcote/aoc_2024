nextmapper = {
    "^": (-1, 0),
    "<": (0, -1),
    ">": (0, 1),
    "V": (1, 0),
}
turnmapper = {"^": ">", ">": "V", "V": "<", "<": "^"}


def sm(v, k):
    return (v[0] + k[0], v[1] + k[1])


def is_outside(values, pos):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(values) or pos[1] >= len(values[0])


def get(values, pos):
    return values[pos[0]][pos[1]]


def printv(values, visited={}):
    [
        print(
            "".join([k if (i, j) not in visited else "X" for j, k in enumerate(r)]) + ""
        )
        for i, r in enumerate(values)
    ]


def visite(
    values,
    pos,
    ori,
    prev_visited: None | set = None,
    prev_been: None | set = None,
    debug: bool = True,
):

    if prev_visited is None:
        prev_visited = set()
    if prev_been is None:
        prev_been = set()
    visited = set([*prev_visited])
    been = set([*prev_been])
    loop = False
    if debug:
        printv(values, visited)
        print(pos, ori, visited)
    while pos is not None:
        b = tuple([*pos, ori])
        visited = {*visited, tuple(pos)}

        step = nextmapper[ori]
        nextpos = sm(pos, step)
        if b in been:
            if debug:
                print("already been here, finishing")
            loop = True
            break
        else:
            been = {*been, b}
        if is_outside(values, nextpos):
            if debug:
                print("Position outside of map")
            break
        v = get(values, nextpos)
        if v == "#":
            if debug:
                print("Turning right")
            ori = turnmapper[ori]
        else:
            if debug:
                print("Forward")
            pos = nextpos

    if debug:
        printv(values, visited)
    return visited, been, loop


def p1(values, pos, ori):
    visited, been, _ = visite(values, pos, ori)
    return len(visited)


def generate_alternative_map(values, pos):
    return [
        [v if (i, j) != pos else "#" for j, v in enumerate(r)]
        for i, r in enumerate(values)
    ]


def p2(values, pos, ori):

    total = 0
    visited = set([])
    been = set([])
    # printv(values, visited)
    print(visited)
    while pos is not None:
        b = tuple([*pos, ori])
        visited = {*visited, tuple(pos)}
        # printv(values, visited)

        step = nextmapper[ori]
        nextpos = sm(pos, step)
        if b in been:
            print("already been here, finishing")
            break
        if is_outside(values, nextpos):
            print("Position outside of map")
            break
        v = get(values, nextpos)
        if v == "#":
            print("Turning right")
            ori = turnmapper[ori]
        else:
            next_visited = tuple(nextpos) in visited
            if not next_visited:
                _, _, loop = visite(
                    generate_alternative_map(values, nextpos),
                    pos,
                    ori,
                    visited,
                    been,
                    debug=False,
                )
                if loop:
                    print("!! Loop detected")
                    total += 1
            pos = nextpos
        # print(ori, v)
        been = {*been, b}
    return total


def parse_input(input: str):  # -> list[Any]:
    # Add code here

    values = [[k for k in v] for v in input.split("\n") if v]
    gs = ["^", ">", "<", "V"]
    pos = 0, 0
    ori = ""
    for i, row in enumerate(values):
        for j, v in enumerate(row):
            if v in gs:
                pos = i, j
                ori = v

    printv(values)
    print(pos, ori)
    return [values, pos, ori]


def main(input: str, part: int = 1):
    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
