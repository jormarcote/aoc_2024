
from dataclasses import dataclass, field



@dataclass
class Group:
    id: int = 0
    fields:set  =field(default_factory=set)
    value: str = ""

    def __hash__(self):
        return hash(self.id)+hash(self.value)

positions = [(0,1),(1,0),(0,-1),(-1,0)]
position_labels = ["R","D","L","U"]
position_values = [1,2,1,2]
position_map = {l:(p,v) for l,p,v in zip(position_labels, positions, position_values)}

def add(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def get(data, pos):
    return data[pos[0]][pos[1]]

def is_outside(data, pos):
    return pos[0] < 0 or pos[0] >= len(data) or pos[1] < 0 or pos[1] >= len(data[0])

def navigate(data):
    map:dict = {}
    groups = set()
    for i,r in enumerate(data):
        for j,v in enumerate(r):
            pos = (i,j)
            if pos in map:
                continue
            stack = [pos]
            while stack:
                # print("STACK", stack)
                pos = stack[-1]
                to_inspect = None
                has_neighbour = False
                for p in positions:
                    d = add(pos,p)
                    if is_outside(data, d) or get(data,d) != v or d in stack:
                        continue
                    else:
                        has_neighbour = True
                        if d in map:
                            dmap = map[d]
                            if pos not in map:
                                map[pos] = dmap
                                dmap.fields.add(pos)
                            elif map[pos]!=dmap:
                                map[pos].fields.update(dmap.fields)
                                for pos2 in dmap.fields:
                                    map[pos2] = map[pos]
                                groups.remove(dmap)     
                        else:
                            to_inspect = d
                            break
                if not has_neighbour:
                    map[pos] = Group(id=100*pos[0]+pos[1], value=v, fields=set({pos}))
                    groups.add(map[pos])
                    stack.pop()
                elif to_inspect:
                    stack.append(to_inspect)
                else:
                    if pos not in map:
                        map[pos] = Group(id=100*pos[0]+pos[1], value=v, fields=set({pos}))
                        groups.add(map[pos])
                    stack.pop()
    return groups



def get_group_data(data, group):

    area = len(group.fields)
    perimeter = 0
    for pos in group.fields:
        for p in positions:
            d = add(pos,p)
            if is_outside(data, d) or get(data,d) != group.value:
                perimeter+=1
    return area, perimeter

def p1(data):
    groups = navigate(data)
    return sum([a*b for a,b in [get_group_data(data, g) for g in groups]])


def has_side(data, pos):
    for p in positions:
        d = add(pos,p)
        if is_outside(data, d) or get(data,d) != group.value:
            return True
    return False

def get_neighbours(data, pos, group):
    neighbours = []
    for p,pl,pv in zip(positions, position_labels, position_values):
        d = add(pos,p)
        if d in group.fields:
            neighbours.append((d,pl,pv))
    return neighbours

def all_checked(checked, group):
    return len(checked) == len(group.fields)

def get_sides(data, group):
    sides = 0
    initial_field = group.fields[0]
    fields = group.fields
    checked = set()
    while not all_checked(checked, group):

def p2(data):
    # print(data)
    groups = navigate(data)
    # print(groups)
    return sum([a*b for a,b in [get_group_data(data, g) for g in groups]])
    # return 0


def parse_input(input:str):# -> list[Any]:
    data = [[v for v in r ] for r in input.split("\n") if r]
    return [data]


def main(input: str, part: int = 1):
    # print(input)

    parsed = parse_input(input)
    
    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
