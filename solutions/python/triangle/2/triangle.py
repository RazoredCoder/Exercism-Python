'''Determine if a triangle is equilateral, isosceles, or scalene.'''

def equilateral(sides):
    '''Determine if a triangle is equilateral'''
    if is_triangle(sides) is False: return False

    if sides[0] == sides[1] == sides[2]: return True
    return False

def isosceles(sides):
    '''Determine if a triangle is isosceles'''
    if is_triangle(sides) is False: return False
    side_a, side_b, side_c = sides

    if side_a == side_b: return True
    if side_b == side_c: return True
    if side_a == side_c: return True
    return False


def scalene(sides):
    '''Determine if a triangle is scalene'''
    if is_triangle(sides) is False: return False
    side_a, side_b, side_c = sides

    if side_a == side_b: return False
    if side_b == side_c: return False
    if side_a == side_c: return False
    return True

def is_triangle(sides:list):
    '''Determine if the sides can create a triangle'''
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0: 
        pass
    else: return False
    if sides[0] + sides[1] > sides[2]: 
        pass
    else: return False
    if sides[1] + sides[1] > sides[0]: 
        pass
    else: return False
    if sides[0] + sides[2] > sides[1]: 
        pass
    else: return False
    return True