def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    lst = list(phrase)
    lst.reverse()
    reversed = lst
    return "".join(reversed)

print(reverse_string('awesome'))
print(reverse_string('sauce'))