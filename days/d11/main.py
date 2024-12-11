def blink_nums(nums):
    result = []
    for num, k in nums:
        if num == 0:
            result.append((1, k))
        elif len(str(num)) % 2 == 0:
            strnum = str(num)
            n1 = strnum[: len(strnum) // 2]
            n2 = strnum[len(strnum) // 2 :]
            result = [*result, (int(n1), k), (int(n2), k)]
        else:
            result.append((num * 2024, k))
    return result


def blink_step(data, steps, cache):
    result = []
    for d in data:
        v, _ = d
        if v not in cache:
            r = [d]
            for i in range(steps):
                r = blink_nums(r)
            cache[d] = r
        result = [*result, *cache[d]]
    return compress(result)


def compress(data):
    data = sorted(data)
    map = {}
    for d, i in data:
        if d not in map:
            map[d] = 0
        map[d] += i
    return [(k, v) for k, v in map.items()]


def super_blink(data, blinks):
    steps = 2
    cache = {}
    data = [(v, 1) for v in data]
    data = compress(data)
    print(data)
    for i in range(blinks // steps):
        print("Iteration: ", i)
        data = blink_step(data, steps, cache)
    for b in range(blinks % steps):
        data = blink_nums(data)

    return sum([v for _, v in data])


def p1(data):
    return super_blink(data, 25)


def p2(data):
    return super_blink(data, 75)


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    data = [int(v) for v in input.split(" ") if v]
    return [data]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
