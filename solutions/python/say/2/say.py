"""Given a number, your task is to express it in English words exactly as your friend should say it out loud."""
def say(number):
    """Given a number, your task is to express it in English words exactly as your friend should say it out loud.
    :param number: int - a number between 0-999,999,999,999
    :return: str - the number expressed in english words
    """
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion"]

    def convert_hundreds(num):
        result = []

        if num >= 100:
            result.append(ones[num // 100])
            result.append("hundred")
            num %= 100
        
        if num >= 20:
            result.append(tens[num // 10])
            if num % 10:
                result[-1] += "-" + ones[num % 10]
        elif num >= 10:
            result.append(teens[num - 10])
        elif num > 0:
            result.append(ones[num])
        
        return " ".join(result)
    
    groups = []
    while number > 0:
        groups.append(number % 1000)
        number //= 1000
    
    result = []
    for index in range(len(groups) - 1, -1, -1):
        if groups[index] > 0:
            result.append(convert_hundreds(groups[index]))
            if scales[index]:
                result[-1] += " " + scales[index]

    return " ".join(result)