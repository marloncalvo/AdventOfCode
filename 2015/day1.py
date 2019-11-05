def final_level(s):
    floor = 0
    for c in s:
        if c == '(':
            floor = floor + 1
        else:
            floor = floor - 1

    return floor

def basement_index(s):
    floor = 0
    index = 0
    for c in s:
        index = index + 1
        if c == '(':
            floor = floor + 1
        else:
            floor = floor - 1
        if floor == -1:
            return index

    # Oh no, we never reached the basement.
    return -1
