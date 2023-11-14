from operator import is_
from re import L


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.replace(" ","").lower()
    letters = list(phrase)
    loops = len(letters) // 2
    is_pal = True
    loop = 0
    while loop <= loops:
        print(letters[loop], letters[-(loop+1)])
        is_pal = False if letters[loop] != letters[-(loop+1)] else True
        loop += 1
    return is_pal

print(is_palindrome('taco cat'))
print(is_palindrome('Noon'))
print(is_palindrome('robert'))