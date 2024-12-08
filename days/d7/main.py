operations = ["*", "+"]
operations2 = ["*", "+", "|"]


def evaluate(operator, values):
    if len(values) == 1:
        return values[0]
    if operator == "*":
        return values[0] * values[1]
    elif operator == "|":
        return int(f"{values[0]}{values[1]}")
    return values[0] + values[1]


def check(values, result, operations=operations):
    if len(values) == 1:
        return values[0] == result
    options = [*operations]
    for i in range(len(values) - 2):
        options = [(*ops, op) for ops in options for op in operations]
    for ops in options:
        value = values[0]
        for i, op in enumerate(ops):
            value = evaluate(op, [value, values[i + 1]])
        if value == result:
            return True

    return False


def p1(values):
    # Add code here
    total = 0
    for equation, values in values:
        if check(values, equation):
            total += equation
    return total


def p2(values):
    # Add code here
    total = 0
    for equation, values in values:
        if check(values, equation, operations=operations2):
            total += equation
    return total


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    r = []
    for line in input.split("\n"):
        items = line.split(": ")
        equation = int(items[0].strip())
        values = list(map(int, items[1].split(" ")))
        r.append((equation, values))
    return [r]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
