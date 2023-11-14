def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    result = True
    num1_digits = [int(digit) for digit in str(num1)]
    num2_digits = [int(digit) for digit in str(num2)]
    for num in num1_digits:
        if num1_digits.count(num) != num2_digits.count(num):
            result = False
    return result

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))