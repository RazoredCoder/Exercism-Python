'''Determine whether a number is an Armstrong number.'''
def is_armstrong_number(number:int):
    num_list_str = list(str(number))
    num_list_int = [int(num_str) for num_str in num_list_str]
    return number == sum(num_int**len(num_list_int) for num_int in num_list_int)