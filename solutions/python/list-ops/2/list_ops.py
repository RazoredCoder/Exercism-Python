'''Implement basic list operations.'''
def append(list1, list2):
    '''Given two lists, add all items in the second list to the end of the first list'''
    for element in list2:
        list1.append(element)
    return list1


def concat(lists):
    '''Given a series of lists, combine all items in all lists into one flattened list'''
    flattened = []
    for element in lists:
        if isinstance(element, list):
            flattened.extend(element)
        else:
            flattened.append(element)
    return flattened


def filter(function, list):
    '''Given a predicate and a list, return the list of all items for which predicate(item) is True'''
    return [element for element in list if function(element)]


def length(list):
    '''Given a list, return the total number of items within it'''
    return sum(1 for element in list)


def map(function, list):
    '''Given a function and a list, return the list of the results of applying function(item) on all items'''
    return [function(element) for element in list]


def foldl(function, list, initial):
    '''Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left'''
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function, list, initial):
    '''Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right'''
    for element in list[-1::-1]:
        initial = function(initial, element)
    return initial


def reverse(list):
    '''Given a list, return a list with all the original items, but in reversed order'''
    return list[-1::-1]
