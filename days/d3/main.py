import re


def p1(data):
    reg = r"mul\((\d{1,3}),(\d{1,3})\)"

    res = re.findall(reg, data, re.MULTILINE | re.DOTALL)
    result = sum([int(x) * int(y) for x, y in res])
    return result


def p2(data):
    reg = r"(do|don\'t)\(\)|(mul)\((\d{1,3}),(\d{1,3})\)"

    res = re.findall(reg, data, re.MULTILINE | re.DOTALL)
    do = 1
    total = 0
    for isdo, ismul, x, y in res:
        if isdo == "do":
            do = 1
        elif isdo == "don't":
            do = 0
        elif ismul == "mul":
            total += do * int(x) * int(y)
    # print(res)
    return total


def parse_input(input: str):  # -> list[Any]:
    return [input]


def main(input: str, part: int = 1):
    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
