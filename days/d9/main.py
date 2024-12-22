import numpy as np


def p1(values):
    disk = [
        int(i / 2) if i % 2 == 0 else -1 for i, v in enumerate(values) for k in range(v)
    ]
    i = 0
    j = len(disk) - 1
    print(len(disk))
    while i < j:
        while disk[i] != -1:
            i += 1

        while disk[j] == -1:
            j -= 1
        if i < j:
            tmp = disk[i]
            disk[i] = disk[j]
            disk[j] = tmp
            i += 1
            j -= 1
    print(len(disk))
    disk_values = np.array([int(d) for d in disk if d != -1])
    result = 0
    disk_results = np.arange(len(disk_values)) * disk_values
    result = np.sum(disk_results)

    return result

def print_disk(disk):
    print("".join([(str(d[0]) if d[0] > -1 else ".")*d[1]
    for d in disk]))

def defragment(disk):
    disk = compact(disk)
    # print(disk)
    # print_disk(disk)
    for index in range(len(disk)-1):
        i = len(disk) -1 -index
        d = disk[i]
        # print([v for v in disk[:i] if v[0] == -1 and v[1] >= d[1]])
        if not len([v for v in disk[:i] if v[0] == -1 and v[1] >= d[1]]):
            continue
        if d[0] != -1:
            # print("GROUP",i, d)
            k  = 0
            while k<i:
                while disk[k][0] != -1:
                    k += 1
                if disk[k][1] >= disk[i][1]:
                    disk = switch(disk,k,i)
                    break
                else:
                    k += 1
            # print(disk)
            # print_disk(disk)
    # print("END")
    return disk

def compact(disk):
    new_disk = []
    value = disk[0][0]
    count = 0
    for d,c in disk:
        # print("d,c",d,c, value, count)
        if d == value:
            count += c
        else:
            new_disk.append((value,count))
            value = d
            count = c
    new_disk.append((value,count))
    return new_disk

def is_fragmented(disk):
    for i,d in enumerate(disk):
        if d[0] == -1:
            if len([v for v in disk[i+1:] if v[0] != -1 and v[1] <= d[1]]):
                return True
    return False


def switch(disk, i, j):
    # print("switch",i,j)
    if disk[i][1] == disk[j][1]:
        tmp = disk[i]
        disk[i] = disk[j]
        disk[j] = tmp
    elif disk[i][1] > disk[j][1]:
        dif = disk[i][1] - disk[j][1]
        disk = disk[:i] + [disk[j],(disk[i][0],dif)] + disk[i+1:j] + [(disk[i][0],disk[j][1])] + disk[j+1:]
    return compact(disk)

def p2(values):
    # Add code here
    disk = [
        (int(i / 2) if i % 2 == 0 else -1,v) for i, v in enumerate(values) 
    ]
    print(len(disk))
    disk = compact(disk)
    # print_disk(disk)
    count = 0
    while is_fragmented(disk):
        count += 1
        print ("defragmenting", count)
        prev_map = [(a,b) for a,b in disk]
        disk = defragment(disk)
        if prev_map == disk:
            print("BREAKING")
        break
    # print_disk(disk)

    disk_values = np.array([ v for v,c in disk for _ in range(c)])
    # print(disk_values)
    print(len(disk_values))
    result = 0
    disk_results = [ a*b for a,b in zip(np.arange(len(disk_values)), disk_values) if b > 0 and a > 0]
    # print(disk_results)
    result = np.sum(disk_results)

    return result


def parse_input(input: str):  # -> list[Any]:
    # Add code here
    return [[int(v) for v in input]]


def main(input: str, part: int = 1):

    parsed = parse_input(input)

    if part == 1:
        return p1(*parsed)
    else:
        return p2(*parsed)
