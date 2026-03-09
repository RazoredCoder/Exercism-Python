'''A binary search algorithm'''
def find(search_list:list, value:int):
    '''A binary search algorithm
    :param: search_list: list - a list to search in
    :value: int - a number to search for
    :return: int - an index of this number
    '''
    if not search_list:
        raise ValueError("value not in array")
    
    middle_index = len(search_list)//2
    if value > search_list[middle_index]:
        return middle_index + 1 + find(search_list[middle_index+1:], value)
    if value < search_list[middle_index]:
        return find(search_list[:middle_index], value)
    return middle_index