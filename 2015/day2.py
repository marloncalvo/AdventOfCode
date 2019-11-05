def wrapping_paper_area(s):
    l,w,h = dimension_to_ints(s)

    perim = 2*(l*w + w*h + l*h)
    area  = min(l*w, w*h, l*h)

    return perim + area

def ribbon_area(s):
    l,w,h = dimension_to_ints(s)

    perim = min(l*w, w*h, l*h)
    vol   = l*w*h

    return perim + vol

def total_area(func, s):
    lines = s.split("\n")
    total = 0
    
    # Some fun with higher-order functions!
    for line in lines:
        total = total + func(line)

    return total

def total_wrapping_area(s):
    return total_area(wrapping_paper_area, s)

def total_ribbon_area(s):
    return total_area(ribbon_area, s)

def dimension_to_ints(s):
    ns = s.split("x")
    return (int(ns[0]), int(ns[1]), int(ns[2]))
