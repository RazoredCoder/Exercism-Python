'''Take a nested array of any depth and return a fully flattened array.'''
def flatten(iterable):
    '''Take a nested array of any depth and return a fully flattened array.
    :param iterable: (list, tuple) - a nested array to flatten
    :return: list - a flattened array
    '''
    flattened = []
    for element in iterable:
        if isinstance(element, (list, tuple)):
            flattened.extend(flatten(element))
        elif element is not None:
            flattened.append(element)
    return flattened