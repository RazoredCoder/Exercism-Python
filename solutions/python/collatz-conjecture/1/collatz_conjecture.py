def steps(number:int):
    if number is not int and number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps_num = 0
    num_float = float(number)
    while num_float > 1:
        if int(num_float) % 2 == 0:
            num_float /= 2
        else:
            num_float = num_float*3 + 1
        steps_num += 1
    if int(num_float) == 1:
        return steps_num
    return None