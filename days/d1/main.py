def split(values, sort: bool = True):
    vas = [v[0] for v in values]
    vbs = [v[1] for v in values]
    if sort:
        vas.sort()
        vbs.sort()
    return vas, vbs


def p1(*args):
    values = args[0]
    print(values, type(values))
    vas, vbs = split(values)
    r = sum([a - b if a > b else b - a for a, b in zip(vas, vbs)])
    return r


def p2(*args):
    values = args[0]

    print(values, type(values))
    vas, vbs = split(values)
    total = 0

    for v in vas:
        total += v * len([k for k in vbs if k == v])

    return total


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    values = [[int(k) for k in v.split(",")] for v in input.split("\n") if v]
    return [values]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)

    print(*parsed)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
