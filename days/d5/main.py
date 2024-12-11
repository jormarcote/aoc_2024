def check_rules(rules, update):
    for i, n in enumerate(update):
        nrules = [nr for nr in rules if nr[0] == n]
        items = update[:i]
        for r in nrules:
            if r[1] in items:
                return False
    return True


def p1(updates, rules):
    total = 0
    for u in updates:
        if check_rules(rules, u):
            total += u[(len(u) - 1) // 2]

    return total


def fix(update, rules):
    while not check_rules(rules, update):
        for i, n in enumerate(update):
            nrules = [nr for nr in rules if nr[0] == n]
            items = update[:i]
            for r in nrules:
                pos = [i for i, x in enumerate(items) if x == r[1]]
                if pos:
                    update[pos[0]] = n
                    update[i] = r[1]
                    break
    return update


def p2(updates, rules):
    incorrect = [u for u in updates if not check_rules(rules, u)]
    total = 0
    for u in incorrect:
        new_u = fix(u, rules)
        total += new_u[(len(new_u) - 1) // 2]

    return total


def parse_input(input: str):  # -> list[Any]:
    splits = input.split("\n\n")
    rules = [tuple(map(int, s.split("|"))) for s in splits[0].split("\n") if s]
    updates = [list(map(int, s.split(","))) for s in splits[1].split("\n") if s]
    return [updates, rules]


def main(input: str, part: int = 1):
    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
