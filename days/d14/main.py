

import re

def parse(robot):
    pj,pi,vj,vi = robot
    return (pi,pj),(pi,pj)

def move(pos, vel, seconds, size):
    pi,pj = pos
    vi,vj = vel
    si,sj = size
    return (pi+vi*seconds)%si, (pj+vj*seconds)%sj


def print_map(data, size):
    [print("".join([ str(len([p for p in data if p ==(i,j)])) if (i,j) in data else "." for j in range(size[1])])) for i in range(size[0])]  


def p1(data):
    # Add code here
    # size = 101,103
    size = 7, 11
    print("data", data)
    seconds = 100
    new_pos = [ move(*parse(r),seconds, size) for r in data]
    print(new_pos)
    print_map(new_pos, size)
    hi = (size[0]-1)//2 
    hj = (size[1]-1)//2 
    print(hi, hj)
    q1 = len([ (i,j) for i,j in new_pos if i < hi and j < hj])
    q2 = len([ (i,j) for i,j in new_pos if i < hi and j > hj])
    q3 = len([ (i,j) for i,j in new_pos if i > hi and j > hj])
    q4 = len([ (i,j) for i,j in new_pos if i > hi and j < hj])
    print(q1,q2,q3,q4)
    return q1*q2* q3* q4
    # return 0


def p2(data):
    # Add code here
    return 0


def parse_input(input:str):# -> list[Any]:
    lines = input.split("\n")
    data = []
    for line in lines:
        items = list(map(int,re.findall(r"(-?\d+)", line, re.M|re.I)))
        data.append(items)
        # print(line, items)
    # Add code here
    return [data]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)
    
    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
