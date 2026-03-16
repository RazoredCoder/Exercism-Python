'''Shows the actual number of eggs in the coop.'''
def egg_count(display_value):
    '''Shows the actual number of eggs in the coop.'''
    eggs = display_value
    binary = ''
    while eggs > 0:
        binary += str(eggs % 2)
        eggs = eggs//2
    return sum(int(number) for number in binary)