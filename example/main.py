

def p1(data):
    # Add code here
    return 0


def p2(data):
    # Add code here
    return 0


def parse_input(input:str):# -> list[Any]:
    # Add code here
    return [input]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)
    
    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
