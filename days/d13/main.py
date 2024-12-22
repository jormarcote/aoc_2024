

import re

def calculate(s):
    ma,na,mb,nb,t1,t2 = s
    b = (t2 - mb*t1/ma) /( nb - mb*na/ma)
    b = (t2*ma - mb*t1)/(nb*ma - mb*na)
    a = (t1 - na*b ) / ma
    # a= (t1 - b*na )/ma
    return a,b

def p1(data):
    total = 0
    for s in data:
        print(s)
        r = calculate(s)
        print(r)
        total += 3 * r[0] + r[1]
    return 0


def p2(data):
    # Add code here
    return 0


def parse_input(input:str):# -> list[Any]:
    # print(input)
    strings = [r for r in input.split("\n\n") if r]
    # print(strings)
    systems = []
    for s in strings:
        # print(s)
        values = list(map(int,re.findall(r"(\d+)", s, re.M|re.I)))
        # print(values)
        systems.append(values)
    return [systems]



def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)
    
    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
