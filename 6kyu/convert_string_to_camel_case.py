# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

import re


def to_camel_case(text):
    """
    Convert a string into camel case format.

    This function takes a string that may contain hyphens (-) or underscores (_)
    and converts it to camel case format. Each character following a hyphen or
    underscore is capitalized and the hyphen/underscore is removed.

    Args:
        text (str): The string to be converted into camel case.

    Returns:
        str: The camel case version of the input string.

    Examples:
        >>> to_camel_case("the-stealth-warrior")
        'theStealthWarrior'
        >>> to_camel_case("The_Stealth_Warrior")
        'TheStealthWarrior'
    """
    # Pattern isolates the letter following the delimiter in capture group 1
    pattern = r"[_-]([a-zA-Z])"

    # Replaces the delimiter and letter with the uppercase letter
    return re.sub(pattern, replace_with_uppercase, text)


def replace_with_uppercase(match):
    """
    Replace a regex match with its uppercase equivalent.

    This function is used as a replacement function in re.sub. It takes a regex match
    object and returns the first captured group (a letter) in uppercase.

    Args:
        match: The regex match object.

    Returns:
        str: The uppercase version of the first captured group in the match.
    """
    return match.group(1).upper()


cases = ["the-stealth-warrior", "The_Stealth_Warrior", "The_Stealth-Warrior"]

for case in cases:
    print(to_camel_case(case))
