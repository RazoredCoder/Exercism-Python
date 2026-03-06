def equilateral(sides):
    if is_triangle(sides) == False: return False

    if sides[0] == sides[1] == sides[2]: return True
    return False

def isosceles(sides):
    if is_triangle(sides) == False: return False
    a, b, c = sides

    if a == b: return True
    if b == c: return True
    if a == c: return True
    return False


def scalene(sides):
    if is_triangle(sides) == False: return False
    a, b, c = sides

    if a == b: return False
    if b == c: return False
    if a == c: return False
    return True

def is_triangle(sides:list):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0: pass
    else: return False
    if sides[0] + sides[1] > sides[2]: pass
    else: return False
    if sides[1] + sides[1] > sides[0]: pass
    else: return False
    if sides[0] + sides[2] > sides[1]: pass
    else: return False
    return True

