'''Calculate the correct score earned by a dart landing at that point.'''
def score(x, y):
    '''Calculate the correct score earned by a dart landing at that point.
    :param x: int or float - position x of the dart
    :param y: int or float - position y of the dart
    :result: int - number of points earned
    '''
    distance = abs((x**2 + y**2)**0.5)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0