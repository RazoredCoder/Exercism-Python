def append(list1, list2):
    for element in list2:
        list1.append(element)
    return list1


def concat(lists):
    flattened = []
    for element in lists:
        if isinstance(element, list):
            flattened.extend(element)
        else:
            flattened.append(element)
    return flattened


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    return sum(1 for element in list)


def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function, list, initial):
    for element in list[-1::-1]:
        initial = function(initial, element)
    return initial


def reverse(list):
    return list[-1::-1]
