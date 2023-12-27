# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input
# will be a non-negative integer.

# Examples

#      16  -->  1 + 6 = 7
#     942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#  132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#  493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


def digital_root(n: int) -> int:
    """
    Calculate the digital root of a non-negative integer.

    The digital root is obtained by recursively summing the digits of the integer
    until a single-digit number is produced.

    Parameters:
    n (int): A non-negative integer whose digital root is to be calculated.

    Returns:
    int: The digital root of the input integer.

    Examples:
    >>> digital_root(16)
    7
    >>> digital_root(942)
    6
    >>> digital_root(132189)
    6
    >>> digital_root(493193)
    2
    """
    temp_root_sum = 0
    int_str = str(n)

    if len(int_str) == 1:
        return n

    for char in int_str:
        temp_root_sum += int(char)

    return digital_root(temp_root_sum)
