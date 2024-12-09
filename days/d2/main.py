import numpy as np


def check(r):

    print("Chec", r)
    diffs = r[:-1] - r[1:]
    maindif = r[0] - r[-1]
    all_equals = np.all((diffs < 0) == (maindif < 0))
    absdif = np.abs(diffs)
    steps_size_ok = np.all(np.logical_and(absdif > 0, absdif < 4))
    print(diffs, absdif, maindif, all_equals, steps_size_ok)

    if not all_equals:
        print("Not equal")
        return False
    if not steps_size_ok:
        print("Steps not ok")
        return False
    return True


def p1(data):
    # Add code here
    print(data)
    print(data.shape)
    total = 0
    for r in data:
        print("Checking", r)
        if check(r):
            total += 1

    return total


def p2(data):
    print(data)
    print(data.shape)
    total = 0
    for r in data:
        print("")
        print("Checking", r)
        if not check(r):
            print("Checking all rotations")
            for i, v in enumerate(r):
                if check(np.array([k for j, k in enumerate(r) if j != i])):
                    total += 1
                    break
        else:
            print("Already ok")
            total += 1

    return total


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    data = [
        np.array([int(x) for x in line.split(" ")])
        for line in input.split("\n")
        if line
    ]
    return [np.array(data)]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
