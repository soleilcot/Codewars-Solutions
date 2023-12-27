# The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
# They would like your help with an application form that will tell prospective members
# which category they will be placed.
#
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
#
# Input
#
# Input will consist of a list of pairs. Each pair contains information for a single potential member.
# Information consists of an integer for the person's age and an integer for the person's handicap.
#
# Output
#
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the
# respective member is to be placed in the senior or open category.
#
# Example
#
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]


def process_member(arr):
    """
    Determine the membership category for a single potential member.

    Args:
        arr (list): A list containing two elements. The first element is an integer representing the age of the member,
                    and the second element is an integer representing the member's handicap.

    Returns:
        str: Returns "Senior" if the member is at least 55 years old and has a handicap greater than 7.
             Otherwise, returns "Open".
    """
    if arr[0] >= 55 and arr[1] > 7:
        return "Senior"

    return "Open"


def open_or_senior(data):
    """
    Process a list of potential members to determine their membership categories.

    Args:
    data (list of lists): A list where each element is a list containing two integers.
                          The first integer represents the age, and the second integer represents the handicap
                          of a potential member.

    Returns:
        list: A list of strings, where each string indicates the membership category ("Senior" or "Open")
            for the respective member in the input list.
    """
    return list(map(process_member, data))
