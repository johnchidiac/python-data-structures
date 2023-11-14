def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiou'
    start = 0
    phrase = list(s)
    end = len(phrase) - 1
    while start < end:

        while start < end and phrase[start] not in vowels:
            start += 1
        while start < end and phrase[end] not in vowels:
            end -= 1
        
        if start < end:
            phrase[start], phrase[end] = phrase[end], phrase[start]
            start += 1
            end -= 1

    return "".join(phrase)

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print( reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))