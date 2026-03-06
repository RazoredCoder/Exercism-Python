def leap_year(year:int):
    '''Determine whether a given year is a leap year.

    :param year: int - a year to check
    :return: bool - True or False if the year is a leap year 
    '''
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    return False